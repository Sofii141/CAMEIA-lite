"""Convierte un documento HTML del proyecto a PDF con Microsoft Edge en modo invisible.

Uso: python _Estilo/html_a_pdf.py "ruta/documento.html"  → crea "ruta/documento.pdf"
"""
import subprocess
import sys
from pathlib import Path

EDGE = [r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"]

html = Path(sys.argv[1]).resolve()
pdf = html.with_suffix(".pdf")
edge = next((e for e in EDGE if Path(e).exists()), None)
if not edge:
    sys.exit("No se encontró Microsoft Edge.")
subprocess.run([edge, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--allow-file-access-from-files", "--virtual-time-budget=20000", "--run-all-compositor-stages-before-draw",
                f"--print-to-pdf={pdf}", html.as_uri()], check=True, capture_output=True)
print(f"PDF generado: {pdf}")
