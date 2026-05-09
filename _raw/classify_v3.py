#!/usr/bin/env python3
"""Final classification pass: add 'skills-ecosystem' and 'security' lanes."""
import json, re
from collections import Counter, defaultdict

ADD_RULES = [
    # Highest priority — security
    ("security", r"\b(cve-?\d+|kernel.?lpe|exploit|vulnerab|0day|zero.?day|page.?cache write|domain.?front|security.?harness|security.?research|sandbox.?escape|priv.?escal)\b"),
    # Skills ecosystem — anything that's a "skill" pack for Claude Code / agents
    ("skills-ecosystem", r"(\bskills?\b.*\b(claude|codex|agent|cli)\b|\b(claude.?code|agent).?skills?\b|[\.-]skill\b|/skills?\.md|skills\.sh|\bskills?\b\s*(for|marketplace|library|pack)|skill[s]?$)"),
    ("agent-memory", r"\b(memory.?palace|agent.?memory|memory.?layer|long.?term.?memory.?for.?agents|persistent memory|agent brain|memory backend)\b"),
    ("legal-tech", r"\b(legal|law|lawyer|contract|gdpr|compliance|attorney)\b"),
    ("creator-tool", r"\b(content.?creator|creator|youtube|tiktok|small.?red.?book|xiaohongshu|substack|newsletter|blog generator|video editor|screen recorder|recording app|presentation|slide.?deck|ppt|pitch.?deck|magazine)\b"),
    ("3d-spatial", r"\b(3d|nerf|gaussian.?splat|point.?cloud|scene reconstruct|foundation.?model.*3d|spatial)\b"),
]

with open("final.jsonl") as f:
    rows = [json.loads(l) for l in f]

with open("readmes.json") as f:
    readmes = json.load(f)

def reclassify(r):
    name = r["name"]
    text_blob = " ".join([
        name,
        r.get("desc", "") or "",
        " ".join(r.get("topics", []) or []),
        readmes.get(name, "")[:2000] if name in readmes else ""
    ]).lower()
    new_lanes = []
    # Try ADD_RULES first (these win if matched)
    for lane, pat in ADD_RULES:
        if re.search(pat, text_blob):
            new_lanes.append(lane)
        if len(new_lanes) >= 1:
            break
    # Keep original lanes too, deduped
    for l in r["lanes"]:
        if l not in new_lanes and l != "other":
            new_lanes.append(l)
        if len(new_lanes) >= 2:
            break
    if not new_lanes:
        new_lanes = r["lanes"][:1] if r["lanes"] else ["other"]
    r["lanes"] = new_lanes[:2]
    return r

rows = [reclassify(r) for r in rows]
with open("final_v2.jsonl", "w") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

lane_count = Counter()
lane_groups = defaultdict(list)
for r in rows:
    primary = r["lanes"][0]
    lane_count[primary] += 1
    lane_groups[primary].append(r)
for items in lane_groups.values():
    items.sort(key=lambda x: -x["stars_per_day"])
print("Primary lane v3:")
for l, c in lane_count.most_common():
    print(f"  {l:22} {c:4d}   top: {lane_groups[l][0]['name']} ({lane_groups[l][0]['stars_per_day']:.0f}/d)")
