# Search E — generative AI in policy analysis, advice and public-sector work (DRAFT, not yet run)

**Status:** drafted 9 November 2026 at the researcher's request. **Not executed.** No counts, exports or screening exist yet. Query strings below are proposals; they must be tested in Scopus Advanced Search, and every iteration recorded as for Search D ([Search D audit](search-d-integration-v0.6.md)).

## 1. Why this search is needed

Searches A–D combine generative AI with judgement, reflection, feedback/scaffolding, professional practice and metacognition. **None includes a policy or public-sector term.** Across the 1,018 unique A–D records, one title concerns policy teaching (Casey, undergraduate public-policy capstone; already a [methodological comparator](../wiki/sources/casey-public-policy-teaching.md)), and no title mentions public administration, the public sector, civil servants or government.

The PolicyMemo.ai study concerns **policy reasoning**. Without a policy-specific search, the review can describe how generative AI shapes judgement in writing, design, coaching and teaching, but cannot say whether AI-assisted policy analysis, policy education or public-sector analytical work has already been studied. Finding that little exists is a reportable result; not having looked is a gap. Search E is a coverage check, not an expansion of scope: the review question and [eligibility](eligibility.md) are unchanged.

## 2. Proposed query (iteration E1)

```text
TITLE-ABS-KEY(
  "generative AI" OR
  "generative artificial intelligence" OR
  ChatGPT OR
  "large language model*"
)
AND
TITLE-ABS-KEY(
  "policy analys*" OR "policy analyst*" OR
  "policy advi*" OR "policy brief*" OR "policy memo*" OR
  "policy design" OR "policy formulation" OR
  "public policy" OR "public administration" OR "public management" OR
  "public servant*" OR "civil servant*" OR "civil service" OR
  "public sector" OR "government official*" OR bureaucra*
)
AND
TITLE-ABS-KEY(
  judgement OR judgment OR reasoning OR
  "decision making" OR "decision-making" OR deliberat* OR
  "evidence use" OR "evidence-informed" OR
  student* OR education OR teaching OR training OR
  curricul* OR pedagog* OR "professional practice"
)
AND PUBYEAR > 2019
AND PUBYEAR < 2027
```

The generative-AI block matches Search D's wording so the searches can be deduplicated and compared.

### Design choices to check in Scopus

- **No bare `learning`** in block 3: it would match "machine learning" and "deep learning" in most AI abstracts. `student*`, `education`, `teaching`, `training` carry the learning sense.
- **`policymaker*` and `policy making` are left out of E1** because abstracts commonly end with "implications for policymakers", which is likely to swamp the results with papers that are not about policy work. Test them in E1b (below) and record the difference rather than assuming.
- **Expect noise from AI-governance and institutional AI-use policy papers** (e.g. university ChatGPT policies, AI regulation). These remain out of scope unless they examine practitioners' or students' actual reasoning or judgement with generative AI ([eligibility](eligibility.md)).

## 3. Iterations to record

| Iteration | Change | Purpose |
|---|---|---|
| E1 | As above | Primary candidate |
| E1b | Add `policymaker* OR "policy maker*" OR "policy making" OR "policy-making" OR policymaking` to block 2 | Sensitivity: how much is gained vs added noise |
| E2 (only if E1 is too large to screen) | Change block 2 from `TITLE-ABS-KEY` to `TITLE` | Narrower fallback |

Record each iteration's Scopus count and date. As with Search D, **only the exported iteration counts towards identification totals**; exploratory counts are not added.

## 4. Known-item checks

- **Casey (2024/2026), *ChatGPT in public policy teaching and assessment*** — https://doi.org/10.1111/1467-8500.12647. E1 should retrieve it. If it does not, the query is faulty.
- Herdağdelen, Joren & Tamkin is a manuscript of unverified publication status ([source note](../wiki/sources/herdagdelen-experts-judgement.md)) and is not expected in Scopus; do not treat its absence as a query failure.
- Any further policy-teaching or public-sector studies the researchers already know of should be listed here before running, so retrieval can be tested against them.

## 5. After export

1. Keep the original `Search-E.csv` unmodified in controlled storage with its SHA-256; do not commit it here ([data handling](data-handling.md)).
2. Deduplicate against the 1,018-record A–D register by normalised DOI and title, as for Search D, and record the duplicate audit.
3. Screen with the existing eligibility rules. Policy-specific studies with undergraduate-only samples (like Casey) are **methodological or contextual leads**, not direct population evidence.
4. Update [search provenance](search-provenance.md) only once real counts exist.
5. Separately note that Scopus-only retrieval misses some known sources (e.g. Lee et al. 2025, CHI, on knowledge workers' critical thinking, is in no A–D export). Citation-following, and possibly the ACM Digital Library, should be documented as additional discovery routes rather than counted as Scopus hits.
