#!/usr/bin/env python
"""Compare the text outputs of two executed copies of the same notebook.

    python tools/compare_runs.py run1.ipynb run2.ipynb

Both files must have been executed (Restart and run all) and saved WITH outputs.
Prints every code cell whose text output differs. Memory addresses and timings are
masked, so remaining differences are real and need explaining (usually a missing seed).
"""
import json, re, sys

MASKS = [(re.compile(r"0x[0-9a-fA-F]+"), "0x…"),
         (re.compile(r"\b\d+(\.\d+)?\s?(ms|s|µs|us|sec|seconds)\b"), "<time>")]


def text_outputs(path):
    nb = json.load(open(path, encoding="utf-8"))
    res = []
    for i, cell in enumerate(nb.get("cells", [])):
        if cell.get("cell_type") != "code":
            continue
        chunks = []
        for o in cell.get("outputs", []):
            if o.get("output_type") == "stream":
                chunks.append("".join(o.get("text", [])))
            elif "data" in o and "text/plain" in o["data"]:
                chunks.append("".join(o["data"]["text/plain"]))
        t = "\n".join(chunks)
        for pat, rep in MASKS:
            t = pat.sub(rep, t)
        res.append((i, t))
    return res


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    a, b = text_outputs(sys.argv[1]), text_outputs(sys.argv[2])
    if len(a) != len(b):
        print(f"different number of code cells: {len(a)} vs {len(b)}")
    diffs = [(i, x, y) for (i, x), (_, y) in zip(a, b) if x != y]
    if not diffs:
        print(f"OK: text outputs identical in all {min(len(a), len(b))} code cells")
        return
    print(f"{len(diffs)} cell(s) differ:")
    for i, x, y in diffs:
        print(f"\n--- cell {i} run1 ---\n{x[:400]}\n--- cell {i} run2 ---\n{y[:400]}")
    sys.exit(1)


if __name__ == "__main__":
    main()
