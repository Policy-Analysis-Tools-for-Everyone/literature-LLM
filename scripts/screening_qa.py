#!/usr/bin/env python3
"""Reproduce Scopus A-D identification and selected screening metadata checks.

Read-only, standard-library-only. Run against a controlled local archive:
python scripts/screening_qa.py /path/to/controlled/archive
Never upload Scopus abstracts or participant data to GitHub.
"""
import csv, sys, re, unicodedata, collections
from pathlib import Path

def records(p):
    with p.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def doi(v):
    return v.strip().lower().removeprefix("https://doi.org/").removeprefix("doi:")

def title(v):
    return "".join(c for c in unicodedata.normalize("NFKC", v).lower() if c.isalnum())

def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    names = "ABCD"
    original = [(s, records(root / ("Search-" + s + ".csv"))) for s in names]
    expected = dict(zip(names, [362, 323, 140, 271]))
    seen, duplicate_counts, kept = {}, collections.Counter(), []
    for group, rows in original:
        assert len(rows) == expected[group], (group, len(rows), expected[group])
        for row_no, row in enumerate(rows, 1):
            keys = []
            if doi(row.get("DOI", "")): keys.append("doi:" + doi(row["DOI"]))
            if title(row.get("Title", "")): keys.append("title:" + title(row["Title"]))
            if any(k in seen for k in keys):
                duplicate_counts[group] += 1
            else:
                kept.append(row)
                for k in keys: seen[k] = (group, row_no)
    combined = records(root / "PolicyMemo-Scopus-combined-1018-v0.6-2026-11-09.csv")
    excluded_ac = records(root / "PolicyMemo-exclusion-audit-all-277-v0.5-2026-11-09.csv")
    d_qa = records(root / "PolicyMemo-Search-D-exclusion-QA25-v0.6-2026-11-09.csv")
    d_duplicates = records(root / "PolicyMemo-Search-D-duplicate-audit-2026-11-09.csv")
    ids = [r["RecordID"] for r in combined]
    dois = [doi(r["DOI"]) for r in combined if doi(r["DOI"])]
    missing = [r["RecordID"] for r in combined if not r.get("Abstract", "").strip() or
               "no abstract available" in r.get("Abstract", "").lower()]
    assert len(kept) == len(combined) == 1018
    assert sum(duplicate_counts.values()) == 78
    assert duplicate_counts["D"] == len(d_duplicates) == 16
    assert len(ids) == len(set(ids)) and len(dois) == len(set(dois))
    assert len(excluded_ac) == 277
    assert len(d_qa) == 25
    assert len(missing) == 5
    d_new = [r for r in combined if r["SearchDFlag"] == "New unique Search D record"]
    assert len(d_new) == 255
    d_excluded = sum(r["SearchDDecision"] == "Provisional exclude" for r in d_new)
    assert d_excluded == 132
    print("PASS: original hits=1096; duplicate hits=78; unique=1018")
    print("Duplicates by search:", dict(duplicate_counts))
    print("A-C proposed exclusions=277; D proposed exclusions=132")
    print("Missing abstracts:", ", ".join(missing))
    print("A-C human-protected decisions:",
          sum(r["V05ResearcherDecisionProtected"] == "Yes" for r in combined))
    print("All initial screening classifications remain PROVISIONAL.")
    print("This check does NOT validate whether individual inclusion/exclusion choices are right.")

if __name__ == "__main__":
    main()
