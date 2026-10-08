#!/usr/bin/env python3
"""Fill index.html's image data blocks from assets/*.webp.

Each <script type="text/plain" id="img-NAME"> block gets assets/NAME.webp as
base64. Re-run after swapping or re-cropping a photo in assets/.
"""
import base64, pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent.parent
page = root / "index.html"
html = page.read_text()

def fill(m):
    name = m.group(1)
    f = root / "assets" / f"{name}.webp"
    if not f.exists():
        sys.exit(f"missing {f}")
    data = base64.b64encode(f.read_bytes()).decode()
    return f'<script type="text/plain" id="img-{name}">{data}</script>'

html, n = re.subn(r'<script type="text/plain" id="img-([\w-]+)">[^<]*</script>', fill, html)
page.write_text(html)
print(f"embedded {n} images, index.html is {len(html.encode())//1024} KB")
