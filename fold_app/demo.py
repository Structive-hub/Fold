"""PDF sintetico, generato senza librerie; nessun documento personale."""

from datetime import date, timedelta


def example_pdf():
    due = (date.today() - timedelta(days=3)).strftime("%d/%m/%Y")
    lines = ["FOLD - DOCUMENTO DI ESEMPIO", "Dati interamente fittizi - non valido per il pagamento",
             "Bolletta n. DEMO-001", "POD: IT001E12345678", "Totale da pagare: 84,72 EUR",
             f"Scadenza: {due}", "Modalita di pagamento: bonifico",
             "La modalita di pagamento non attesta un pagamento avvenuto."]
    commands = ["BT /F1 16 Tf 50 780 Td"]
    for i, line in enumerate(lines):
        if i:
            commands.append("0 -34 Td")
        commands.append("(" + line.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)") + ") Tj")
    commands.append("ET")
    stream = "\n".join(commands).encode("latin-1")
    objects = [b"<< /Type /Catalog /Pages 2 0 R >>",
               b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
               b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>",
               b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
               b"<< /Length " + str(len(stream)).encode() + b" >>\nstream\n" + stream + b"\nendstream"]
    result = bytearray(b"%PDF-1.4\n")
    offsets = [0]
    for i, obj in enumerate(objects, 1):
        offsets.append(len(result))
        result.extend(f"{i} 0 obj\n".encode() + obj + b"\nendobj\n")
    xref = len(result)
    result.extend(f"xref\n0 {len(objects)+1}\n0000000000 65535 f \n".encode())
    for offset in offsets[1:]:
        result.extend(f"{offset:010d} 00000 n \n".encode())
    result.extend(f"trailer\n<< /Size 6 /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode())
    return bytes(result)
