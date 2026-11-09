# PolicyMemo.ai — focused reading and exclusion-audit protocol (v0.3)

**Date:** 2026-11-08. **Phase:** title/abstract screening refinement. **Status:** AI-assisted prioritisation only, not final publication eligibility or dual human screening.

## Purpose

The researcher accepted a stricter *active reading* strategy after the initial 98-case review became too broad. This v0.3 pass preserves the entire 763-record original screening dataset and all 14 frozen researcher-adjudicated decisions; it **does not** silently replace exclusions or declare final PRISMA counts.

### Review question

How does interaction with generative AI shape the development, exercise and justification of judgement among adult learners and practitioners undertaking complex professional tasks?

### Narrow scope (v0.3)

1. **Core / immediate full text:** empirical records in which adult learners or practitioners *actually use or work with* generative AI to make, contest, explain or revise judgement in complex tasks, including feedback uptake, critique, peer–AI dialogue, and division of cognitive labour. Conceptual contributions directly defining evaluative judgement are included as theory, never as empirical learning evidence.
2. **Contextual / selective full text:** retain only if a *specific planned analytic role* exists: foundational evaluative judgement/reflection; human-only critique as comparative theory; assessment validity; or professional accountability. General discussions, acceptance surveys and generic pedagogical integrations are placed in **context reserve** rather than an expanding active reading list.
3. **Exclude at abstract stage (provisional):** benchmarks of AI performance, generic adoption/attitude surveys, governance debates without situated use, conference-proceedings records, and one-off tool demonstrations without relevant judgement processes. Distinguish these from comparative work on judgement even where credibility is involved.
4. **Methodology:** a paper's *relevance* is independent of evidence quality. Report what is measured: observed process, transcripts, participant reflection, task output, self-reported impressions, post-test, or delayed transfer. Do not claim that assisted task grades demonstrate learning.
5. **Uncertainty:** use not-reviewed/context reserve/audit queue when an abstract is insufficient; do not infer data or missing measures. Keep full-text and researcher adjudication outstanding.

## Preserved identification counts

- Scopus A 362, B 323, C 140; **825 hits**.
- **62 repeated hits** removed; **763 unique records**.
- **14 researcher-adjudicated pilot decisions frozen**.
- Prior v0.2 AI-only screen: 196 core, 259 contextual, 31 uncertain, 277 excluded. These are **not final PRISMA eligibility counts**.

## v0.3 outputs

- `PolicyMemo-screening-priorities-v0.3-2026-11-08.csv`: all 763 records with v0.2 classification intact, new reading priority, QA98 proposed status, and flags for risk-based exclusion auditing.
- `PolicyMemo-QA98-focused-audit-v0.3-2026-11-08.csv`: all 98 difficult cases, preserving their v0.2 and earlier second-pass proposals.
- `PolicyMemo-exclusion-audit-queue-v0.3-2026-11-08.csv`: **96 non-unique audit selections merged into unique records**, combining deterministic risk triggers (71 records) and a fixed-seed **30-record random sample** from all 277 exclusions. No records in this queue are automatically researcher-accepted.
- `PolicyMemo-focused-reading-queue-v0.3-2026-11-08.csv`: **65 unique articles** from the previous 37-paper shortlist, targeted QA98 direct/core cases, selected contextual comparators and rescue proposals. This is a **reading queue, not the final included-study set**.
- `PolicyMemo-seven-decision-cards-v0.3-2026-11-08.csv`: seven consequential cases for researcher judgement, with complete Scopus abstracts.

### Targeted exclusion flags

These are risk *signals*, not the result of 277 independent qualitative reappraisals. Automated selection uses explicit text patterns for actual AI-mediated reflection, feedback uptake, revision, practice logs or professional judgement; records originally classified as excluded are **not automatically changed**. The additional fixed-seed random selection checks whether lexical targeting itself misses eligible studies.

#### Immediate false-exclusion candidates

| Record | Provisional proposal | Why |
|---|---|---|
| SC-0092 | Core candidate | Students co-design GPTs and reflect on iterative decisions using project logs; task differs from policy analysis. |
| SC-0578 | Core candidate | Self-monitoring and adoption of GenAI feedback in revision; group differences do not establish causality. |
| SC-0357 | Contextual | Professional development narratives of language educators, but not clearly observed individual AI decisions. |
| SC-0407 | Contextual | Hybrid-intelligence feedback intervention; need to determine whether judgement is measured or only outcomes. |
| SC-0684 | Contextual | Human/technology collaborative reflection; not an AI-specific empirical finding. |

### Methodological safeguards before freezing exclusions

The previous random sample found **10 potentially false exclusions in 30 checked records**. This suggests that the current AI-only exclusion pool may contain more eligible studies. Do not certify the 277 exclusions solely by reviewing the 98-record QA queue or this lexical sweep. The researcher, or a suitably trained independent reviewer, should inspect the flagged records and a genuinely random set of exclusions; if disagreements remain material, expand human screening. Record original and revised labels, reasons, assessor, date, and whether a full text was obtained. Only then report final exclusion totals.

## Researcher decisions needed (seven cases)

- **SC-0077**, *Telling Students to Evaluate Does Not Make It Happen: Task Stage, Offloading Tendency, and Error Detection in AI-Assisted Student Writing*: v0.2 **Uncertain**, proposed **Core candidate**. An experimental design that distinguishes students evaluating AI from AI evaluating students. Strong process relevance despite error-detection outcome.
- **SC-0425**, *Evaluating GenAI as a Grading Support Tool in Higher Education: Impacts on Workflow, Efficiency, and Feedback Quality*: v0.2 **Core candidate**, proposed **Core candidate**. Professional evaluative judgement of TAs in AI-assisted marking. Does the practitioner strand encompass educators, not just learners?
- **SC-0116**, *Empathy-Driven Digital Practices in a Computational Design Studio: The Feeling-AS Framework*: v0.2 **Contextual candidate**, proposed **Contextual candidate**. AI is one of several studio technologies. Keep as a reflective-practice comparator without claiming separable GenAI effects.
- **SC-0092**, *Co-creating custom GPTs: an autoethnographic study of undergraduate students as partners in generative AI innovation*: v0.2 **Exclude**, proposed **Core candidate**. Rescue from exclusion: students co-design GPTs, test and revise them, with reflexive logs. Distinct task from policy analysis.
- **SC-0578**, *AI self-efficacy and knowledge graph-integrated generative AI feedback in higher education*: v0.2 **Exclude**, proposed **Core candidate**. Rescue from exclusion: GenAI feedback uptake, self-monitoring and revision. Compare measured outcomes versus causal learning claims.
- **SC-0357**, *Navigating Professional Growth in AI in Language Education: Narratives from a University in Hong Kong*: v0.2 **Exclude**, proposed **Contextual candidate**. Rescue from exclusion: teacher professional growth narratives. Need human–AI practice detail before promoting to core.
- **SC-0407**, *Hybrid Intelligence Feedback: A Model Proposal and Preliminary Study*: v0.2 **Exclude**, proposed **Contextual candidate**. Rescue from exclusion: feedback intervention; whether the study measures judgement process is unclear from the abstract.

The seven cases are *illustrative boundary decisions*, not a claim that seven researcher decisions validate the other 756. Keep the chosen conceptual boundary fixed when full-text appraisal begins. Separately maintain a screening log, a full-text appraisal log, and a narrative synthesis.