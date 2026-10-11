#!/usr/bin/env python
"""Strip personal metadata from a notebook before committing it.

    python tools/clean_notebook.py notebooks/D2_Topic08_LeQuan.ipynb

Removes, in place:
  * cell.metadata.executionInfo   (Colab: displayName, userId, user_tz, timings)
  * notebook.metadata.colab.provenance, and notebook.metadata.widgets (breaks GitHub preview)
Then scans the whole file for things that still look personal and prints them so you can
fix them by hand: e-mail addresses, Google Drive paths, /Users/ or /home/ paths.
Outputs and execution counts are kept (the PDF/figures need them).
"""
import json, re, sys

PATTERNS = {
    "email": re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+"),
    "drive path": re.compile(r"/content/drive/[^\s\"']*"),
    "home path": re.compile(r"/(?:Users|home)/[^\s\"'/]+"),
}


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    path = sys.argv[1]
    nb = json.load(open(path, encoding="utf-8"))
    n = 0
    for cell in nb.get("cells", []):
        if cell.get("metadata", {}).pop("executionInfo", None) is not None:
            n += 1
    meta = nb.get("metadata", {})
    if isinstance(meta.get("colab"), dict):
        meta["colab"].pop("provenance", None)
    meta.pop("widgets", None)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(f"removed executionInfo from {n} cell(s)")

    text = open(path, encoding="utf-8").read()
    clean = True
    for name, pat in PATTERNS.items():
        hits = sorted(set(pat.findall(text)))
        if hits:
            clean = False
            print(f"[check by hand] {name}: {hits[:10]}")
    if clean:
        print("no e-mail / Drive path / home path found")


if __name__ == "__main__":
    main()
