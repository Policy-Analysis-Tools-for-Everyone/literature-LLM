# Research quality gates

**Purpose:** improve the trustworthiness of a critical narrative review intended to inform the PolicyMemo.ai study, not produce a misleading ‘automatic peer review’ stamp.

## Gates

| Gate | Trigger | Required evidence | Outcome |
|---|---|---|---|
| Q0 — Scope and authority | Every session | Approved study question, population boundary, adjudicated decisions, current amendment status | Stop if the task assumes unapproved access or changes human decisions |
| Q1 — Source identity | New paper | Verified DOI, title, year, version/status; full text or abstract access status; PDF page conventions | Unverified metadata marked; no fabricated Harvard reference |
| Q2 — Method appraisal | New primary paper | Sampling, design, unit of analysis, comparator, task/intervention, outcome operationalisation, missingness, bias/transfer limitations | Conditional, design-specific appraisal; not a numerical ‘quality score’ |
| Q3 — Claim-to-evidence | New/revised synthesis | Specific claim; support/contradiction; source DOI and section/page/table; evidence type; alternative explanation | No HIGH-impact claim without retrievable support |
| Q4 — Review screening audit | Search or decision change | Original search/query/date, raw hits, duplicate logic, screening label, actor, rationale and version | Never convert AI-only screening to confirmed human exclusion; preserve old status |
| Q5 — Cross-paper synthesis | Major synthesis update | Corroboration/counterevidence, differing populations, overlapping review samples, null findings, theories and unresolved gaps | Distinguish finding, author interpretation and researcher inference |
| Q6 — Study design translation | New research activity/protocol | Claim IDs underpinning choice, observability, rival explanations, feasibility, risks, ethics permission | No claim a proposed interview/observation is approved |
| Q7 — Researcher decision | Scope, framework, protocol or final prose | Visible unresolved disagreements and explicit researcher acceptance/rejection | Mark ‘human-adjudicated’ only following actual decision |

## Study-design-specific appraisal questions

**Experiments / quasi-experiments:** randomisation and allocation, intervention and comparator equivalence, baseline difference, assessment contamination from AI access, construct validity, task realism, clustering/unit of analysis, attrition, short vs delayed follow-up, preregistration/analysis flexibility, effect sizes and uncertainty. A non-significant result is not automatically evidence of no effect.

**Qualitative work:** recruitment/setting, positionality, sample/context sufficiency, access to real interaction traces versus retrospective reporting, coding transparency, discrepant cases, whether examples represent all participants, alternative explanations, transferability. Small n is not automatically disqualifying; distinguish reported experiences from observed behaviour.

**Longitudinal and group-level studies:** observations and timepoints, group vs individual unit, dependence, maturation, repeated-task learning, selectivity of retained traces, cohort changes and confounding.

**Reviews/meta-analyses:** eligibility, database/search coverage, quality appraisal, heterogeneity, dependence/overlap among included studies, study-level moderator transparency, construct consistency, publication bias. Do not double-count an original study repeated in multiple reviews.

**Conceptual papers:** what is argued, original basis, conceptual coherence, competing theories, assumptions and which empirical expectations follow; do not assign experimental evidence status.

## Design-targeted integrity test

Before releasing study recommendations, explicitly answer:
- What evidence of *enacted* judgement differs from final memo quality, self-report and prompted compliance?
- What can be observed without data sources not yet ethically authorised?
- Can rival mechanisms (teaching, peer work, task repetition, selection, existing proficiency, tool differences) explain the observed episode?
- How are disagreement, justified acceptance, non-adoption, and ambiguous cases coded?
- What would disconfirm our preferred conceptual framework?

## External toolkit provenance

Adapted **in approach, not copied code** from [Academic Research Skills](https://github.com/Imbad0202/academic-research-skills): its `deep-research`, `sr-screener` and `academic-paper-reviewer` modes, claim/source verification and human checkpoints. ARS licence: CC BY-NC 4.0; review obligations before incorporating its actual implementation. Distinctive project-specific safeguards above are written for this review. AI ‘double review’ is not independent human second screening.
