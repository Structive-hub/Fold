"""Server della sola anteprima locale: loopback, origini e scritture delimitate."""

import argparse
import hashlib
import json
import os
import re
import secrets
from importlib.metadata import version
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit

from . import electricity
from .core import ConflictError, Store
from .demo import example_pdf
from .extraction import MAX_FILE_BYTES, extract_pdf

STATIC = Path(__file__).parent / "static"


def present(store, subject_id):
    data = store.subject(subject_id)
    payment = data["current"].get("payment_status", {}).get("value", "unknown")
    data["situation"] = electricity.situation(data["current"], payment)
    data["field_definitions"] = electricity.FIELDS
    return data


class FoldServer(ThreadingHTTPServer):
    daemon_threads = True

    def __init__(self, address, store):
        super().__init__(address, Handler)
        self.store = store
        self.token = secrets.token_urlsafe(32)


class Handler(BaseHTTPRequestHandler):
    server_version = "FoldLocal/0.1"

    def log_message(self, format, *args):
        # Never print filenames, extracted contents or form values.
        pass

    def allowed_host(self):
        return self.headers.get("Host", "") in {
            f"127.0.0.1:{self.server.server_port}", f"localhost:{self.server.server_port}"}

    def send_bytes(self, data, content_type, status=200, filename=None):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'self'; style-src 'self'; object-src 'none'; frame-ancestors 'none'; base-uri 'none'; form-action 'self'")
        if filename:
            self.send_header("Content-Disposition", f'attachment; filename="{filename}"')
        self.end_headers()
        self.wfile.write(data)

    def send_json(self, value, status=200):
        self.send_bytes(json.dumps(value, ensure_ascii=False).encode("utf-8"), "application/json; charset=utf-8", status)

    def do_GET(self):
        if not self.allowed_host():
            return self.send_json({"error": "Indirizzo non autorizzato."}, 403)
        route = urlsplit(self.path).path
        try:
            if route == "/":
                html = (STATIC / "index.html").read_text(encoding="utf-8").replace("__FOLD_TOKEN__", self.server.token)
                return self.send_bytes(html.encode(), "text/html; charset=utf-8")
            if route in ("/app.js", "/style.css"):
                return self.send_bytes((STATIC / route[1:]).read_bytes(), "text/javascript; charset=utf-8" if route.endswith("js") else "text/css; charset=utf-8")
            if route == "/api/subjects":
                return self.send_json({"subjects": self.server.store.list_subjects()})
            match = re.fullmatch(r"/api/subjects/([a-f0-9]{32})", route)
            if match:
                return self.send_json(present(self.server.store, match[1]))
            match = re.fullmatch(r"/api/sources/([a-f0-9]{32})", route)
            if match:
                _, content = self.server.store.source(match[1])
                return self.send_bytes(content, "application/pdf", filename="originale-fold.pdf")
            if route == "/api/backup":
                return self.send_bytes(self.server.store.backup(), "application/zip", filename="fold-backup.zip")
            if route == "/api/example.pdf":
                return self.send_bytes(example_pdf(), "application/pdf", filename="bolletta-esempio.pdf")
            return self.send_json({"error": "Pagina non trovata."}, 404)
        except KeyError as exc:
            return self.send_json({"error": exc.args[0]}, 404)
        except ValueError as exc:
            return self.send_json({"error": str(exc)}, 422)
        except (BrokenPipeError, ConnectionResetError):
            return
        except Exception:
            return self.send_json({"error": "Errore locale durante la lettura. I dati non sono stati modificati."}, 500)

    def do_POST(self):
        expected_origins = {f"http://127.0.0.1:{self.server.server_port}", f"http://localhost:{self.server.server_port}"}
        if (not self.allowed_host() or self.headers.get("Origin") not in expected_origins
                or not secrets.compare_digest(self.headers.get("X-Fold-Token", ""), self.server.token)):
            return self.send_json({"error": "Richiesta non autorizzata: apri Fold dal suo indirizzo locale."}, 403)
        try:
            route = urlsplit(self.path).path
            if self.headers.get("Transfer-Encoding"):
                raise ValueError("Tipo di trasferimento non supportato.")
            length = int(self.headers.get("Content-Length", "0"))
            limit = MAX_FILE_BYTES if route == "/api/import" else 16_384
            if length < 0 or length > limit:
                return self.send_json({"error": "File troppo grande: il limite per i PDF è 10 MB."}, 413)
            self.connection.settimeout(30)
            body = self.rfile.read(length)
            if len(body) != length:
                raise ValueError("Trasferimento incompleto.")
            if route in ("/api/import", "/api/demo"):
                content = example_pdf() if route.endswith("demo") else body
                filename = "Bolletta di esempio.pdf" if route.endswith("demo") else unquote(self.headers.get("X-Filename", "Documento.pdf"))
                filename = re.split(r"[/\\]", filename)[-1]
                filename = "".join(c for c in filename if ord(c) >= 32)[:160] or "Documento.pdf"
                # Same-byte reimport still records reception, without rerunning the parser.
                existing = self.server.store.lookup(hashlib.sha256(content).hexdigest())
                pages = [] if existing else extract_pdf(content)
                subject_id, duplicate = self.server.store.import_document(content, filename, pages,
                         electricity.interpret(pages), "electricity_bill", "demo" if route.endswith("demo") else "upload",
                         extraction_method="pypdf/" + version("pypdf") + "/native-text")
                return self.send_json({"subject": present(self.server.store, subject_id), "duplicate": duplicate}, 200 if duplicate else 201)
            match = re.fullmatch(r"/api/subjects/([a-f0-9]{32})/revise", route)
            if match:
                if self.headers.get("Content-Type", "").split(";")[0] != "application/json":
                    raise ValueError("La richiesta deve contenere dati JSON.")
                data = json.loads(body)
                if not isinstance(data, dict) or type(data.get("revision")) is not int:
                    raise ValueError("Riferimento della revisione non valido.")
                predicate = data.get("predicate")
                note = data.get("note", "")
                if not isinstance(note, str) or not note.strip() or len(note) > 1000:
                    raise ValueError("Indica il motivo o il contenuto della dichiarazione (massimo 1000 caratteri).")
                if predicate == "payment_status":
                    value = data.get("value")
                    if value not in ("unknown", "paid", "unpaid"):
                        raise ValueError("Stato del pagamento non valido.")
                    origin = "human_declaration"
                else:
                    value = electricity.normalize(predicate, data.get("value", ""))
                    origin = "human_confirmation" if data.get("selected_id") else "human_correction"
                selected_id = data.get("selected_id")
                if selected_id is not None and (not isinstance(selected_id, str) or not re.fullmatch(r"[a-f0-9]{32}", selected_id)):
                    raise ValueError("Alternativa non valida.")
                self.server.store.revise(match[1], predicate, value, data["revision"],
                    {"value_entered": data.get("value"), "note": note.strip()}, origin, selected_id)
                return self.send_json(present(self.server.store, match[1]))
            return self.send_json({"error": "Operazione non trovata."}, 404)
        except ConflictError as exc:
            return self.send_json({"error": str(exc)}, 409)
        except KeyError as exc:
            return self.send_json({"error": exc.args[0]}, 404)
        except (ValueError, TypeError, json.JSONDecodeError) as exc:
            return self.send_json({"error": str(exc)}, 422)
        except (BrokenPipeError, ConnectionResetError):
            return
        except Exception:
            return self.send_json({"error": "Operazione non completata. Ricarica la scheda prima di riprovare."}, 500)


def main():
    parser = argparse.ArgumentParser(description="Fold — prima esperienza locale")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--data-dir", type=Path, default=Path(os.environ.get("LOCALAPPDATA", str(Path.home()))) / "Fold" / "local-preview")
    args = parser.parse_args()
    if not 1 <= args.port <= 65535:
        parser.error("La porta deve essere tra 1 e 65535.")
    try:
        import pypdf  # noqa: F401
    except ImportError:
        parser.exit(1, "Manca pypdf. Installa requirements.txt nel tuo ambiente Python.\n")
    try:
        server = FoldServer(("127.0.0.1", args.port), Store(args.data_dir))
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Avvio non riuscito: {exc}\n")
    print(f"Fold pronto: http://127.0.0.1:{server.server_port}", flush=True)
    print(f"Dati: {args.data_dir.resolve()}\nPremi Ctrl+C per fermare Fold.", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
