# PolicyMemo.ai — Search D integration and provisional screening (v0.6)

**Date:** 9 November 2026. **Source:** user-supplied `Search-D.csv`, Scopus Advanced Search. **Status:** supplementary database search processed, title/abstract AI-assisted triage provisional, no full-text eligibility or human validation claimed. **Review:** focused critical narrative review; PRISMA-style identification bookkeeping may be used without calling the review systematic.

## 1. Search development and query

Three iterations were tested on 9 November 2026, only the final one exported:

| Iteration | Scopus reported results | Treatment |
|---|---:|---|
| Broad metacognition, self-monitoring and learning terms | 1,189 | Exploratory, not exported, not additive |
| Metacognition or self-assessment/calibration in title | 474 | Exploratory, not exported, not additive |
| Narrow metacognition or calibration in title | **271** | Final exported dataset, Search D |

```text
TITLE-ABS-KEY(
  "generative AI" OR
  "generative artificial intelligence" OR
  ChatGPT OR
  "large language model*"
)
AND
TITLE(
  metacognit* OR
  "confidence calibration" OR
  "performance calibration"
)
AND PUBYEAR > 2019
AND PUBYEAR < 2027
```

Search D deliberately prioritises records whose titles refer to metacognition or calibration. This improves focus but misses relevant papers under other language; citation-following remains necessary. The query also captures **technical studies of LLM self-calibration**, which must be distinguished from human metacognition.

## 2. Identification and deduplication

| Count | A–C originally | Search D addition | Combined |
|---|---:|---:|---:|
| Scopus search hits | 825 | 271 | **1,096** |
| Duplicate hits removed | 62 | 16 | **78** |
| Unique records | 763 | **255 new** | **1,018** |

Deduplication: compare normalised DOI and Unicode-/punctuation-normalised titles against the existing A–C register, then within Search D. **Fifteen D hits match earlier A–C records** (fourteen distinct original records; one was represented twice in D), and **one further duplicate pair is unique to D**. The duplicate audit records matching IDs and rule. A–C records retain their existing classifications and researcher decisions; the merged CSV adds Search D provenance without overwriting the historical decisions. All D records keep their original source-row number and new `SD-####` ID where applicable.

**Export integrity:** `Search-D.csv` includes 271 rows; 3 of the 255 new records have no usable abstract. Original CSV SHA-256: `5a306cd897c36fa3b8d61125c970304383ce60708a1e1df6838851fa6737ae78`.

## 3. Search D first-pass title/abstract screening

| Provisional lane | New unique D records |
|---|---:|
| Core: explicitly postgraduate or practising professional + relevant empirical activity | **12** |
| Contextual/theoretical/measurement lead | **47** |
| Postgraduate/professional population or relevance requires verification | **61** |
| Abstract retrieval required | **3** |
| Provisionally outside scope | **132** |
| **Total** | **255** |

This is **AI-assisted provisional screening, not researcher-approved final screening**. Exclusion categories include technical LLM-internal calibration, school/undergraduate-only empirical populations, and peripheral studies without a substantive analysis of human learning/judgement. The context lane is *not* a reading commitment. Source abstracts and individual reasons are retained for all records. No full papers were read during this Search D pass. A spot check of 25 proposed exclusions identified two more appropriate as contextual **methodological leads** (SD-0083 on annotation of team metacognition and SD-0128 on multimodal traces). Those corrections are reflected in the figures. This spot check was conducted by AI and is **not an independent human validation** of the exclusion pool.

### Core postgraduate / professional candidates

| ID | Title | Year | DOI | Priority |
|---|---|---:|---|---|
| SD-0006 | Cognitive offloading and metacognitive calibration in generative AI-mediated doctoral learning: a grounded theory study of accountable reconstruction | 2026 | 10.3389/fpsyg.2026.1920947 | A |
| SD-0017 | The VALUE of AI-Guided Communication: Enhancing Shared Decision-Making in Metabolic Bariatric Surgery Consultations Through a Metacognitive Framework | 2026 | 10.1007/s11695-026-08760-9 | B |
| SD-0018 | Exploring the Potential of Metacognitive Support Agents for Human-AI Co-Creation | 2025 | 10.1145/3715336.3735785 | A |
| SD-0036 | Leveraging generative AI to foster metacognition and self-directed learning | 2026 | 10.1128/jmbe.00153-25 | B |
| SD-0046 | Metacognitive regulation and ChatGPT-assisted writing: introducing an interactive model for cultivating strategic engagement | 2026 | 10.1007/s44217-026-01282-7 | A |
| SD-0086 | A Qualitative Inquiry Into Metacognitive Strategies of Postgraduate Students in Employing ChatGPT for English Academic Writing | 2025 | 10.1111/ejed.12824 | A |
| SD-0166 | Cognitive Outsourcing in Generative AI-Supported Learning: A Behavioural-Sequence Analysis of Metacognitive Differentiation | 2026 | 10.1177/21582440261497399 | A |
| SD-0186 | GenAI Tools in Academic Reading: A Study on AI-Assisted Metacognitive Strategies and Emotional Reactions | 2025 | 10.1007/978-981-96-4952-5_7 | B |
| SD-0203 | Exploring metacognitive regulation activities and their roles in prompt literacy development among humanities and social science researchers in GenAI | 2026 | 10.47989/ir31iConf64194 | A |
| SD-0222 | AI as Scaffold or Shortcut? Metacognitive Regulation in Graduate Students’ Educational App Design | 2026 | 10.3390/educsci16081198 | A |
| SD-0239 | Metacognitive strategy use in GenAI-supported academic reading: a qualitative study of postgraduate students in UK higher education | 2026 | 10.3389/fpsyg.2026.1787647 | A |
| SD-0242 | Unpacking the Impacts of GAI Use on Doctoral Students’ Metacognitive Experiences in Summary Writing: A Mixed Methods Study | 2026 | 10.1111/ijal.70267 | A | 

These are **potential core papers**, not appraised or necessarily high-quality studies. Qualitative single-site designs, training-plus-tool interventions, and observational claims should be assessed against the actual study design, measurement and claims. The distinction between **improved output, self-reported metacognition and demonstrated learning** remains essential.

### Important contextual candidates

- **SD-0201, Fernandes et al., *AI makes you smarter but none the wiser*** — previously researcher-supplied and correctly found in Search D. Two studies (N=246 and N=452) on AI-assisted reasoning and accuracy of self-assessment; mixed/general population, so *contextual* rather than directly postgraduate evidence. DOI: `10.1016/j.chb.2025.108779`.
- **SD-0114, *The Metacognitive Demands and Opportunities of Generative AI*** — conceptual human–AI metacognition, potentially useful for design implications and theorising interaction.
- **SD-0208, *The IDEA framework for metacognitively regulated GenAI use in higher education*** — examine the framework as a design lead; its cited pilot involves undergraduates and does not become eligible postgraduate empirical evidence.
- **SD-0189, *Developing self-regulation for generative AI through a metacognitive checklist*** — one practising teacher’s case. Useful as a practice/process illustration; not a population-level estimate.
- **SD-0217, *Metacognitive Processes in Generative AI-Supported Rapid Design Tasks*** — four graduate designers; process-oriented, but limited scale and transferability warrant caution.
- **SD-0238, *The Strategic Prompting Scale*** and **SD-0252, *Measuring human metacognition in GPT-assisted cognition*** — potential instrument and construct references; psychometric relevance does not imply evidence of change in judgement.

### Three records requiring abstract retrieval

- **SD-0082** — BOARD # 78: Student Use of ChatGPT and Claude in Introductory Engineering Education: Insights into Metacognition and Problem-Solving Patterns
- **SD-0109** — Metacognitive laziness and cognitive offloading in the era of generative AI: Risks and responsible use; [Pereza metacognitiva y descarga cognitiva en la era de la IA generativa: Riesgos y uso responsable]
- **SD-0250** — Assessing AI-Driven Metacognitive Offloading: Initial Development and Validation of the Metacognitive Laziness Scale

## 4. Implications for the review

Search D fills a genuine gap in the original strategy. Its strongest additions include studies of **doctoral research reasoning and accountable reconstruction**, **postgraduate academic writing/reading metacognitive strategies**, **professional designers using metacognitive support agents**, and **graduate students' cognitive outsourcing / regulation**. It also yields potentially useful null or counterintuitive findings; for example, SD-0242's abstract reports no overall group difference in metacognitive experiences, alongside lower task-specific metacognitive strategy reports among AI users. This is *an abstract claim to verify*, not a synthesised finding.

The original user restriction stands: undergraduate-only studies are **not direct empirical evidence**; theoretical frameworks or method leads may be evaluated as context. General AI credibility/model-confidence research remains out of scope, including papers where the *model itself*, rather than the human user, is the subject of calibration.

## 5. Recommended reading order

1. SD-0006 (doctoral grounded theory, artifacts and stimulated recall), SD-0086 (13 postgraduate writers, interviews and chat logs), SD-0222 (12 graduate students, multiple cases) — process and reasoning practices.
2. SD-0166 (90 graduate students, year-long behavioural sequences), SD-0242 (103 doctoral students, mixed methods including null finding), SD-0036 (graduate pre/post self-reports) — outcome-measurement and assisted versus independent capability.
3. SD-0018 (20 professional mechanical designers, agent support strategies), SD-0203 (17 humanities/social-science researchers), SD-0239 (12 UK postgraduate L2 readers) — professional comparison and UK context.
4. SD-0201 (Fernandes) as the targeted contextual comparison on performance/self-assessment mismatch.

No claim of methodological quality is made from abstracts alone. Retrieve full texts for the first batch before drafting claims from them. Keep the earlier exclusion audit open: a targeted Search D extension does not resolve it.

## 6. File map

- `PolicyMemo-Scopus-combined-1018-v0.6-2026-11-09.csv`: authoritative **combined provenance/screening register** (A–C decisions preserved; D appended).
- `PolicyMemo-Search-D-screened-255-v0.6-2026-11-09.csv`: new D records, full Scopus abstracts, provisional decisions and reasons.
- `PolicyMemo-Search-D-duplicate-audit-2026-11-09.csv`: 16 duplicate hits, matches and rules.
- `PolicyMemo-Search-D-reading-priorities-v0.6-2026-11-09.csv`: tighter reading shortlist, core and selected conceptual context.
- `PolicyMemo-Search-D-population-checks-v0.6-2026-11-09.csv`: unresolved population/abstract checks.
- `PolicyMemo-Search-D-exclusion-QA25-v0.6-2026-11-09.csv`: reproducible random provisional-exclusion audit sample; **not yet human reviewed**.
- `PolicyMemo-Search-D-audit-counts-v0.6-2026-11-09.json`: machine-readable counts.
- `Search-D.csv`: original unmodified export, retained separately.

## 7. PRISMA-style reporting boundary

Count 1,096 raw database search hits (825 A–C + 271 D), 78 duplicate hits, and 1,018 unique records. Do **not** sum the exploratory D trial queries; do **not** mark provisional AI exclusions as researcher-validated exclusions or turn the total into “studies included.” Additional sources located via citation-following or researcher recommendation should be counted through separate discovery routes. Full-text eligibility, final inclusion, and reproducibility of future citation-following remain outstanding.