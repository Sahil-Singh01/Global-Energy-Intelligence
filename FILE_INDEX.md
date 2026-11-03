# Project File Index

This inventory lists the tracked project files on the `main` branch. File sizes are approximate.

| Path | Size |
|---|---:|
| `.github/workflows/validate-notebooks.yml` | 1.4 KB |
| `.gitignore` | 71 B |
| `README.md` | 9.9 KB |
| `FILE_INDEX.md` | This file |
| `project_manifest.json` | 1.4 KB |
| `requirements.txt` | 112 B |
| `data/README.md` | 1.8 KB |
| `data/owid_energy.csv` | 8.66 MB |
| `notebooks/01_data_audit_and_preparation.ipynb` | 245.2 KB |
| `notebooks/02_descriptive_and_distributional_analysis.ipynb` | 197.0 KB |
| `notebooks/03_global_energy_trends.ipynb` | 241.2 KB |
| `notebooks/04_country_benchmarking_and_energy_mix.ipynb` | 40.7 KB |
| `notebooks/05_statistical_analysis_and_robustness.ipynb` | 121.1 KB |
| `outputs/README.md` | 431 B |
| `outputs/figures/01_top_variable_missingness.png` | 179.4 KB |
| `outputs/figures/02_missingness_by_year.png` | 56.1 KB |
| `outputs/figures/03_scale_variable_distributions.png` | 165.2 KB |
| `outputs/figures/04_per_capita_intensity_and_share_boxplots.png` | 52.8 KB |
| `outputs/figures/05_world_energy_and_electricity_trends.png` | 148.5 KB |
| `outputs/figures/06_world_electricity_sources.png` | 123.4 KB |
| `outputs/figures/07_renewables_vs_carbon_intensity.png` | 147.3 KB |
| `outputs/tables/audit_overview.csv` | 259 B |
| `outputs/tables/correlation_sensitivity.csv` | 127 B |
| `outputs/tables/country_benchmark_coverage_recent.csv` | 4.8 KB |
| `outputs/tables/country_multi_year_averages.csv` | 171.9 KB |
| `outputs/tables/country_top10_benchmarks.csv` | 6.2 KB |
| `outputs/tables/data_dictionary.csv` | 10.9 KB |
| `outputs/tables/data_quality_flags.csv` | 4.6 KB |
| `outputs/tables/descriptive_statistics.csv` | 2.1 KB |
| `outputs/tables/entity_coverage.csv` | 9.1 KB |
| `outputs/tables/indicator_coverage.csv` | 378 B |
| `outputs/tables/missingness_by_column.csv` | 5.4 KB |
| `outputs/tables/missingness_by_year.csv` | 7.3 KB |
| `outputs/tables/records_by_year.csv` | 4.1 KB |
| `outputs/tables/renewable_generation_growth_periods.csv` | 460 B |
| `outputs/tables/renewables_carbon_intensity_test.csv` | 248 B |
| `outputs/tables/world_trend_endpoint_changes.csv` | 1.1 KB |
| `outputs/tables/world_trends.csv` | 9.4 KB |
| `reports/README.md` | 946 B |
| `reports/data_dictionary.csv` | 10.9 KB |
| `reports/data_quality_report.md` | 1.7 KB |
| `reports/executive_summary.md` | 3.3 KB |
| `reports/project_methodology.md` | 3.5 KB |
| `reports/statistical_findings.md` | 1.5 KB |
| `src/analysis_helpers.py` | 879 B |
| `src/data_quality.py` | 1.4 KB |
| `src/visualization_helpers.py` | 790 B |

## Notes

- The five notebooks contain executed outputs and were checked for stored execution errors in the build environment.
- The GitHub Actions workflow validates notebook structure and Python syntax on pushes and pull requests; it does not execute the notebooks.
- The raw energy dataset combines sources with potentially different licensing terms. See [data documentation](data/README.md).
