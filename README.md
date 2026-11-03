# Global Energy Intelligence
### A narrative-first exploratory data analysis of global energy systems

I use the Our World in Data energy dataset to investigate global energy use, electricity generation, renewable adoption, fossil-fuel dependence, and electricity carbon intensity. The project is organized as a sequence of research notebooks. Each analysis section states the question, explains the method, presents the code, and follows with a plain-English conclusion and limitations.

## Start here

1. Read this README.
2. Review [`reports/project_methodology.md`](reports/project_methodology.md) for analytical decisions.
3. Open the notebooks in numerical order.
4. Review the saved tables and figures under `outputs/`.
5. Read [`reports/executive_summary.md`](reports/executive_summary.md) for the high-level findings.

## Repository structure

```text
global-energy-intelligence-professional/
├── README.md
├── requirements.txt
├── data/
│   ├── owid_energy.csv
│   └── README.md
├── notebooks/
│   ├── 01_data_audit_and_preparation.ipynb
│   ├── 02_descriptive_and_distributional_analysis.ipynb
│   ├── 03_global_energy_trends.ipynb
│   ├── 04_country_benchmarking_and_energy_mix.ipynb
│   └── 05_statistical_analysis_and_robustness.ipynb
├── src/
│   ├── data_quality.py
│   ├── analysis_helpers.py
│   └── visualization_helpers.py
├── reports/
│   ├── executive_summary.md
│   ├── project_methodology.md
│   ├── data_dictionary.csv
│   ├── data_quality_report.md
│   └── statistical_findings.md
└── outputs/
    ├── figures/
    └── tables/
```

## Environment setup

Python 3.10+ is recommended.

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
jupyter lab
```

Run notebooks from the repository root in numeric order. The notebooks use relative paths and save generated outputs under `outputs/`.

## Research questions

- How have global energy consumption and electricity generation changed over time?
- How has the electricity mix changed across coal, gas, hydro, nuclear, solar and wind?
- Which country candidates have high or low energy consumption, renewable electricity shares and carbon intensity?
- Is renewable electricity share associated with electricity carbon intensity?
- Are the conclusions sensitive to year selection, missingness and extreme observations?

## Analytical standards

- I preserve the original CSV and do not impute missing values by default.
- I separate the `World` aggregate from country-level comparisons.
- ISO-code presence is treated as a country-candidate filter, not proof of sovereign status.
- I report valid sample sizes, periods and explicit selection rules.
- I distinguish energy from electricity and absolute quantities from per-capita measures and shares.
- I treat unusual values as investigation flags rather than automatically deleting them.
- Correlation is not described as causation.
- Each major code section is followed by an interpretation and limitations note.

## Libraries

NumPy, pandas, Matplotlib, Seaborn and SciPy. Python's standard library is used for file and path handling.

## Data provenance and licensing

The supplied CSV is included for reproducibility in this working package. Before publishing or redistributing the dataset, verify the current Our World in Data energy dataset license and attribution requirements, and follow the source's preferred download instructions. See [`data/README.md`](data/README.md).

## Limitations

This is an observational EDA project. Coverage varies across variables, entities and time. Country-year rows are repeated observations, source categories can overlap, and national differences may reflect many unobserved factors. Results are descriptive and should not be used as standalone investment or policy recommendations.

## Project status

The notebooks have been authored and executed in the build environment. Re-run them locally before publication to confirm environment compatibility and regenerate outputs from the included CSV.
