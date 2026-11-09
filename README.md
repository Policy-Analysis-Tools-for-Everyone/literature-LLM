# Literature LLM — practice as software

A **version-controlled research wiki** for a focused critical narrative literature review informing the PolicyMemo.ai study. The aim is to accumulate, question and refine interpretations of original studies—not train a new language model or generate a paper on autopilot.

**Research question:** How does interaction with generative AI shape the development, exercise and justification of judgement among adult learners and practitioners undertaking complex professional tasks?

## How it works

1. **Evidence stays separate from synthesis.** Raw search exports, eligibility decisions and licensed PDFs are retained in controlled storage; wiki pages hold carefully sourced, revisable interpretation.
2. **Ingest** one complete source at a time: create a source note with methods, population, outcomes, actual findings, limitations and access status.
3. **Connect** that source to relevant conceptual and debate pages, recording support, contradiction, or uncertainty.
4. **Query** the wiki with traceable citations to original source notes; say when evidence is absent.
5. **Lint** local links and source status, then commit a documented change. A human reviews consequential research decisions.

This repository is **private**, but that does not authorise uploading UCL participant data, licensed PDFs, or research records outside approved storage arrangements. See [data handling](protocol/data-handling.md).

## Start here

- [Agent instructions](AGENTS.md), shared across model providers
- [Research scope and eligibility](protocol/eligibility.md)
- [Research provenance and search counts](protocol/search-provenance.md)
- **[Current eighteen-paper synthesis](wiki/synthesis/new-postgraduate-evidence.md)**
- [Research wiki](wiki/index.md)
- [Change log](wiki/log.md)
- [Initial sourced example: Wiles et al.](wiki/sources/wiles-2026.md)
- [First ingestion procedure](protocol/workflow.md)

## Current research state (9 Nov 2026)

Scopus A–D: **1,096 exported hits → 78 duplicate hits removed → 1,018 unique records**. AI-assisted title/abstract screening remains **provisional**, with a consequential false-exclusion risk; these are *not* final PRISMA eligibility counts. Initial full-text appraisals exist outside this repository; new wiki source notes must be checked against those actual PDFs before citation-heavy synthesis.

## Tool-agnostic by design

ChatGPT, Claude Code or another assistant may work on this repository. `AGENTS.md` is the governing protocol; `CLAUDE.md` links to it. The repository and your decisions are the source of truth, not a chat history. For now, no database, embeddings, server or API key is needed.

## Six-paper pilot and research handover

- [Research handover v0.6](protocol/handover-v0.6.md)
- [Researcher decisions v0.4](protocol/researcher-decisions-v0.4.md)
- [Scopus A–C audit](protocol/searches-a-c-original-audit.md)
- [Search D audit](protocol/search-d-integration-v0.6.md)
- [Six supplied PDFs: roles and SHA-256 manifest](protocol/source-library-index.md)
- [Evidence-based six-paper synthesis](wiki/synthesis/six-paper-synthesis.md)

The raw Scopus data, licensed PDFs, and earlier cycle-seven synthesis remain in controlled storage rather than being copied into this repository.


## Second literature ingestion (9 November 2026)

The repository now has **18 distinct full-text source notes**: the original six plus twelve newly acquired papers. The [expanded critical synthesis](wiki/synthesis/new-postgraduate-evidence.md) is the current working synthesis; the [original six-paper synthesis](wiki/synthesis/six-paper-synthesis.md) is retained as a versioned baseline. For exact source hashes and the Fernandes filename correction, see [source library manifest](protocol/source-library-index.md). These are **initial AI-assisted appraisals**, not researcher-adjudicated quality assessments or completed review inclusions.
