#!/usr/bin/env python3

"""Download de indscannede billeder fra Chouinards udstyrskatalog fra 1972,
der skabte opmærksom om 'clean climbing'

Konverter til pdf:
convert *.jpg chouinard72.pdf

https://climbaz.com/chouinard72/chouinard.html
"""

import urllib.request

URL = "http://www.climbaz.com/chouinard72/graphics/{page}.JPG"
pages = ["cover"] + [f"page{page:02}" for page in range(72+1)]

for p in pages:
    durl = URL.format(page=p)
    urllib.request.urlretrieve(durl, f"{p}.jpg")
