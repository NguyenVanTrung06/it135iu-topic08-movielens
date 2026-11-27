# IT135IU – Topic 8: Which films should a streaming service promote to a given audience?

Course project for **IT135IU – Introduction to Data Science** (VNU-HCM International University).

- **Dataset:** MovieLens 1M (GroupLens Research)
- **Group:** Group 3, Topic 08

## Repository layout

```text
.
├── .gitignore                              # excludes data files and generated artifacts
├── README.md
├── REPRODUCIBILITY_REPORT_TEMPLATE.md
├── requirements.txt                        # pinned environment dependencies
├── data/
│   ├── .gitkeep                            # keeps the directory in version control
│   └── README.md
├── notebooks/
│   ├── D2_Topic08_Phuong_LeQuan_Que_HoangQuan_Tuyen_Trung_Cuong.ipynb
│   ├── D3_Topic08_Phuong_LeQuan_Que_HoangQuan_Tuyen_Trung_Cuong.ipynb
│   └── D3_Topic08_Phuong_LeQuan_Que_HoangQuan_Tuyen_Trung_Cuong.pdf
├── report/
│   ├── analystA/
│   │   ├── D3_check_Que.csv
│   │   ├── D3_Analyst_A_Que.ipynb
│   │   └── D3_Analyst_A_Que_notes.pdf
│   ├── analystB/
│   │   ├── D3_Analyst_B_HoangQuan.ipynb
│   │   ├── D3_Analyst_B_HoangQuan_notes_v2.pdf
│   │   └── D3_columns_HoangQuan_v2.pdf
│   ├── Ethics/
│   │   └── D3_Ethics_Cuong_v2.pdf
│   ├── productOwner/
│   │   └── D3_ProductOwner_Phuong_v2.pdf
│   └── Visualization/
│       └── D3_Viz_Tuyen.ipynb
└── tools/
    ├── check_seed.py                        # checks visible random seeds
    ├── clean_notebook.py                    # removes personal notebook metadata
    ├── compare_runs.py                      # compares executed notebook outputs
    └── freeze_from_notebook.py              # records environment dependencies
```

## Data (not included)

The MovieLens 1M data files are **not committed** to this repository (they are blocked by `.gitignore`). The notebook automatically downloads and extracts the dataset from GroupLens into temporary storage:

`https://files.grouplens.org/datasets/movielens/ml-1m.zip`

An active internet connection is required for automatic download.

### If data download fails

Download [`ml-1m.zip`](https://grouplens.org/datasets/movielens/1m/) manually and place it in the repository's `data/` directory.

**Why is the data not in the repo?** The dataset belongs to GroupLens, and its terms of use do not allow redistribution. Keeping it out also keeps the repository small. Users can obtain the same files from the official source.

**Citation required by the terms:** F. M. Harper and J. A. Konstan, “The MovieLens Datasets: History and Context,” *ACM Transactions on Interactive Intelligent Systems* 5(4), 2015.

## How to reproduce

1. Use **Python 3.13.18**.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Open `notebooks/D3_Topic08_Phuong_LeQuan_Que_HoangQuan_Tuyen_Trung_Cuong.ipynb` and choose **Restart and run all**. The dataset is downloaded automatically.

All randomness is seeded globally with **`SEED = 42`** (`np.random.seed(SEED)` for the Step B1 user split, and `np.random.default_rng(SEED)` for 1,000 bootstrap resamples in Steps B4–B6 and 10,000 resamples in Step B8) to guarantee reproducible results.

## Helper scripts

| Script | Purpose |
|---|---|
| `tools/freeze_from_notebook.py` | Writes `requirements.txt` and `env_report.txt` from the real environment |
| `tools/clean_notebook.py` | Removes personal metadata (Colab `executionInfo`) before committing |
| `tools/check_seed.py` | Lists lines that use randomness and whether a seed is visible |
| `tools/compare_runs.py` | Compares the text outputs of two executed runs |

## Team & Contributions (Group 3)

- **Phuong** – Product Owner (problem framing, KPI definition, business recommendations)
- **Le Quan (`Aqvanax`)** – Data Engineering & Base D3 Pipeline (data cleaning, demographic segmentation, Step B1 user split)
- **Que** – Analyst A (descriptive statistics & segment/genre summary tables, Steps Q0–Q2)
- **Hoang Quan** – Analyst B (LCB ranking, baseline estimation & bootstrap hypothesis testing, Steps B2–B9)
- **Tuyen** – Data Visualization (charts & visual communication, Steps B10.1–B10.4)
- **Trung** – Reproducibility Lead (repository architecture, dependency pinning, notebook merging & verification)
- **Cuong** – Ethics & Governance Lead (bias audit, privacy & responsible use assessment)

## Responsible use

- **Source and terms of use:** See “Data (not included)” above.
- **AI assistance:** AI tools (ChatGPT, Gemini, Claude) were used to draft the repository skeleton (README and tool scripts), assist with Git/GitHub commands, and explain specific pandas and Python functions. The project team reviewed and verified all AI-generated output and analysis.
- **Known data limitations:**
  - *Time period:* Ratings were collected from 2000 to 2003 and may not reflect modern streaming audiences.
  - *Rating scale:* Ratings are discrete integers from 1 to 5, with no half-stars.
  - *Selection bias:* Only users with at least 20 ratings are included. Demographic fields (age, gender, occupation) are self-reported and grouped into categories.