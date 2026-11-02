"""Memoria locale: sorgenti, osservazioni, enunciati e revisioni collegate.

Il Core non conosce campi o regole delle bollette. SQLite è la persistenza
di questa slice, non il contratto definitivo del modello concettuale.
"""

import hashlib
import io
import json
import sqlite3
import uuid
import zipfile
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path


class ConflictError(ValueError):
    pass


def uid():
    return uuid.uuid4().hex


def now():
    return datetime.now(timezone.utc).isoformat()


def encoded(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


class Store:
    def __init__(self, folder):
        self.folder = Path(folder).resolve()
        self.folder.mkdir(parents=True, exist_ok=True)
        self.path = self.folder / "fold.sqlite3"
        with self.connection() as db:
            version = db.execute("PRAGMA user_version").fetchone()[0]
            if version not in (0, 1):
                raise ValueError("Versione dati non supportata. Usa la versione di Fold che li ha creati.")
            db.executescript("""
                CREATE TABLE IF NOT EXISTS sources (
                    id TEXT PRIMARY KEY, sha256 TEXT NOT NULL UNIQUE, filename TEXT NOT NULL,
                    content BLOB NOT NULL, created_at TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS acquisitions (
                    id TEXT PRIMARY KEY, source_id TEXT NOT NULL REFERENCES sources(id),
                    channel TEXT NOT NULL, created_at TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS observations (
                    id TEXT PRIMARY KEY, source_id TEXT NOT NULL REFERENCES sources(id),
                    page INTEGER NOT NULL CHECK(page > 0), text TEXT NOT NULL, method TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS subjects (
                    id TEXT PRIMARY KEY, kind TEXT NOT NULL, title TEXT NOT NULL,
                    revision INTEGER NOT NULL DEFAULT 0, created_at TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS subject_sources (
                    subject_id TEXT NOT NULL REFERENCES subjects(id),
                    source_id TEXT NOT NULL REFERENCES sources(id), role TEXT NOT NULL,
                    PRIMARY KEY(subject_id, source_id));
                CREATE TABLE IF NOT EXISTS contributions (
                    id TEXT PRIMARY KEY, subject_id TEXT NOT NULL REFERENCES subjects(id),
                    target TEXT NOT NULL, actor TEXT NOT NULL, received_json TEXT NOT NULL,
                    created_at TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS assertions (
                    id TEXT PRIMARY KEY, subject_id TEXT NOT NULL REFERENCES subjects(id),
                    predicate TEXT NOT NULL, value_json TEXT NOT NULL, origin TEXT NOT NULL,
                    observation_id TEXT REFERENCES observations(id), excerpt TEXT,
                    contribution_id TEXT REFERENCES contributions(id), rule TEXT,
                    supersedes_id TEXT REFERENCES assertions(id), created_at TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS selections (
                    subject_id TEXT NOT NULL REFERENCES subjects(id), predicate TEXT NOT NULL,
                    assertion_id TEXT NOT NULL REFERENCES assertions(id),
                    PRIMARY KEY(subject_id,predicate));
                CREATE INDEX IF NOT EXISTS assertions_by_subject ON assertions(subject_id,predicate);
                PRAGMA user_version=1;
            """)

    @contextmanager
    def connection(self):
        db = sqlite3.connect(self.path, timeout=10)
        db.row_factory = sqlite3.Row
        db.execute("PRAGMA foreign_keys=ON")
        try:
            with db:
                yield db
        finally:
            db.close()

    def lookup(self, digest):
        with self.connection() as db:
            row = db.execute("""SELECT ss.subject_id FROM sources s JOIN subject_sources ss
                              ON ss.source_id=s.id WHERE s.sha256=? ORDER BY ss.subject_id LIMIT 1""", (digest,)).fetchone()
            return row[0] if row else None

    def import_document(self, content, filename, pages, candidates, kind, channel="upload", extraction_method="native-text"):
        digest = hashlib.sha256(content).hexdigest()
        timestamp = now()
        with self.connection() as db:
            db.execute("BEGIN IMMEDIATE")
            previous = db.execute("SELECT id, content FROM sources WHERE sha256=?", (digest,)).fetchone()
            if previous:
                if bytes(previous["content"]) != content:
                    raise ValueError("Conflitto di integrità del documento.")
                db.execute("INSERT INTO acquisitions VALUES (?,?,?,?)", (uid(), previous["id"], channel, timestamp))
                subject = db.execute("SELECT subject_id FROM subject_sources WHERE source_id=?", (previous["id"],)).fetchone()
                return subject[0], True
            source_id, subject_id = uid(), uid()
            db.execute("INSERT INTO sources VALUES (?,?,?,?,?)", (source_id, digest, filename, content, timestamp))
            db.execute("INSERT INTO acquisitions VALUES (?,?,?,?)", (uid(), source_id, channel, timestamp))
            db.execute("INSERT INTO subjects VALUES (?,?,?,?,?)", (subject_id, kind, filename, 0, timestamp))
            db.execute("INSERT INTO subject_sources VALUES (?,?,?)", (subject_id, source_id, "original"))
            observation_ids = {}
            for page, text in enumerate(pages, 1):
                observation_id = uid()
                observation_ids[page] = observation_id
                db.execute("INSERT INTO observations VALUES (?,?,?,?,?)",
                           (observation_id, source_id, page, text, extraction_method))
            groups = {}
            for candidate in candidates:
                assertion_id = uid()
                value = encoded(candidate["value"])
                predicate = candidate["predicate"]
                db.execute("INSERT INTO assertions VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                           (assertion_id, subject_id, predicate, value, "document",
                            observation_ids[candidate["page"]], candidate["excerpt"], None,
                            candidate["rule"], None, timestamp))
                # Multiple occurrences with the same value do not become independent votes.
                groups.setdefault(predicate, {}).setdefault(value, assertion_id)
            for predicate, values in groups.items():
                if len(values) == 1:
                    db.execute("INSERT INTO selections VALUES (?,?,?)", (subject_id, predicate, next(iter(values.values()))))
            return subject_id, False

    def list_subjects(self):
        with self.connection() as db:
            return [dict(row) for row in db.execute("SELECT * FROM subjects ORDER BY created_at DESC,id")]

    def subject(self, subject_id):
        with self.connection() as db:
            row = db.execute("SELECT * FROM subjects WHERE id=?", (subject_id,)).fetchone()
            if not row:
                raise KeyError("Documento non trovato.")
            result = dict(row)
            result["sources"] = [dict(x) for x in db.execute("""SELECT s.id,s.sha256,s.filename,s.created_at,
                       (SELECT count(*) FROM acquisitions a WHERE a.source_id=s.id) receptions,
                       EXISTS(SELECT 1 FROM acquisitions a WHERE a.source_id=s.id AND a.channel='demo') is_demo
                       FROM sources s JOIN subject_sources ss ON s.id=ss.source_id WHERE ss.subject_id=?""", (subject_id,))]
            selections = {x["predicate"]: x["assertion_id"] for x in db.execute("SELECT * FROM selections WHERE subject_id=?", (subject_id,))}
            history = []
            for record in db.execute("""SELECT a.*, o.page, o.source_id, c.received_json, c.actor
                       FROM assertions a LEFT JOIN observations o ON a.observation_id=o.id
                       LEFT JOIN contributions c ON a.contribution_id=c.id
                       WHERE a.subject_id=? ORDER BY a.created_at,a.rowid""", (subject_id,)):
                item = dict(record)
                item["value"] = json.loads(item.pop("value_json"))
                item["received"] = json.loads(item.pop("received_json")) if item["received_json"] else None
                item["selected"] = selections.get(item["predicate"]) == item["id"]
                history.append(item)
            result["assertions"] = history
            result["current"] = {item["predicate"]: item for item in history if item["selected"]}
            result["text_available"] = bool(db.execute("""SELECT 1 FROM observations o JOIN subject_sources ss
                     ON o.source_id=ss.source_id WHERE ss.subject_id=? AND trim(o.text)<>'' LIMIT 1""", (subject_id,)).fetchone())
            return result

    def revise(self, subject_id, predicate, value, revision, received, origin="human_correction", selected_id=None):
        with self.connection() as db:
            db.execute("BEGIN IMMEDIATE")
            row = db.execute("SELECT revision FROM subjects WHERE id=?", (subject_id,)).fetchone()
            if row is None:
                raise KeyError("Documento non trovato.")
            if row[0] != revision:
                raise ConflictError("La scheda è cambiata in un'altra finestra. Ricaricala prima di confermare.")
            previous = db.execute("SELECT assertion_id FROM selections WHERE subject_id=? AND predicate=?", (subject_id,predicate)).fetchone()
            if selected_id:
                candidate = db.execute("SELECT value_json FROM assertions WHERE id=? AND subject_id=? AND predicate=?",
                                       (selected_id,subject_id,predicate)).fetchone()
                if not candidate:
                    raise ValueError("L'alternativa scelta non appartiene a questo campo.")
                value = json.loads(candidate[0])
            assertion_id, contribution_id, timestamp = uid(), uid(), now()
            received = dict(received, selected_candidate=selected_id)
            db.execute("INSERT INTO contributions VALUES (?,?,?,?,?,?)",
                       (contribution_id, subject_id, previous[0] if previous else predicate, "Utente locale", encoded(received), timestamp))
            db.execute("INSERT INTO assertions VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                       (assertion_id,subject_id,predicate,encoded(value),origin,None,None,
                        contribution_id,None,previous[0] if previous else None,timestamp))
            db.execute("INSERT INTO selections VALUES (?,?,?) ON CONFLICT(subject_id,predicate) DO UPDATE SET assertion_id=excluded.assertion_id",
                       (subject_id,predicate,assertion_id))
            db.execute("UPDATE subjects SET revision=revision+1 WHERE id=?", (subject_id,))
            return assertion_id

    def source(self, source_id):
        with self.connection() as db:
            row = db.execute("SELECT * FROM sources WHERE id=?", (source_id,)).fetchone()
            if not row:
                raise KeyError("Originale non trovato.")
            data = bytes(row["content"])
            if hashlib.sha256(data).hexdigest() != row["sha256"]:
                raise ValueError("Il controllo di integrità dell'originale non è riuscito.")
            return row["filename"], data

    def backup(self):
        # A single transactional snapshot includes original bytes and all evidence links.
        with self.connection() as source:
            snapshot = sqlite3.connect(":memory:")
            try:
                source.backup(snapshot)
                database = snapshot.serialize()
                manifest = {"format": "fold-local/1", "created_at": now(), "tables": {}}
                for table in ("sources", "acquisitions", "observations", "subjects", "subject_sources", "contributions", "assertions", "selections"):
                    snapshot.row_factory = sqlite3.Row
                    manifest["tables"][table] = [{k: row[k] for k in row.keys() if k != "content"} for row in snapshot.execute("SELECT * FROM " + table)]
                output = io.BytesIO()
                with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
                    archive.writestr("fold.sqlite3", database)
                    archive.writestr("manifest.json", encoded(manifest))
                    archive.writestr("LEGGIMI.txt", "Backup Fold 0.1. Contiene documenti e dati personali, se importati.\nPer ripristinare: ferma Fold, estrai fold.sqlite3 in una cartella NUOVA e avvia Fold con --data-dir seguito dal percorso di quella cartella. Non sovrascrivere un archivio esistente.\n")
                    for row in snapshot.execute("SELECT sha256,content FROM sources"):
                        archive.writestr("originals/" + row["sha256"] + ".pdf", row["content"])
                return output.getvalue()
            finally:
                snapshot.close()
