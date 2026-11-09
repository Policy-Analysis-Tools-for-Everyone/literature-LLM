# Minimal research agent workflow

## Start: audit
Read `README.md`, `AGENTS.md`, `protocol/eligibility.md`, `protocol/search-provenance.md` and `wiki/index.md`. Confirm whether source PDFs are available. Do not guess that an indexed citation means a source has been read.

## 1 — INGEST
Take **one** user-specified full text; verify DOI, population and publication status. Create a source note from `_TEMPLATE.md`. Quote sparingly with exact page citations. Distinguish author claims from findings, and report limitations and null results.

## 2 — CONNECT
Revise only directly affected concept/debate pages. Link source note and assess whether it supports, qualifies or contradicts the current synthesis. Do not write conclusions unsupported by originals.

## 3 — QUERY
Answer with specific source note links and full-text page references; state what remains unknown. A tool should support the researcher's judgement, not substitute for it.

## 4 — LINT / RECONCILE
Check local Markdown links, source access status, mismatched populations, contradictory claims, missing counterevidence and unlogged changes. Human adjudications stay authoritative. Record any proposed screening change as a proposal until accepted.

## 5 — LOG
Append date, source, pages inspected, changed paths, significant inference and outstanding gaps to `wiki/log.md`. Commit a small, reviewable diff.

### First test
Appraise Wiles (2026) from its full text (already a starter note), then obtain one **confirmed** postgraduate original study in the reading queue and ingest it. Run the same question before and after to see if the wiki's synthesis becomes more accurate rather than merely longer.
