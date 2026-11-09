# Harvard author–date reference and claim-linking standard

**Scope:** UCL study drafts and the wiki. Harvard is a *family* of conventions rather than one globally unique style. Until the target journal/UCL guide is selected, this project uses a documented **UK Harvard author–date house style** and retains machine-readable source identities. A submission must apply the specific target publisher's instructions.

## In-text citation

- One author: `(Surname, 2026)`; two: `(Surname and Surname, 2026)`.
- Three or more: `(Surname et al., 2026)` (house style, check venue).
- Narrative citation: `Surname et al. (2026) find…`.
- Direct quotation: `(Surname, 2026, p. 14)` and quote no more than justified by rights; use exact original page.
- Specific table, study or outcome: add locator where available, `(Surname, 2026, Table 2)`.
- Distinguish *PDF page* from publisher's *printed page*. If only PDF pagination exists, mark it as `PDF p. 7` in source notes and do not silently convert it into journal page numbering.
- Multiple works: `(Surname, 2018; Another, 2024)` with consistent chronological or alphabetical ordering.
- Same author/year: `(Surname, 2026a, 2026b)`, assigned only after full bibliography validation.
- For preprints/working papers, explicitly specify version/status and do not imply peer review.

## Reference list patterns

Journal: `Surname, I. and Surname, J. (2026) ‘Article title’, Journal Title, 17(2), pp. 100–114. doi:10.xxxx/xxxxx.`

Online article number: `Surname, I. et al. (2026) ‘Article title’, Journal Title, 175, article 108779. doi:10.xxxx/xxxxx.`

Book: `Surname, I. (1983) Title of book. Place: Publisher.` (place retained in this house style, venue conventions may differ).

Conference: `Surname, I. et al. (2025) ‘Paper title’, Proceedings title, pp. xx–yy. doi:10.xxxx/xxxxx.` Only include verified pages, editors, venue and DOI.

Web: `Organisation (2026) Title. Available at: URL (Accessed: 9 November 2026).` Use access date only for actually accessed pages.

**Never fabricate** authors, issue, page range, publication date, study year, DOI or access date. Missing metadata stays `[verification pending]`, not inferred.

## Machine-readable record

A `references/library.bib` and/or `references/library.json` is the eventual source of bibliographic truth. Every source note should identify DOI or canonical permanent ID; **its title and author names should be checked against the original paper and publisher**. A DOI resolving to another title is a blocking error. Case-specific sources are also listed in `protocol/source-library-index.md`.

## Claim-to-citation test

Citations are not decoration. For each substantive assertion, log:

`claim_id | claim | status (finding/author-interpretation/our-inference) | population | outcome | support DOI | locator | counterevidence | quality limitation | researcher_status`

A real DOI with a real article **does not show** that the article supports the particular claim. The original passage/table must be inspected. High-impact claims influencing study design require manual verification. Do not treat an LLM-generated 'citation passed' label as peer review.

## Self-tests before submission

1. Every in-text author-year is in bibliography, and vice versa (with explicit justified exceptions).
2. DOI resolves to the stated publication, not merely a vaguely related record.
3. Distinct sources are not duplicated under different filenames.
4. Bibliography is consistently rendered in chosen Harvard variant, including article numbers and DOI.
5. Page-specific qualitative claims match actual printed/PDF page.
6. No abstract-only record is silently represented as full-text analysis.
7. Conceptual and empirical citations are not interchanged.
