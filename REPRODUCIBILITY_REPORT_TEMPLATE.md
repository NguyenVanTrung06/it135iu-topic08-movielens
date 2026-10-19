# Re-run report – D2 notebook (Reproducibility Lead)

**Notebook:** D2_Topic08_LeQuan.ipynb, version/date frozen: ____ (fill in: time of Lê Quân's "final" message)
**Run by:** Trung   **Date:** 20/10/2026 (runs at about 1:20 AM and 1:23 AM)

## Environment (copy from `env_report.txt`, do not type from memory)
- Platform / runtime: Google Colab, runtime type: CPU (Python 3 Google Compute Engine backend, 12.7 GB RAM, no GPU)
- Python: 3.13.16
- Key packages: pandas 2.2.3, numpy 2.1.3, matplotlib n/a (not imported), scipy n/a (not imported), _others_ none (`io`, `urllib.request`, `zipfile`, `typing` are part of the Python standard library)

## Result of "Restart session and run all" (fresh Colab, nothing carried over)
- [ ] Ran end to end without error (tick after checking that no cell shows an error)
- Errors (cell number, message, suspected cause): ____ (write "none" if there is no error)
- Data loading worked from a clean runtime: yes, the notebook downloads `ml-1m.zip` from GroupLens automatically (no data file in the repo). The working table has 1,000,209 rows x 10 columns.
- Run time: ____

## Determinism (two runs)
- Output of `tools/compare_runs.py run1 run2`: `OK: text outputs identical in all 16 code cells`
- Differences and explanation: none. Memory addresses and timings are masked by the script. The "Step 9" data profile (1,000,209 rows x 10 columns, same min/max for every column) is identical in both runs.

## Seed audit (`tools/check_seed.py`)
- Seed 42 set at: cell 3, line 9 (`np.random.seed(SEED)`, with `SEED = 42`)
- Randomness with no visible seed: none. The only line flagged by the script is the seed-setting line itself. The script printed "seeds set (0)" because it looks for the literal number 42 and the notebook uses the variable `SEED`, so this is a false positive. D2 only profiles data and does not use random sampling.

## PDF export
- [ ] Every code cell has its output
- [ ] Figures present, axes labelled
- Missing/truncated outputs: ____

## Repository check
- [ ] No *.dat / *.csv / *.parquet tracked (`git ls-files | grep -E '\.(dat|csv|parquet)$'` is empty)
- [ ] `executionInfo` / account name / userId removed (`tools/clean_notebook.py`)
- [ ] Another member cloned, installed from requirements.txt and ran it without asking: ____
