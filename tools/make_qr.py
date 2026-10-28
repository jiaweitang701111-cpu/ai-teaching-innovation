# -*- coding: utf-8 -*-
"""Make share/QRcode.png for the deck URL.
Uses the qrcode-generator JS that is bundled inside index.html (run through
Node) plus Pillow, so no extra Python packages are needed.
usage: python tools/make_qr.py <url> <out.png>
"""
import sys, re, io, base64, pathlib, subprocess, tempfile
from PIL import Image

url, out = sys.argv[1], pathlib.Path(sys.argv[2])
root = pathlib.Path(__file__).resolve().parent.parent
html = (root / "index.html").read_text(encoding="utf-8")
lib = re.search(r"var qrcode=function\(\).*?qrcode\}\)\);", html, re.S).group(0)
runner = lib + """
const q=qrcode(0,'M');q.addData(process.argv[2],'Byte');q.make();
process.stdout.write(q.createDataURL(1,0));
"""
with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
    f.write(runner)
data_url = subprocess.check_output(["node", f.name, url], text=True)
pathlib.Path(f.name).unlink()
qr = Image.open(io.BytesIO(base64.b64decode(data_url.split(",", 1)[1]))).convert("L")
n, cell, quiet = qr.width, 20, 4            # n = modules per side
img = Image.new("L", ((n + 2 * quiet) * cell,) * 2, 255)
img.paste(qr.resize((n * cell, n * cell), Image.NEAREST), (quiet * cell, quiet * cell))
img.save(out, optimize=True)
print("saved", out, img.size, "modules", n)
