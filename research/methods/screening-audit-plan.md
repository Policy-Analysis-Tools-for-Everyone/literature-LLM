# Reconcile the existing AI-assisted screening — not a systematic-review claim

## Current identification ledger

| Search | Exported hits |
|---|---:|
| A | 362 |
| B | 323 |
| C | 140 |
| D (final version) | 271 |
| **Total** | **1,096** |

Duplicates: **62 across A–C**, **16 added when D was integrated**, **78 total**, **1,018 unique records**.

The preliminary broad D searches returning 1,189 and 474 results were exploratory **alternative queries**, not additional exported search cohorts. Fernandes was researcher-identified before Search D and is in the D export; do not silently add it a second time.

## Known incomplete stages

- A–C v0.2 initial full screening (763 unique records): **196 Core, 259 Contextual, 31 Uncertain, 277 Exclude (all provisional machine dispositions except named human decisions)**.
- A–C exclusion audit found **10 potential false exclusions in a random sample of 30**. Later population QA checked 277 but was still AI-assisted; unresolved exclusions are not verified negative decisions.
- D: **255 newly unique**, provisionally 12 core, 47 contextual, 61 verification, 3 no usable abstract, 132 exclusions; not a final selection flow.
- **Two A–C records** (SC-0702, SC-0708) have `[No abstract available]`. Three D records lacked usable abstracts. Recover source or log title-only status; do not call them screened from abstracts.
- Reading queues and 18 currently appraised PDFs are prioritisation artefacts; **not** all records at full-text eligibility stage.
- Original researcher adjudications and A–C/D source membership must remain preserved, not overwritten by model re-screening.

## Verification path

1. Freeze exact A–D exports and cumulative register in authorised archive; record hashes and collection dates.
2. Use *human reviewer* to inspect seeded ambiguous and previously excluded samples, preferably blind to initial AI decisions. A second model may suggest misses, but must be labelled AI-assisted and **not** counted as independent human screening.
3. Escalate any inconsistent population cues, mixed samples, no-abstract records, and false exclusions for human adjudication.
4. Keep an append-only decision ledger: `record_id, old, proposed_new, actor, decision_date, reason, source_access, final_human_decision`.
5. Recompute inclusion/exclusion and full-text sought figures **only** from verified dispositions. Preserve the previous counts as dated snapshots.
6. Report the review accurately as *critical narrative with documented searching and screening*; PRISMA-style identification is useful but does not by itself establish a PRISMA-compliant systematic review.

## Stop rule

Conclude supplementary searching when no *material* framework or study-design gap justifies more; record the decision. Do not impose an arbitrary quota of thirty or forty studies, or imply a complete systematic inclusion count based on the current priority queue.

## Technical QA run — 9 November 2026

[Deterministic A–D audit](screening-technical-qa-2026-11-09.md) reproduced **1,096 exports → 78 duplicate hits → 1,018 unique records**, checked master RecordIDs and DOI uniqueness, verified D's sixteen duplicates and identified five missing/unusable abstracts. Its [52-record bibliographic researcher queue](screening-qa-researcher-queue-2026-11-09.csv) combines seven targeted cases, five missing abstracts, the existing twenty-five D QA records and fifteen additional deterministically sampled A–C exclusions. **Technical provenance checks pass; adjudication does not.** The queue contains blanks for human decisions and deliberately preserves all original screening labels. Re-check independently as a human, and keep any AI recommendation advisory.
