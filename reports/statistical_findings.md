# Statistical Findings

## Research question

Is renewable electricity share associated with electricity carbon intensity in a single-year cross-section?

## Design

- Year: 2024
- Observational unit: country-candidate entity
- Inclusion: non-null ISO code, not `World`, and complete values for both indicators
- Sample size: 195
- Significance threshold: α = 0.05

## Results

| Statistic | Result |
|---|---:|
| Pearson r | -0.8770 |
| Pearson p-value | 2.455e-63 |
| Spearman ρ | -0.8937 |
| Spearman p-value | 4.115e-69 |
| Bootstrap 95% interval for Pearson r | [-0.9171, -0.8355] |

## Interpretation

The observed association is strongly negative in the selected sample. Both linear correlation and rank correlation indicate that higher renewable electricity shares tend to occur alongside lower electricity carbon intensity.

This result does **not** establish causation. The analysis does not control for nuclear generation, fuel mix, electricity imports, geography, economic structure or other potential confounders. It is a cross-sectional comparison, not a within-country causal analysis.

## Robustness

The notebook compares the full complete-case sample with a sensitivity sample that excludes the outer 1% tails of both variables. The full-sample result remains primary; the trimmed result is a diagnostic and should not be used to selectively remove inconvenient observations.

## Reproduction

Run `05_statistical_analysis_and_robustness.ipynb`. The result table is saved as `outputs/tables/renewables_carbon_intensity_test.csv`.
