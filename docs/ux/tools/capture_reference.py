"""Capture real browser screenshots of the UX reference where Chromium is permitted.

Optional dependency: pip install playwright; python -m playwright install chromium.
Run: python docs/ux/tools/capture_reference.py
This runs an HTTP server serving the static prototype only; no Fold backend is used.
"""
from pathlib import Path
import contextlib
import http.server
import socketserver
import threading

root = Path(__file__).resolve().parents[1]
reference = root / "reference"
output = root / "screenshots"

class Server(socketserver.TCPServer):
    allow_reuse_address = True

@contextlib.contextmanager
def serve():
    handler = lambda *args, **kwargs: http.server.SimpleHTTPRequestHandler(*args, directory=str(reference), **kwargs)
    server = Server(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_address[1]}/"
    finally:
        server.shutdown()
        server.server_close()

if __name__ == "__main__":
    from playwright.sync_api import sync_playwright
    with serve() as url, sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        for label, width, height in [("desktop", 1440, 900), ("mobile", 390, 844)]:
            page = browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=1)
            page.goto(url)
            page.screenshot(path=str(output / f"situazione-{label}-browser.png"), full_page=True)
            if label == "mobile":
                page.locator("#mobileMenu").click()
            page.locator('[data-nav="archive"]').click()
            page.screenshot(path=str(output / f"utenze-{label}-browser.png"), full_page=True)
            page.locator('button[data-select="electricity"]').click()
            page.locator('.inspector button[data-doc="electricity"]').click()
            page.screenshot(path=str(output / f"documento-{label}-browser.png"), full_page=True)
            page.locator('#addDoc').click()
            page.screenshot(path=str(output / f"acquisizione-{label}-browser.png"), full_page=True)
            page.locator('[data-intake-tab="links"]').click()
            page.get_by_role('button', name='Esamina il contesto della casa').click()
            page.screenshot(path=str(output / f"bene-{label}-browser.png"), full_page=True)
            page.close()
        browser.close()
    print("Browser screenshots exported:", output)
