#!/usr/bin/env python
"""List every line that involves randomness, and flag those with no visible seed.

    python tools/check_seed.py notebooks/D2_Topic08_LeQuan.ipynb [--seed 42]

This is a text heuristic, not a proof. It helps you review by eye; it cannot see seeds
hidden inside helper functions or libraries it does not know about.
"""
import json, re, sys

SEED = 42
if "--seed" in sys.argv:
    SEED = int(sys.argv[sys.argv.index("--seed") + 1])

RANDOM_CALLS = re.compile(
    r"\b(np\.random\.\w+|numpy\.random\.\w+|random\.(?!seed)\w+|\.sample\(|\.shuffle\(|"
    r"train_test_split|KFold|StratifiedKFold|ShuffleSplit|KMeans|RandomForest\w*|"
    r"GradientBoosting\w*|SGD\w*|TSNE|PCA\(|NMF|TruncatedSVD|default_rng|torch\.rand\w*)")
SEED_SET = re.compile(r"(np\.random\.seed|random\.seed|default_rng|manual_seed|random_state|seed)\s*[(=]\s*(\d+)")


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    nb = json.load(open(sys.argv[1], encoding="utf-8"))
    seeds_set, flagged = [], []
    for i, cell in enumerate(nb.get("cells", [])):
        if cell.get("cell_type") != "code":
            continue
        src = "".join(cell["source"]) if isinstance(cell["source"], list) else cell["source"]
        for ln, line in enumerate(src.splitlines(), 1):
            if line.lstrip().startswith(("#", "import ", "from ")):
                continue
            for m in SEED_SET.finditer(line):
                seeds_set.append((i, ln, line.strip(), int(m.group(2))))
            if RANDOM_CALLS.search(line) and not SEED_SET.search(line):
                flagged.append((i, ln, line.strip()))

    print(f"== seeds set ({len(seeds_set)}) ==")
    for i, ln, line, val in seeds_set:
        ok = "" if val == SEED else f"   <-- not {SEED}!"
        print(f"cell {i} line {ln}: {line}{ok}")
    print(f"\n== randomness with NO seed on the same line ({len(flagged)}) - review each ==")
    for i, ln, line in flagged:
        print(f"cell {i} line {ln}: {line}")
    print("\nNote: a global np.random.seed(%d) / random.seed(%d) earlier in the notebook covers "
          "calls that use the global generator, but NOT scikit-learn objects given no random_state "
          "when you want them independent of call order." % (SEED, SEED))


if __name__ == "__main__":
    main()
