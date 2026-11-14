# Policy-reasoning decision episodes — analytic framework v0.1

**Date:** 14 November 2026. **Status:** unvalidated design proposal, not an approved research instrument or permission to process student data with an LLM. The [conceptual framework](../../wiki/synthesis/conceptual-framework-v0.1.md) is the theoretical justification.

## Unit of analysis

An **episode** is a bounded, traceable sequence in which an actor introduces, evaluates, retains, changes or rejects a consequential choice in policy analysis—such as the problem framing, a causal claim, evidence source, normative criterion, option, uncertainty or recommendation.

**Episode start:** first visible choice or challenge in an authorised artefact or consented conversation. **Episode end:** documented decision, revision, explicit deferral or end of trace. Multiple episodes by the same student or group are **not statistically independent cases**.

## Proposed coding fields

| Code | Question | Candidate codes | Boundary |
|---|---|---|---|
| E1 — Analytical object | What is at stake? | problem boundary; causal claim; evidence; uncertainty; criteria/public value; alternative; trade-off; recommendation | Mere mention is not a consequential choice |
| E2 — Visible provenance | Who introduces the move? | student; peer; teacher; AI; joint; unknown | Do **not** infer authorship from fluent prose or final ownership |
| E3 — Basis for evaluation | Which grounds are visible? | evidence/relevance; causal logic; public value; equity; feasibility; legitimacy; uncertainty; none stated; unobservable | A named criterion is not proof it was applied competently |
| E4 — Response to challenge | What happens? | accept with reasons; accept without visible reasons; modify; reject with reasons; reject without reasons; defer; unobservable | Acceptance may be justified; rejection is not automatically good judgement |
| E5 — Revision evidence | Did the artefact or argument change? | explicit textual change; changed criteria; changed framing; unchanged with rationale; no available comparison | Distinguish an AI suggestion from actual uptake |
| E6 — Regulation/reflection indicator | What monitoring or reframing is visible? | plan; check; seek alternatives; notice inconsistency; reframe; later reflection; none visible | Do not code mental processes that were not observed |
| E7 — Evidence type | How is this known? | directly observed text/edit; retrospectively reported; researcher inferred; not observable | Keep source quotations/line identifiers and confidence distinct |
| E8 — Quality and defensibility | How is quality assessed? | domain-specific rationale; competing values; calibration of uncertainty; negative case; undecidable | Not an automatic score; needs a defensible policy-specific rubric |
| E9 — Temporal comparison | What can change be compared with? | prior task; later comparable task; same-session revision; none | Same-session improvement is **not** proof of durable learning |
| E10 — Alternative explanation | What else might account for this? | peer input; tutor prompt; task repetition; prior proficiency; self-selection; formatting requirement; tool affordance; unknown | Record rival hypotheses rather than assigning causation |

## Synthetic coding illustration — not a research participant

**Initial position:** “The problem is that applicants fail to complete the online licensing form.”  
**AI suggestion:** “Consider whether complex eligibility criteria and administrative design create the difficulty.”  
**Student revision:** “Reframe as unequal administrative burden; compare low digital confidence with service complexity, and seek data before asserting cause.”

A provisional episode might code: **E1 framing/causation; E2 AI challenge, student revision; E3 equity, evidence and uncertainty; E4 modify with reasons; E5 documented reframing; E6 explicit check; E7 directly visible in synthetic transcript**. It is **not** evidence the student learnt to frame future problems independently. A plausible alternative is that the example explicitly cued the desired revision.

## Minimal episode sheet

```yaml
episode_id: "EXAMPLE-001"
case_id: ""
task_id: ""
source_type: "authorised_artefact | consented_tool_trace | approved_observation | approved_interview"
start_locator: ""
end_locator: ""
e1_decision_object: ""
e2_visible_provenance: ""
e3_grounds: []
e4_response: ""
e5_revision: ""
e6_regulation: []
e7_evidence_type: ""
e8_quality_assessment: "undecided"
e9_temporal_comparison: ""
e10_rival_explanations: []
counterevidence: ""
coder: ""
status: "provisional"
```

## Design and ethics limitations

Under the **original approved plan**, the likely material is opt-in seminar artefacts, voluntarily shared PolicyMemo.ai conversations, and eligible final memos after marking. This will produce **partial episodes**; absent peer/tutor dialogue should be coded *unknown*, not imagined. The approved plan explicitly prohibits feeding actual research participant material into an AI analysis tool. This repository therefore holds **only the codebook and synthetic examples**.

Interviews, structured observations across groups and extra questionnaires remain **proposed**, to be incorporated in a future ethics amendment **after** research design refinement.

## Validation before use

1. Researcher adjudicates the **episode definition** and which categories count as policy judgement.
2. Test the scheme on **synthetic contrasting examples** including defensible AI acceptance, uncritical AI rejection, and unchanged work with good reasons.
3. Run a human coding pilot on ethically authorised material **outside AI tools** once permitted. Discuss coder disagreements, boundary definitions and negative cases.
4. Distinguish **exercise** of judgement from **development** with a separately justified temporal/comparative strategy.
5. Revise the codebook based on actual ambiguity rather than forcing every observation to fit.
