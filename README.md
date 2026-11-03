# Global Energy Intelligence
### A narrative-led exploratory analysis of global energy systems

[![Notebook validation](https://github.com/Sahil-Singh01/Global-Energy-Intelligence/actions/workflows/validate-notebooks.yml/badge.svg)](https://github.com/Sahil-Singh01/Global-Energy-Intelligence/actions/workflows/validate-notebooks.yml)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Analysis](https://img.shields.io/badge/Focus-Exploratory%20Data%20Analysis-147D64)
![Notebooks](https://img.shields.io/badge/Jupyter-5%20notebooks-F37626?logo=jupyter&logoColor=white)

An end-to-end Python EDA project exploring historical energy consumption, electricity generation, energy-source composition, renewable adoption, country-level differences, and electricity carbon intensity using the Our World in Data (OWID) Energy dataset.

The project is designed as an analyst's investigation rather than a collection of disconnected charts: each notebook introduces a question, explains the method, presents the analysis, and follows important code sections with a plain-English conclusion and limitations.

---

## At a glance

| Dataset characteristic | Value |
|---|---:|
| Observations | **19,494** |
| Variables | **130** |
| Entity labels | **260** |
| Recorded year range | **1700–2025** |
| Missing cells | **61.17%** |
| Duplicate entity–year keys | **0** |
| Main analysis notebooks | **5** |

The high overall missingness is an important analytical constraint. The project therefore uses indicator-specific samples and reports coverage rather than applying blanket imputation or dropping every incomplete row.

## Selected analysis

### Data quality and coverage

![Missingness by variable](outputs/figures/01_top_variable_missingness.png)

The audit establishes the schema, missingness profile, entity coverage, year coverage, duplicate checks, and screening flags. Missing values are not automatically treated as zero, and unusual values are investigated rather than silently deleted.

### Global energy and electricity trends

![Global energy and electricity trends](outputs/figures/05_world_energy_and_electricity_trends.png)

Global time-series analysis uses the OWID `World` aggregate where the indicator is available. Total energy and electricity generation are treated as distinct measures; aggregate records are not added to country observations.

### Electricity generation by source

![Electricity generation by source](outputs/figures/06_world_electricity_sources.png)

The source-level view compares generation from selected sources in TWh. Absolute generation and percentage shares are interpreted separately.

### Renewable electricity and carbon intensity

![Renewable electricity share and carbon intensity](outputs/figures/07_renewables_vs_carbon_intensity.png)

In the **2024 cross-section**, the complete-case sample contains **195 country-candidate observations**:

| Statistic | Result |
|---|---:|
| Pearson correlation | **−0.877** |
| Spearman rank correlation | **−0.894** |
| Pearson p-value | **2.45 × 10⁻⁶³** |
| Bootstrap 95% interval for Pearson r | **[−0.917, −0.836]** |

This is a strong negative association in the selected sample: observations with higher renewable electricity shares tend to have lower electricity carbon intensity. It is **not a causal estimate**. The analysis does not isolate the effects of nuclear generation, fuel mix, imports, geography, or other potential confounders. See the statistical notebook and report for the full design and sensitivity check.

---

## Research questions

1. How have global energy consumption and electricity generation changed over time?
2. How has the global electricity mix evolved across coal, gas, hydro, nuclear, solar, and wind?
3. How do country candidates compare on absolute energy use, per-capita use, renewable electricity share, and carbon intensity?
4. Is renewable electricity share associated with electricity carbon intensity in a cross-section?
5. How sensitive are the findings to reporting coverage, year selection, and extreme observations?

## Notebook guide

Run the notebooks in numerical order from the repository root.

| Notebook | Focus | Main deliverables |
|---|---|---|
| [01 — Data Audit and Preparation](notebooks/01_data_audit_and_preparation.ipynb) | Schema, integrity, missingness, entity and year coverage, quality flags | Data dictionary and audit tables |
| [02 — Descriptive and Distributional Analysis](notebooks/02_descriptive_and_distributional_analysis.ipynb) | Summary statistics, distributions, skewness, boxplots, coverage | Descriptive tables and distribution charts |
| [03 — Global Energy Trends](notebooks/03_global_energy_trends.ipynb) | World energy and electricity trends, source mix, endpoint changes and CAGR | Global trend tables and figures |
| [04 — Country Benchmarking and Energy Mix](notebooks/04_country_benchmarking_and_energy_mix.ipynb) | Indicator-specific coverage, country-candidate rankings, multi-year averages | Benchmark and coverage tables |
| [05 — Statistical Analysis and Robustness](notebooks/05_statistical_analysis_and_robustness.ipynb) | Pearson/Spearman correlation, bootstrap interval, sensitivity analysis | Statistical results and relationship chart |

**Notebook reading convention:** research question → analytical approach → code and output → conclusion and limitations.

## Repository structure

```text
Global-Energy-Intelligence/
├── data/
│   ├── owid_energy.csv
│   └── README.md
├── notebooks/
│   ├── 01_data_audit_and_preparation.ipynb
│   ├── 02_descriptive_and_distributional_analysis.ipynb
│   ├── 03_global_energy_trends.ipynb
│   ├── 04_country_benchmarking_and_energy_mix.ipynb
│   └── 05_statistical_analysis_and_robustness.ipynb
├── outputs/
│   ├── figures/                 # Saved analysis charts
│   └── tables/                  # Reproducible CSV outputs
├── reports/
│   ├── executive_summary.md
│   ├── project_methodology.md
│   ├── data_quality_report.md
│   ├── statistical_findings.md
│   └── data_dictionary.csv
├── src/
│   ├── analysis_helpers.py
│   ├── data_quality.py
│   └── visualization_helpers.py
├── .github/workflows/           # Notebook syntax validation
├── requirements.txt
└── README.md
```

## Run locally

**Requirements:** Python 3.10 or later.

```bash
# Clone the repository
git clone https://github.com/Sahil-Singh01/Global-Energy-Intelligence.git
cd Global-Energy-Intelligence

# Create and activate a virtual environment
python -m venv .venv

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate

# Install dependencies
python -m pip install -r requirements.txt

# Launch Jupyter
jupyter lab
```

Open the notebooks in `notebooks/` and execute them in numerical order. Run Jupyter from the repository root so the relative data and output paths resolve correctly. Generated tables and charts are written to `outputs/`.

## Analytical decisions

- **Preserve the source:** the raw CSV is loaded without blanket imputation or automatic row deletion.
- **Separate aggregates:** the `World` aggregate is used for global trends and excluded from country comparisons.
- **Use careful entity language:** a non-null ISO code is a practical country-candidate filter, not proof of sovereign-state status.
- **Respect indicator coverage:** each analysis selects the fields it needs and reports its valid sample size and time period.
- **Keep measures distinct:** total energy, electricity generation, per-capita measures, intensity, and shares answer different questions.
- **Investigate unusual values:** screening flags prompt review; they are not automatic deletion rules.
- **Avoid causal overstatement:** correlations and descriptive comparisons do not establish cause and effect.

Detailed decisions are documented in [Project Methodology](reports/project_methodology.md).

## Data provenance and attribution

The analysis uses the OWID Energy dataset. The dataset catalog describes a country-year table compiled from sources including the Energy Institute's Statistical Review of World Energy, Ember, the U.S. Energy Information Administration, OWID population data, and the Maddison Project Database.

- [OWID Energy dataset catalog and documentation](https://catalog.ourworldindata.org/energy/owid_energy/)
- [OWID energy-data repository and source documentation](https://github.com/owid/energy-data)
- [OWID guidance on data reuse and attribution](https://ourworldindata.org/faqs#how-should-i-cite-your-data)

The dataset is a compilation of third-party sources. **Do not assume that every underlying data point is covered by one blanket license.** Check the original provider's terms and cite OWID and the relevant underlying providers when reusing or redistributing data. The included CSV is the snapshot used for this analysis; it should not be assumed to be the latest release.

## Project documentation

- [Executive summary](reports/executive_summary.md)
- [Data-quality report](reports/data_quality_report.md)
- [Statistical findings](reports/statistical_findings.md)
- [Project methodology](reports/project_methodology.md)
- [Data dictionary](reports/data_dictionary.csv)
- [Output inventory](outputs/README.md)
- [Complete file index](FILE_INDEX.md)

## Limitations

This is an observational EDA project. Reporting coverage varies across entities, indicators, and years. Entity labels include aggregates and source-specific regions. Indicator definitions and units should be checked against the source codebook before high-stakes interpretation. Cross-country associations may reflect confounding factors, and the statistical analysis does not identify causal effects.

---

**Author:** [Sahil Singh](https://github.com/Sahil-Singh01)  
**Repository:** [Sahil-Singh01/Global-Energy-Intelligence](https://github.com/Sahil-Singh01/Global-Energy-Intelligence)
