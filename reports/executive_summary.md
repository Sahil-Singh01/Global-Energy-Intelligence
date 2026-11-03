# Executive Summary

## Project purpose

I analyzed the supplied Our World in Data energy CSV to understand historical global energy use, electricity generation, source mix, country-level differences, and the association between renewable electricity share and electricity carbon intensity.

## Dataset overview

- **Rows:** 19,494
- **Columns:** 130
- **Entity labels:** 260
- **Recorded years:** 1700–2025 (326 distinct years)
- **Missing cells:** 1,550,291 (61.17%)
- **Exact duplicate rows:** 0
- **Duplicate country–year keys:** 0

The file has broad historical scope, but missingness is substantial and differs across variables. I therefore use indicator-specific samples instead of dropping every row with any missing value.

## Main analytical observations

1. **Data coverage must shape the question.** The overall missing-cell rate is 61.17%, so country rankings and statistical tests need their own valid sample counts and coverage rules.
2. **Global and country-level analysis require separate samples.** I use the `World` row for global time-series questions when the indicator is available and exclude it from country rankings to avoid double counting.
3. **Energy and electricity are distinct.** The notebooks analyze total energy consumption separately from electricity generation and generation by source.
4. **Absolute and normalized indicators answer different questions.** Total consumption reflects system scale; per-capita energy, energy intensity and source shares provide complementary perspectives.
5. **Growth rates require care.** Percentage changes can become extreme when the baseline is very small or zero. I inspect underlying levels and avoid treating every extreme growth value as an error.

## Statistical result: renewable electricity share and carbon intensity

For the **2024 cross-section**, the complete-case sample included **195 country-candidate observations** with both renewable electricity share and electricity carbon intensity available.

- Pearson correlation: **r = -0.877**
- Pearson p-value: **2.45e-63**
- Spearman rank correlation: **ρ = -0.894**
- Spearman p-value: **4.12e-69**
- Bootstrap 95% interval for Pearson r: **[-0.917, -0.836]**

The observed association is strongly negative in this sample: country candidates with higher renewable electricity shares tend to have lower electricity carbon intensity. This is an association, not a causal estimate. Nuclear generation, fossil-fuel mix, imports, geography and other factors may also matter.

## Limitations

- Variable definitions and units should be checked against the source documentation before publication.
- Some rows are aggregate or source-specific entities rather than individual countries.
- ISO-code presence is used as a practical country-candidate filter, not as a definitive sovereignty classification.
- Coverage changes across time and indicators.
- Correlations and trend comparisons do not establish policy effects or causation.
- Public redistribution of the raw CSV requires checking the source's current licensing terms.

## Conclusion

The dataset supports a broad, reproducible exploration of global energy systems. The most defensible narrative comes from combining coverage-aware global trends, transparent country benchmarks, and a small number of well-motivated statistical analyses. All conclusions should be presented with the sample, time period and limitations that support them.
