# External research toolkit assessment — academic-research-skills

**Source:** [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills), inspected 9 November 2026. Upstream README shows **v3.24.2**, and the repository licence is **CC BY-NC 4.0**.

## What it offers

| Upstream mode / feature | Project adaptation | Status |
|---|---|---|
| `sr-screener` protocol, pilot, audit, full-text and report modes | Apply stable eligibility to A–D register; preserve AI-labelled decisions and random false-exclusion audit | Own research-specific protocol added; **no external skill installed** |
| `deep-research` fact-check, review and source verification | Claim-support audit, page anchors, conflicting evidence, design relevance | Own citation and gates documented |
| `academic-paper-reviewer` methodology-focus and devil's advocate | Study-design-specific critique of experiments, qualitative work, group trajectories, reviews | Own appraisal questions documented |
| `academic-paper` citation-check and format-convert | UK Harvard author–date house style, DOI/title checks, accurate original page locators | Own Harvard style drafted; bibliography generation not yet implemented |
| `academic-pipeline` integrity checkpoints and human decisions | Human confirmation before changing research questions, screening labels, conclusions and UCL study methods | Human authority preserved; no automated gates claimed |

## Not adopting wholesale

- Upstream **systematic-review / PRISMA compliant** claims: this review remains a critical narrative review with transparent searching; a diagram may describe actual identification without suggesting completed systematic methods.
- Automatic multi-agent ‘independent’ adjudication: two AI reviewers are **not** independent human double-screening.
- Full manuscript production and automatic method selection: study questions and consequential inference remain researcher-led.
- External agent hooks, APIs and dependencies: inspect installation permissions, licensing and data flows before enabling in a UCL-related research workflow.
- Upstream APA defaults: this project needs a consistent **Harvard** house style, with an eventual target-journal-specific variant.
- Bulk upstream source-code copying or vendoring: CC BY-NC reuse obligations and potential future commercial work must be reviewed first.

## What to test next

Conduct a controlled evaluation against the current 18-paper corpus:
1. **Claim verification:** choose ten high-impact assertions, locate original PDF support, log false supports and missing locators.
2. **Methods critique:** test at least one small qualitative paper, one randomised or quasi-experimental paper, one meta-analysis and one theoretical paper for design-specific limitations.
3. **Screening audit:** randomly sample previously proposed exclusions and compare agent recommendations with actual human reading.
4. **Citation formatting:** render five verified records into the selected Harvard variant and check manually.

Only install upstream tooling if it clearly outperforms our light workflow **and** passes licence, privacy and oversight review. See [quality gates](../methods/quality-gates.md), [screening QA plan](../methods/screening-audit-plan.md), [Harvard standard](../../references/harvard-standard.md).
