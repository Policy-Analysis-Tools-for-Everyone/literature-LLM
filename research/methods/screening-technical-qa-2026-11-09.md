# Scopus A–D screening technical QA — 9 November 2026

**Status:** deterministic file/provenance QA completed; **human exclusion adjudication remains open**. This is a *critical narrative literature review with documented searching*, not a systematic review. No source exclusions or original records were overwritten.

## Independent deterministic checks

| Check | Result |
|---|---|
| Original Search A export | 362 rows |
| Original Search B export | 323 rows |
| Original Search C export | 140 rows |
| Original Search D export | 271 rows |
| Combined original exports | 1096 hits |
| Duplicate hits, DOI then Unicode-normalised title | 78 ({'A': 1, 'B': 27, 'C': 34, 'D': 16}) |
| Unique identified papers | **1018** — matches combined master **1018** |
| D duplicate audit | 16 entries — matches independently reproduced 16 |
| Distinct D additions in master | 255 |
| Repeat DOI keys within deduplicated master | 0 |
| Empty/unusable abstracts | 5 (SC-0702, SC-0708, SD-0082, SD-0109, SD-0250) |
| A–C initial AI-proposed exclusions | 277 — still subject to original v0.5 QA |
| D AI-proposed exclusions | 132 |
| Total A–C plus D proposed exclusion sets | **409** — NOT human-validated |
| Recorded protected researcher decisions in A–C | 21 |
| FinalHumanValidated in combined master | **0 explicit Yes**; statuses {'No — AI-assisted population triage; prior individual researcher decisions preserved': 763, 'No': 255} |
| Existing D exclusion QA sample | 25; all marked "Human check required" in source file |

## Why the screening cannot be certified as final yet

- The existing A–C random exclusion check previously flagged **ten potentially mistaken exclusions in a thirty-record sample**. This is a serious sensitivity warning, not a statistically stable miss-rate estimate.
- A subsequent A–C AI-only pass examined all 277 proposed exclusions and retained many provisionally, but **that is not an independent human review**.
- The D 25-record QA sample has **AuditStatus = Human check required** for all records; two additional D papers (SD-0083 and SD-0128) were previously recognised as contextual leads by AI and are not treated as direct empirical inclusions.
- Neither the original human-protected judgements nor any earlier AI screening labels were changed by this check.
- The number 1,018 describes **identified unique records**, not final studies included; it does not imply all were independently screened.

## Targeted human adjudication queue

Created a bibliographic-only **52-record** queue (no bulk abstract text) at `screening-qa-researcher-queue-2026-11-09.csv`. It includes {'High-priority adjudication': 7, 'Abstract retrieval': 5, 'Pre-existing random QA sample': 25, 'Additional random sample': 15}. The queue is **a decision aid, not a new exclusion result**.

The highest-priority first cases are SC-0057 (professional educator study), SC-0451 (postgraduate quasi-experiment), SC-0637 (MSc case), two unclear-population records, five missing-abstract records and the already upgraded D method leads. Three A–C studies are currently proposed as potential false-exclusion rescues; no automatic changes have been made.

## Data and method provenance

| Input | SHA-256 |
|---|---|
| `Search-A.csv` | `a55142aa02a469bae50e60d230e5226d0673b09ee4588006e3febd0379d6f536` |
| `Search-B.csv` | `ce25366e7f14ba1575fad1461e880e15f875abada382f9303a7de4b443362db0` |
| `Search-C.csv` | `d7b628db646f353e7ecfcc6962a6c47cc165ebaa4a17f10c4ad29a809c2b8cf9` |
| `Search-D.csv` | `5a306cd897c36fa3b8d61125c970304383ce60708a1e1df6838851fa6737ae78` |
| `PolicyMemo-Scopus-combined-1018-v0.6-2026-11-09.csv` | `bed39db924fe5878ce5784cea23ff1b620779a691b0ef51dbc18872d2162e308` |
| `PolicyMemo-exclusion-audit-all-277-v0.5-2026-11-09.csv` | `64fa6a6ebefa097904f63b035b09e787e72c685cd49097d0889df91219d3829a` |
| `PolicyMemo-Search-D-exclusion-QA25-v0.6-2026-11-09.csv` | `60378999bc2f2b0e37764d28cbb629b844ed60a5748ef543e1bb99f8f70f3c0b` |
| `PolicyMemo-Search-D-duplicate-audit-2026-11-09.csv` | `bb30cb2a92c6be06cf06e6c9a930bfa56600f8d9cd842f0b7c876a10a6b65234` |

## Next step

1. Researcher (or human colleague) inspects first the higher-risk cases, recording **retain / contextual / direct candidate / unresolvable**, rationale and whether a full text is needed.
2. Review the pre-existing D sample and additional A–C random sample blind to the first AI decision wherever practical. **Do not treat a second AI pass as human double screening.**
3. Preserve all changes in append-only decision rows; recompute verified selection outcomes only once actual human decisions exist.
4. Since the objective is a design-informed **critical narrative review**, begin theory/methodology synthesis now while keeping the final screening audit as an open limitation. There is no justified fixed target for number of included papers.