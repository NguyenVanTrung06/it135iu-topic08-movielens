# IT135IU – Topic 8: Which films should a streaming service promote to a given audience?

Course project for **IT135IU – Introduction to Data Science** (VNU-HCM International University).

- **Dataset:** MovieLens 1M (GroupLens Research)
- **Group:** 08


---

## Repository layout

```text
.
├── notebooks/
│   └── D2_Topic08_Phuong_LeQuan_Que_HoangQuan_Tuyen_Trung_Cuong.ipynb   # main analysis notebook (D2 – Data Profiling)
├── tools/                        # small helper scripts for reproducibility
│   ├── freeze_from_notebook.py
│   ├── clean_notebook.py
│   ├── check_seed.py
│   └── compare_runs.py
├── .gitignore                    # blocks data files (*.dat, *.csv, *.parquet)
├── requirements.txt              # exact package versions from the environment that ran the notebook
└── README.md
```

---

## Data (not included)

The MovieLens 1M data files are **not committed** to this repository (they are blocked by `.gitignore`). The notebook **automatically downloads and extracts** the dataset from GroupLens into the runtime's temporary storage while it runs:

`https://files.grouplens.org/datasets/movielens/ml-1m.zip`

No manual download or `data/` folder setup is required. An active internet connection is needed to run the notebook.

**Why is the data not in the repo?** The dataset belongs to GroupLens and its terms of use do not allow redistributing it. Keeping it out also keeps the repo small, and anyone can fetch the exact same files from the official source.

**Citation required by the terms:** F. M. Harper and J. A. Konstan, "The MovieLens Datasets: History and Context", *ACM Transactions on Interactive Intelligent Systems* 5(4), 2015.

---

## How to reproduce

1. Use **Python `<PYTHON_VERSION>`** (the notebook was originally executed on Google Colab; replace with the version printed by the notebook / `env_report.txt`).
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Open `D2_Topic08_Phuong_LeQuan_Que_HoangQuan_Tuyen_Trung_Cuong.ipynb` and choose **Restart and run all**. The dataset is downloaded automatically.

All randomness is seeded with **`SEED = 42`** at Step 1 so that runs give identical numbers. The current D2 profiling steps do not use random sampling, but the seed is set so later deliverables stay reproducible.

---

## Helper scripts

| Script | Purpose |
|---|---|
| `tools/freeze_from_notebook.py` | writes `requirements.txt` and `env_report.txt` from the real environment |
| `tools/clean_notebook.py` | removes personal metadata (Colab `executionInfo`) before committing |
| `tools/check_seed.py` | lists every line that uses randomness and whether a seed is visible |
| `tools/compare_runs.py` | compares the text outputs of two executed runs |

---

## Responsible use

- **Source and terms of use:** see "Data (not included)" above.
- **AI assistance:** AI tools (ChatGPT, Gemini, Claude) were used to draft the repository skeleton (README, tool scripts), assist with Git/GitHub commands, and explain specific pandas/Python functions. All AI-generated output and analysis was reviewed and verified by the project team.
- **Known data limitations:**
  - *Time period:* ratings were collected from 2000 to 2003 and may not reflect modern streaming audiences.
  - *Rating scale:* ratings are discrete integers from 1 to 5 (no half-stars).
  - *Selection bias:* only users with at least 20 ratings are included. Demographic fields (age, gender, occupation) are self-reported and binned into categories.