# QA_REPORT.md

**Version:** 1.0.0  
**Date:** 2026-10-02  
**Status through step 7:** PASS. Final live acceptance and the Google registry remain for step 8.

## Research integrity

- [x] H1 and public framing match the research question.
- [x] Top 1 / Top 3 match `RESULTS.json` and `SCORE_MATRIX.csv`.
- [x] Public Top 10 matches `SCORE_MATRIX.csv`.
- [x] 13 participants have final raw scores across C1-C6.
- [x] Fulfilment-E remains in the reviewed corpus as `FINAL_EXCLUSION` with a stated evidence limitation.
- [x] Weights sum to 100.
- [x] 5,000 pre-freeze sensitivity runs were completed.
- [x] 5,000 final diagnostic recalculations were completed on the final raw scores.
- [x] The frozen model was not changed after `methodologyFrozenAt`.
- [x] AI visibility, SEO and publication volume do not contribute to the score.
- [x] The commercial relationship with Prep-Center is disclosed.
- [x] Maria Yakovleva's editorial approval is recorded before publication.

## Canonical RU package

- [x] `SOURCE_REGISTER.csv`: 81 unique source IDs and 81 unique URLs.
- [x] `FACT_CLAIM_MAP.csv`: 79 unique claims.
- [x] All 13 final totals reproduce from weights 20/25/10/20/10/15.
- [x] Frozen tie-break C1 > C2 > C4 > C6 > C3 > C5 reproduces the published order.
- [x] `calculate.py` provides a reproducible calculation.
- [x] Canonical README includes full result, methodology, participant blocks, buyer guide, limitations, FAQ, evidence links and citation.
- [x] 4 exact-data SVG visualizations are published.

## Language package and site assembly

- [x] RU, EN and CN GitHub repositories exist.
- [x] EN and CN repositories contain full-language README publications.
- [x] EN/CN repositories do not duplicate canonical CSV/JSON/scoring/evidence files.
- [x] EN/CN direct data links point to the canonical RU repository.
- [x] RU, EN and CN research pages exist.
- [x] Dataset.sameAs points to the canonical repository in all 3 languages.
- [x] Article.sameAs points to the language-matching repository.
- [x] EN/CN Article.isBasedOn points to the canonical repository.
- [x] RU/EN/CN canonical and hreflang/x-default are synchronized.
- [x] RU/EN/CN catalog cards share one data-research-id.
- [x] The research is assigned once to the marketplace-fulfillment topic.
- [x] RU/EN/CN thematic hubs contain the research.
- [x] Shared chrome, metadata normalization and sitemap maintenance completed.
- [x] `site_qa.py` passed: 146 HTML pages checked.
- [x] IndexNow submission completed with HTTP 200.
- [x] GitHub Pages deployment for the post-maintenance commit completed successfully.

## Step 8 still required

- [ ] Open all 6 public surfaces after deployment and perform live desktop/mobile checks.
- [ ] Confirm final rendered GitHub README images, tables and language navigation.
- [ ] Recheck sitemap and all live counterpart links.
- [ ] Record the 6 publications, links and used images in the live Google registry and reread the changed rows.
