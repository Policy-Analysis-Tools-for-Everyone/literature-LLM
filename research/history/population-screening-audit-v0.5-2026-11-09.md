# PolicyMemo.ai — screening and exclusion audit v0.5

**Date:** 9 November 2026  
**Scope:** postgraduate learners and practising professionals, with separate theory/framework lane.  
**Status:** AI-assisted title/abstract triage; researcher decisions preserved, not final independently validated exclusions.

## Identification and sample ledger

- Scopus Search A: 362 results; B: 323; C: 140.
- Total records returned: **825** (not unique).
- Duplicates removed: **62**.
- Unique records: **763**. Former screen v0.2 (provisional): 196 core / 259 contextual / 31 uncertain / **277 exclusions**.
- Twenty-one previous researcher decisions maintained in original, traceable columns.
- Full population source-audit of all 763, and targeted reassessment of all 277 prior AI-only exclusion labels, including crosswalk to the original 96-case quality review.

## New focused reading lanes

| Lane | Count | Action |
|---|---:|---|
| Clearly postgraduate/professional | **29** | Seek full text |
| Population unresolved | **19** | Verify actual postgraduate/professional participants |
| Theory and reviews | **8** | Read selectively |
| Undergraduate-derived leads | **2** | Conceptual/framework only, not empirical generalisation |
| Undergraduate-only removed | **10** | Preserve excluded records/history |

This yields **58 active potential readings** in distinct lanes, not fifty-eight eligible studies or a commitment to read them all.

### Three recovered papers

1. **SC-0451** — graduate students, quasi-experimental design (35), cognitive-depth assessment. Examine how learning was assessed rather than equating scores with judgement.
2. **SC-0057** — twelve maritime instructors/policy specialists, division of labour and feedback using Cultural-Historical Activity Theory, potentially fruitful for the *practice* framing.
3. **SC-0637** — MSc Marketing group case work with ChatGPT; focus group; practice evidence but no causal learning estimate.

### Preserved intellectual leads

- SC-0092 — undergraduate co-created custom GPTs: strategy-as-practice **lead**, not evidence this paper uses formal strategy-as-practice theory.
- SC-0407 — undergraduate human–AI feedback model: assess framework only.
- SC-0578 — university students not identified as postgraduates in abstract; remain contingent pending source check.
- SC-0175 — Casey's public-policy brief study used undergraduates; previously appraised, now **historical comparator only**, not direct target-population evidence.

## Method

- Added v0.5 population assessment fields and excerpts to all 763 records, preserving prior labels and adjudications.
- Population categories include confirmed-from-abstract PG/professional, probable undergraduate-only, teacher pre-service level uncertain, mixed, non-empirical, and unspecified; unknown was **not turned into exclusion**.
- Reviewed the ninety-six-record previous audit queue and cross-referenced the entire set of 277 AI exclusions. Recorded source cues and recommendations per record. These are evidence triage judgments and priority signals, **not independently validated title/abstract decisions**.
- Kept two no-abstract records flagged (SC-0702, SC-0708), and did not make conference venue a reason for exclusion.
- Screened potential relevance separately from methodological strength (e.g. interviews about attitudes can be relevant as perspectives without proving learning).
- Earlier pilot audit recorded ten possible false exclusions among thirty checked, meaning residual false exclusions are a material risk. Do not freeze 277 as final PRISMA exclusions until genuinely independent validation has occurred. Even the records here labelled *retain exclusion* remain provisional.

## Further validation required before a formal PRISMA screening count

1. Have a researcher or independent reviewer examine and adjudicate prior provisional exclusions without relying uncritically on AI suggestions.
2. Resolve population status for nineteen shortlisted cases, plus any other abstract-uncertain cases that become relevant.
3. Document full-text retrieval and population verification, then final inclusion/exclusion with reasons and reviewer identifiers.
4. Export a frozen final screening version (separate from this provisional register) and only then populate the PRISMA screening/full-text branches.

## File provenance

Primary input: `PolicyMemo-Scopus-full-register-with-researcher-decisions-2026-11-09.csv`  
SHA-256: `2389763f1690aba8482b59a2784a0357f829ee224a14406154a39cc9fd91fd0f`.

New working files:

- `PolicyMemo-Scopus-population-and-exclusion-register-v0.5-2026-11-09.csv`
- `PolicyMemo-exclusion-audit-all-277-v0.5-2026-11-09.csv`
- `PolicyMemo-exclusion-audit-prior-96-v0.5-2026-11-09.csv`
- `PolicyMemo-reading-queue-v0.5-2026-11-09.csv`
- `PolicyMemo-active-reading-58-v0.5-2026-11-09.csv`
- `PolicyMemo-evidence-synthesis-cycle7-2026-11-09.md`

The analytical script `policymemo_v05_audit.py` accompanies the handover and records source-cue rules and targeted overrides. It is a triage aid, not a systematic-review screening engine.