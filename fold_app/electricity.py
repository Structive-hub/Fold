"""Semantica limitata delle bollette elettriche; nessuna dipendenza dal database."""

import re
from datetime import date
from decimal import Decimal, InvalidOperation

FIELDS = {
    "document_number": {"label": "Numero bolletta", "kind": "text"},
    "pod": {"label": "POD riportato", "kind": "text"},
    "amount_due": {"label": "Totale da pagare", "kind": "money"},
    "due_date": {"label": "Scadenza", "kind": "date"},
}
RULE_VERSION = "electricity-labels/1"
PATTERNS = {
    "document_number": r"(?:numero\s+bolletta|bolletta\s+n[.°º]?)\s*[:\-]?\s*([A-Z0-9][A-Z0-9/_.\-]{1,49})",
    "pod": r"\bPOD\s*[:\-]?\s*(IT[0-9A-Z]{12,13})\b",
    "amount_due": r"\btotale\s+da\s+pagare\s*[:\-]?\s*(?:EUR\s*|€\s*)?([0-9]+(?:\.[0-9]{3})*,[0-9]{2}|[0-9]+\.[0-9]{2})(?:\s*(?:EUR|€))?(?![0-9])",
    "due_date": r"(?:scadenza(?:\s+(?:del\s+)?pagamento)?|pagare\s+entro\s+il)\s*[:\-]?\s*([0-9]{1,2}/[0-9]{1,2}/[0-9]{4})\b",
}


def normalize(predicate, value):
    if predicate not in FIELDS:
        raise ValueError("Campo non supportato.")
    value = str(value).strip()
    if not value or len(value) > 100:
        raise ValueError("Inserisci un valore di massimo 100 caratteri.")
    if predicate == "amount_due":
        cleaned = value.replace("€", "").replace("EUR", "").strip()
        if "," in cleaned:
            if not re.fullmatch(r"(?:[0-9]+|[0-9]{1,3}(?:\.[0-9]{3})+),[0-9]{2}", cleaned):
                raise ValueError("Usa un importo come 84,72.")
            cleaned = cleaned.replace(".", "").replace(",", ".")
        if not re.fullmatch(r"[0-9]+(?:\.[0-9]{1,2})?", cleaned):
            raise ValueError("Usa un importo positivo con al massimo due decimali.")
        try:
            amount = Decimal(cleaned)
        except InvalidOperation as exc:
            raise ValueError("Importo non valido.") from exc
        if amount > Decimal("999999999.99"):
            raise ValueError("Importo troppo grande.")
        return {"amount": format(amount.quantize(Decimal("0.01")), ".2f"), "currency": "EUR"}
    if predicate == "due_date":
        try:
            if "/" in value:
                day, month, year = map(int, value.split("/"))
                parsed = date(year, month, day)
            else:
                parsed = date.fromisoformat(value)
        except (ValueError, TypeError) as exc:
            raise ValueError("Inserisci una data valida, per esempio 2026-11-20.") from exc
        return parsed.isoformat()
    if predicate == "pod":
        value = value.upper()
        if not re.fullmatch(r"IT[0-9A-Z]{12,13}", value):
            raise ValueError("Il POD atteso in questa versione è IT seguito da 12 o 13 lettere/cifre.")
    return value


def interpret(pages):
    """Propone solo corrispondenze esplicite; conserva tutte le alternative."""
    results = []
    for page_number, text in enumerate(pages, 1):
        for predicate, pattern in PATTERNS.items():
            for match in re.finditer(pattern, text, re.IGNORECASE):
                try:
                    value = normalize(predicate, match.group(1))
                except ValueError:
                    continue
                results.append({"predicate": predicate, "value": value,
                                "page": page_number, "excerpt": match.group(0),
                                "rule": RULE_VERSION})
    return results


def situation(fields, payment, today=None):
    today = today or date.today()
    due = fields.get("due_date", {}).get("value")
    if payment == "paid":
        return {"key": "paid", "label": "Pagamento dichiarato", "tone": "good",
                "reason": "Hai dichiarato il pagamento di questa bolletta. Fold conserva la dichiarazione; non è una verifica bancaria.",
                "reference_date": today.isoformat()}
    if due and date.fromisoformat(due) < today:
        label = "Scadenza superata · pagamento non verificato" if payment != "unpaid" else "Scadenza superata · da pagare secondo la tua dichiarazione"
        reason = "La data riportata è precedente a oggi. Il tempo trascorso non dimostra che la bolletta non sia stata pagata."
        return {"key": "overdue", "label": label, "tone": "attention", "reason": reason,
                "reference_date": today.isoformat()}
    if due:
        return {"key": "upcoming", "label": "Scadenza oggi" if due == today.isoformat() else "Scadenza in arrivo",
                "tone": "neutral", "reason": "La scadenza deriva dal dato selezionato qui sotto. Il pagamento rimane distinto.",
                "reference_date": today.isoformat()}
    return {"key": "unknown", "label": "Scadenza da chiarire", "tone": "neutral",
            "reason": "Non c'è una scadenza univoca disponibile. Puoi scegliere un'alternativa o inserire una correzione.",
            "reference_date": today.isoformat()}
