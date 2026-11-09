# PolicyMemo.ai — Scopus pilot search audit

**Record created:** 8 November 2026
**Status:** researcher-reported search counts; raw Scopus exports awaited. Do not treat dates, filters, or exact strings as independently verified against Scopus export/search history until checked.
**Purpose:** preserve a reproducible pilot search trail for a focused critical narrative literature review and possible PRISMA-style reporting. Not a claim that a systematic review has been performed.

## Search identification baseline

| Source | Search strand | Search hits before deduplication |
|---|---|---:|
| Scopus | A — AI, judgement and learning | 362 |
| Scopus | B — AI scaffolding and reasoning | 323 |
| Scopus | C — AI and professional practice | 140 |
| **Scopus (3 search runs)** | **Combined hits (not unique records)** | **825** |

Numbers reported by the researcher on 8 November 2026. Overlap and duplication between queries are currently unknown. Distinguish database search runs (3) from databases searched (1: Scopus). Confirm final export record counts and actual date/time of the search using Scopus search history or export metadata.

## Searches used (as specified in the conversation)

### Search A — AI, judgement and learning

```text
TITLE-ABS-KEY(
  ("generative AI" OR "ChatGPT" OR "large language model*")
  AND
  ("evaluative judgement" OR "evaluative judgment"
   OR "reflective practice" OR "professional judgement"
   OR "professional judgment")
  AND
  (learning OR education OR teaching OR training)
)
AND PUBYEAR > 2019
AND PUBYEAR < 2027
```

### Search B — AI as scaffolding for reasoning

```text
TITLE-ABS-KEY(
  ("generative AI" OR "ChatGPT" OR "large language model*")
  AND
  ("scaffolding" OR "feedback" OR "critique")
  AND
  ("critical thinking" OR "reasoning" OR "reflection")
  AND
  ("higher education" OR "postgraduate"
   OR "professional learning")
)
AND PUBYEAR > 2019
AND PUBYEAR < 2027
```

### Search C — AI and professional practice

```text
TITLE-ABS-KEY(
  ("generative AI" OR "ChatGPT" OR "large language model*")
  AND
  ("knowledge workers" OR "professional practice"
   OR "professional learning")
  AND
  (reasoning OR judgement OR judgment OR reflection)
)
AND PUBYEAR > 2019
AND PUBYEAR < 2027
```

## Pending export confirmation

- [ ] Retain unmodified separate `Scopus-A.csv`, `Scopus-B.csv`, `Scopus-C.csv` files; capture any export restriction and count mismatch.
- [ ] Verify the search date/time, precise Scopus query strings, filters, and document/language/source-type constraints (if any).
- [ ] Preserve bibliographic identifiers (DOI, Scopus EID), titles, authors, year, source, abstracts, keywords, and record URLs where available.
- [ ] Compute imported records by export and compare against 362/323/140.
- [ ] Deduplicate by DOI/EID, then normalised title and bibliographic review, logging ambiguous decisions.
- [ ] Record unique records, duplicates removed, records screened and excluded (with reasons as appropriate), full texts sought, unavailable, assessed, excluded with reasons and included.
- [ ] Record separately any additional studies identified through citation-following or targeted web searches, without mislabelling them as Scopus search results.

## Scope and project continuity

The review examines how generative AI shapes adult learners' and practitioners' development, exercise and justification of judgement in complex work. The research focuses on reflective practice, critique, feedback, scaffolding, delegation, and distinctions between AI-assisted performance and learning. Broad investigations of AI credibility and error detection alone are outside the current priority scope. D3 and D4 were deprioritised. Existing appraisals and decisions remain in the living evidence synthesis and screening log.

**Next:** import the three Scopus exports, verify the search audit, deduplicate and pilot-screen. This is the natural point to decide whether to hand the primary research workflow to Claude. This audit is platform-independent and should accompany any handover.