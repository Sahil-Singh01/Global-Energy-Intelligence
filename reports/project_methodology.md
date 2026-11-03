# Project Methodology and Analytical Decisions

## 1. Workflow

The notebooks are designed to be read in order:

1. `01_data_audit_and_preparation.ipynb` — file integrity, schema, missingness, entity coverage and quality flags.
2. `02_descriptive_and_distributional_analysis.ipynb` — descriptive statistics, distribution shape and coverage.
3. `03_global_energy_trends.ipynb` — global time series, source trends and endpoint changes.
4. `04_country_benchmarking_and_energy_mix.ipynb` — country-candidate selection, indicator coverage, rankings and multi-year averages.
5. `05_statistical_analysis_and_robustness.ipynb` — correlation, bootstrap interval, influence sensitivity and growth-period comparisons.

Each major code block is followed by a conclusion cell. Those conclusion cells state what the displayed output means, how it should be interpreted, and what it cannot establish.

## 2. Raw data preservation

The notebooks load the CSV into `raw` and create `df = raw.copy()`. No blanket imputation or automatic row deletion is performed. Outputs are written to `outputs/tables/` and `outputs/figures/`.

## 3. Entity handling

- Global time-series analysis uses the `World` row where the indicator is present.
- Country benchmarking excludes `World` and uses a non-null `iso_code` as a country-candidate signal.
- ISO presence is not treated as definitive proof of sovereign-country status.
- Aggregates are never added to their constituent country totals.

## 4. Missing data

Missing values remain missing unless an explicitly documented analysis-specific filter requires a complete case. Each table or test should report its own valid sample size. Missing is not interpreted as zero.

## 5. Time coverage

The file's latest year is not assumed to be complete. Recent-year coverage is inspected for each indicator. Country benchmarks use the latest year with at least 30 valid country-candidate observations per indicator. This threshold is a project convention and should be tested if the rankings are used for consequential decisions.

## 6. Growth

Absolute changes are reported alongside percentage changes. CAGR is calculated only for positive start and end values over a positive year span. Extreme annual growth rates are investigated rather than automatically removed.

## 7. Statistics

- Pearson correlation measures linear association.
- Spearman correlation measures monotonic rank association.
- The renewable-share/carbon-intensity test uses a single-year cross-section of complete country-candidate cases.
- A bootstrap interval is computed using a fixed random seed.
- A sensitivity check excludes the outer 1% tails on both variables, while retaining the full sample as primary.
- The test is observational and does not establish causality.

## 8. Visual standards

Plots use clear titles, units, axis labels and a restrained style. Logarithmic transforms are used only to visualize positive, highly skewed scale variables; they do not alter the underlying data.

## 9. Reproducibility

Install `requirements.txt`, open Jupyter from the repository root, and run notebooks in numeric order. Tables and figures are generated under `outputs/`. The code uses only NumPy, pandas, Matplotlib, Seaborn, SciPy and the Python standard library.

## 10. Publication checklist

- Verify variable definitions and units against source documentation.
- Review every chart and its conclusion.
- Confirm that table samples match the narrative.
- Re-run notebooks from a clean environment.
- Check the current dataset license and attribution requirements before redistributing the raw CSV.
