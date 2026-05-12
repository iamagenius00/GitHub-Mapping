# GitHub AI Ecosystem Maps

## 6-month map v3 (latest, recommended)

**`6month-map-v3.md`** — 2026-05-11. Same window as v1 (2025-11-09 → 2026-05-09, stars≥2000, 703 repos) but re-classified under a **multi-label** scheme: 28 labels, each repo gets 1 primary + 0–2 secondary. Surfaces composite forms (skill pack + research app, agent harness + memory, dashboard + observability) that single-label flattens.

Headline: A (Agent Infrastructure) covers 35.3% of repos, B (Skills & Prompts) covers 33.4%, A∪B covers 59.3%. D (Models & Training) covers only 4.1%.

## 6-month map v1 (single-label, earlier pass)

**`6month-map.md`** — 2025-11-09 → 2026-05-09, stars≥2000, **703 repos**, 6.24M ★ total.
5 macro categories × 23 sub-categories, citation graph, cohort decay analysis. Single-label classification (each repo belongs to exactly one category).

## 3-month map (earlier, narrower window)

- **`main.md`** — 2026-02-09 → 2026-05-09, stars≥1000, 691 repos.
- **`addendum-upstreams.md`** — 8 upstream repos created outside the 3-month window but heavily cited by repos inside it. **Now superseded by `6month-map-v3.md`** which absorbs these as proper data points.

## Data

- **`_raw/repos-6m.jsonl`** — 703 repos metadata (6-month window)
- **`_raw/classified-6m.jsonl`** — same, with category labels
- **`_raw/citations-6m.json`** — repo→repo citation graph from top 120 enriched READMEs
- **`_raw/classify-6m.py`** — rule-based classifier (24 sub-categories)
- **`_raw/final_v2.jsonl`** — 691 repos (3-month, kept for diff/audit)
- **`_raw/upstream_enriched.json`** — the 8 upstream repos
- **`_raw/classify_v3.py`** — earlier 3-month classifier
