# PolicyMemo.ai — Scopus pilot title-and-abstract screening

**Date:** 8 November 2026  
**Reviewer:** One AI-assisted screener (GPT-6), **provisional**; no independent second reviewer or researcher adjudication.  
**Purpose:** Calibrate eligibility for a **focused critical narrative review**; not a completed systematic review.  
**Source:** User-exported Scopus searches A, B and C, and the preserved stratified pilot sample `PolicyMemo-Scopus-pilot-sample-90-2026-11-08.csv`.

## 1. Search, sampling and audit boundary

Three Scopus search runs: Search A **362** hits; B **323**; C **140**; **825** combined search hits. Across exports, **62** repeated search hits were removed, leaving **763** unique records. The 90-record pilot was drawn via stratified sampling without replacement from: A only 25/312; B only 25/290; C only 25/106; multiple searches 15/55. Sample selection used ascending RecordID, sequential `random.Random(20261108)` calls, as documented in the original sampling protocol. The original three CSVs, deduplicated master and sampling frame were not modified.

**Do not mistake this sample for a new or independent corpus.** The 90 records belong to the 763. At this point 90 have provisional title/abstract decisions, **673 remain unscreened**. None has been declared finally eligible after full-text assessment.

## 2. Eligibility applied in the pilot

**Review focus:** How generative AI shapes development, exercise or explanation of judgement through professional/complex work among adult learners and practitioners, including reflection, feedback, critique, peer discussion and AI-mediated deliberation.

**Core candidate:** Original empirical interaction with GenAI and identifiable processes of adult reasoning, feedback uptake, reflection, professional judgement, or complex practice. Directness and quality vary: this label **does not mean high-quality causal evidence**.

**Contextual candidate:** Relevant conceptual work, synthesis, intervention design or adjacent empirical comparison that informs theory or methods but does not directly test/observe the central process.

**Uncertain:** Abstract does not provide enough information about methods or the extent of GenAI-mediated adult practice. Examine full text before deciding.

**Exclude:** Out of the active scope. Recurring boundaries: benchmark studies of AI reasoning without human practice; AI grading accuracy; generic uptake and confidence surveys without meaningful process information; primarily AI credibility, source verification, bias or error detection; work about AI governance rather than professionals using AI; work with GenAI only as researchers' review tool.

**Guardrail:** Positive, negative and null findings are all eligible. Evidence based on perception cannot be treated as demonstrated learning. Enhanced assisted output cannot be equated with independent judgement. The screen does not require AI-free transfer measures, which would themselves be only one indicator of learning.

## 3. Results

| Mutually exclusive pilot stratum | Core | Contextual | Uncertain | Exclude | Total |
|---|---:|---:|---:|---:|---:|
| A only | 9 | 9 | 0 | 7 | 25 |
| B only | 8 | 6 | 1 | 10 | 25 |
| C only | 4 | 6 | 1 | 14 | 25 |
| Multiple searches | 4 | 7 | 0 | 4 | 15 |
| **Total** | **25** | **28** | **2** | **35** | **90** |

**Interpretation:** Search C generated the highest exclusion count in this pilot (14/25), because its broad professional vocabulary also retrieves GenAI benchmarks, AI governance and other adjacent work. Its four core candidates are distinctive practitioner or workplace studies, so the evidence does not justify discarding it. Search A and Search B give relatively richer learning/feedback evidence. Multiple-search records were deliberately oversampled and **their distributions cannot be extrapolated unweighted to the full 763**.

The 28 contextual papers are **not** a list of confirmed full-text inclusions; they may be used selectively to follow citations or inform theoretical framing. In particular, conceptual models should not be treated as empirical demonstrations that AI improves learning.

### Exclusions

Thirty-five pilot records were provisionally excluded. Major clusters include AI-only capability benchmarks, AI-scoring agreement, student opinions of AI critical-thinking benefits without process observations, broad GenAI adoption, and accuracy/credibility research. All have an individual primary reason in the workbook and screened CSV; the wording is retained rather than forcing artificial reasons into a tiny set of categories.

### Uncertain records requiring targeted methods checks

- **PILOT-B-25 (SC record shown in workbook), _Promoting active learning with ChatGPT: A constructivist approach in Sri Lankan higher education_.** Abstract lists 16 strategies but does not establish sample, data collection, or whether it observed actual adult AI-mediated reasoning.
- **PILOT-C-21, _Digitalisation in regenerative cities: opportunities and challenges in the built environment_.** Interviews, survey and live cases examine professional discretion, but GenAI appears to be one of several digital technologies; verify extent of actual GenAI interaction.

## 4. Recommended first full-text retrieval queue (not yet appraised)

| Priority | Pilot / Record ID | Paper | Specific value and interpretive caution |
|---|---|---|---|
| High | PILOT-C-25 / SC-0719 | "Will This Tool Ever Push Back or Challenge Me?": Reflections on a Multi-agent LLM Tool for Perspective Seeking | Agents explicitly challenge workers and change perspective-seeking; **caution:** Interview/probe, not observed long-term learning. |
| High | PILOT-A-19 / SC-0197 | Orchestrating human and artificial intelligence: a model for collaborative reflective practice in EFL teacher development | Cycles of human, peer and ChatGPT-supported professional reflection; **caution:** AI is bundled with multiple learning mechanisms. |
| High | PILOT-B-12 / SC-0406 | Investigating the impact of ChatGPT-assisted feedback on the dynamics and outcomes of online inquiry-based discussion | Compares idea-oriented versus task-oriented AI feedback in peer inquiry; **caution:** Non-random class assignment; assess comparability. |
| High | PILOT-C-17 / SC-0716 | Beyond Answer Generation: University Teachers’ Experiences with a Reflective GenAI Chatbot for Professional Learning | Reflective AI tutor and pedagogical friction among professional educators; **caution:** Only 11 respondents used the tool. |
| High | PILOT-A-06 / SC-0330 | Between prompting strategies and ethical concerns: How EAP teachers develop materials with Generative AI | UK practitioner interviews plus actual chat logs and iterative revision; **caution:** Specialised language-teaching domain. |
| High | PILOT-X-04 / SC-0225 | Coaching the machine: exploring ChatGPT as coachee and feedback partner in coaching education | Postgraduate simulated professional practice with AI feedback; **caution:** Twelve students, perceived learning. |
| High | PILOT-B-06 / SC-0622 | Can AI be friends? AN innovative approach to integrating generative AI as a critical friend in Bahrain polytechnic's English foundation programme | AI feedback coincides with changes to peer/teacher interaction; **caution:** Small foundation programme; no causal attribution. |
| High | PILOT-X-11 / SC-0557 | How generative AI guided-professional development supports teachers’ engagement with mathematical creativity, content knowledge, and pedagogical content knowledge | AI-dialogue logs, artifacts and reflection in teacher professional development; **caution:** Eight participant embedded case study. |
| Next | PILOT-A-25 / SC-0007 | Students’ engagement with ChatGPT feedback: implications for student feedback literacy in the context of generative artificial intelligence | Observes uptake and metacognitive engagement with AI feedback; **caution:** Undergraduate language-writing task. |
| Next | PILOT-C-13 / SC-0725 | Are We on Track? AI-Assisted Active and Passive Goal Reflection during Meetings | Active versus passive AI prompts for workplace meeting reflection; **caution:** Short technology probe, 15 participants. |
| Next | PILOT-B-16 / SC-0440 | The effects of generative AI -supported peer feedback on preservice teachers’ learning outcomes, feedback uptake, and critical thinking | AI-supported peer feedback, artifact revision and critical thinking; **caution:** Inspect operationalisation of 'critical thinking'. |
| Next | PILOT-B-07 / SC-0401 | From Chatbot to Adaptive Syllabus-aware AI-mechanism: LLM Personalized Teaching Assistant in Higher Education | Hint-first tutor, log data and tensions between efficiency and reflection; **caution:** Student uptake not causal learning proof. |

Why these rather than the biggest effect sizes: they offer direct traces of **how** people interact with AI, including asynchronous peer discussion, challenging perspectives, iteration, reflection and participant accounts of affordances and constraints. We should inspect what was *observed*, *measured* and merely *claimed* before promoting any to the review's empirical core.

## 5. Provisional implications for the conceptual synthesis

1. **Human–AI–peer ecology matters.** A19, B06, B12 and B16 create a promising comparative strand on feedback and social interaction, not just individual output quality.
2. **Challenge is a separate interaction mechanism.** C25 and C17 indicate that people may expect AI to disagree, ask questions or resist easy completion; we must examine whether reported demand for challenge translates into learning.
3. **Reflection is not automatically learning.** Studies of logs, reflective statements and artifact revisions can reveal process, but self-explanation and reflection quality may be performative or shaped by assessment demands.
4. **Professional and postgraduate evidence exists but is thin.** A06, C13, C17, C25 and X04 provide practitioner or postgraduate cases; many other records involve preservice teachers or undergraduate students.
5. **Avoid a credibility detour.** Verification can occur as a sub-action within evaluative judgement, but work that principally benchmarks model accuracy or tests AI error spotting remains out of the active shortlist.

## 6. Recommended calibration and next phase

Before freezing criteria, the researcher should independently adjudicate a deliberately mixed **12–15-record check**, including at least five exclusion decisions and the two uncertain cases. Suggested borderline audit examples: A01 (error-review), B21 (AI-free retrieval framework), C09 (verification-dominant workplace interviews), C24 (policymakers discussing AI, rather than using AI for judgement), X15 (pre-GenAI human peer critique), and the two uncertain papers.

Record any rule changes with a timestamp. **Reapply those changes to the entire existing 90-record sample** before screening the remaining 673, so decisions remain consistent. A second independent human reviewer or a second AI model can offer useful challenge, but does not substitute for methodological adjudication.

The next screening pass can process the remaining records in small batches using the same decision columns. After title/abstract screening, only those sought at full text can be assessed for actual methods and quality. PRISMA-style flow counting should be finalised only after reconciliation, without double-counting the ninety sample records.

## 7. Working files / reproducibility

- `PolicyMemo-Scopus-pilot-screened-90-2026-11-08.xlsx`: definitive **provisional decision-level** pilot record; all 90 titles and abstracts, screening decisions, evidence labels, exclusion reasons, reviewer notes and sampling frame. Three existing tabs retained, plus a new `Pilot analysis` tab.
- `PolicyMemo-Scopus-pilot-screened-90-2026-11-08.csv`: portable row-by-row version for future platform handover.
- `PolicyMemo-Scopus-pilot-sampling-protocol-2026-11-08.md`: unchanged sampling design and seed.
- `Search-A.csv`, `Search-B.csv`, `Search-C.csv`: unchanged source exports.
- `PolicyMemo-Scopus-deduplicated-master-2026-11-08.csv`: unchanged 763-record corpus.

**Record status:** Completed AI-only pilot title/abstract screening; researcher calibration and full-text appraisal pending. Do not describe these as 25 finally included studies or as 35 formally excluded studies in a completed systematic review.