"""Lettura PDF isolata dal processo web; nessuna interpretazione del dominio."""

import io
import json
import subprocess
import sys
import tempfile
from pathlib import Path

MAX_FILE_BYTES = 10 * 1024 * 1024
MAX_PAGES = 50


def read_pdf(data):
    from pypdf import PdfReader

    reader = PdfReader(io.BytesIO(data), strict=False)
    if reader.is_encrypted:
        raise ValueError("Il PDF è cifrato: usa una copia non protetta.")
    if len(reader.pages) > MAX_PAGES:
        raise ValueError("Questa versione accetta PDF con massimo 50 pagine.")
    pages = []
    for page in reader.pages:
        contents = page.get_contents()
        if contents is not None and len(contents.get_data()) > 8 * 1024 * 1024:
            raise ValueError("Una pagina è troppo complessa per questa prima versione.")
        text = page.extract_text() or ""
        if len(text) > 100_000:
            raise ValueError("Una pagina contiene troppo testo.")
        pages.append(text)
    if not pages:
        raise ValueError("Il PDF non contiene pagine.")
    return pages


def extract_pdf(data):
    if not data.startswith(b"%PDF-"):
        raise ValueError("Il file non sembra un PDF valido.")
    if len(data) > MAX_FILE_BYTES:
        raise ValueError("Il limite è 10 MB per documento.")
    with tempfile.TemporaryDirectory(prefix="fold-extract-") as folder:
        path = Path(folder) / "input.pdf"
        path.write_bytes(data)
        try:
            result = subprocess.run([sys.executable, "-m", "fold_app.extraction", str(path)],
                                    capture_output=True, timeout=25, check=False)
        except subprocess.TimeoutExpired as exc:
            raise ValueError("La lettura ha superato 25 secondi. L'importazione non è stata completata.") from exc
        if result.returncode or len(result.stdout) > 8 * 1024 * 1024:
            raise ValueError("Non è stato possibile leggere questo PDF. L'importazione non è stata completata.")
        payload = json.loads(result.stdout)
        if "error" in payload:
            raise ValueError(payload["error"])
        return payload["pages"]


if __name__ == "__main__":
    try:
        output = {"pages": read_pdf(Path(sys.argv[1]).read_bytes())}
    except ValueError as exc:
        output = {"error": str(exc)}
    except Exception:
        output = {"error": "Il PDF è danneggiato o usa un formato non leggibile in questa versione."}
    sys.stdout.buffer.write(json.dumps(output, ensure_ascii=False).encode("utf-8"))
