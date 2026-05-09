#!/usr/bin/env python3
"""Classify 703 repos into 5 macro / 23 sub categories.
Rule-based on desc + topics + name. Reports unclassified for manual review.
"""
import json, re
from collections import Counter, defaultdict

IN = "/Users/vivien/wiki-projects/projects/research/_raw_6m/repos.jsonl"
OUT = "/Users/vivien/wiki-projects/projects/research/_raw_6m/classified.jsonl"

CATS = [
    # (code, name, [(weight, regex)]). First high-weight match wins; ties → highest score.
    ("A1", "agent-harness-cli", [
        (3, r"\b(claude code|claude-code|codex cli|gemini cli|opencode|openclaw|openagent|cursor agent|qoder|kiro|kilo|antigravity|hermes-agent|claw-code|picoclaw|openclaude|symphony|oh-my-)\b"),
        (3, r"\b(harness|cli agent|coding agent cli|terminal agent|agent harness|agent platform|agents platform|managed agents|agent CLI|agent loop|autonomous coding agent)\b"),
        (3, r"\b(personal ai assistant|ai assistant.{0,20}any (os|platform))\b"),
        (3, r"\bautonomous (ai|coding) agent\b"),
        (3, r"\b(your.{0,10}(coding|ai) (assistant|agent)|run anywhere.{0,30}(use|model))\b"),
        (3, r"\bagent[- ]native\b"),
        (3, r"\b(isolated|autonomous) (implementation|execution) runs?\b"),
        (2, r"\bopen[- ]source.{0,30}agent (cli|harness|loop)\b"),
        (2, r"^[\w-]*claw[\w-]*$"),
        (2, r"runs anywhere.{0,20}uses anything"),
    ]),
    ("A2", "coding-agent-ide", [
        (3, r"\b(cursor|replit|devin|copilot|aider|sweep|continue\.dev|qwen code)\b"),
        (3, r"\bcoding (assistant|agent)\b"),
        (3, r"\bvibe coding\b|vibe-coding"),
        (3, r"\b(phone agent|mobile agent|android agent|ios agent|autoglm)\b"),
        (3, r"\b(generative ui|ui (framework|generation).{0,20}agent)\b"),
        (2, r"\bdev environment\b.*\bagent\b"),
    ]),
    ("A3", "agent-protocol", [
        (3, r"\b(MCP|model context protocol|model-context|ACP|agent client protocol|A2A|agent-to-agent)\b"),
        (3, r"\bagent protocol\b"),
        (2, r"\b(mcp server|mcp-server)\b"),
    ]),
    ("A4", "agent-memory", [
        (3, r"\b(memory|memo|recall) (system|engine|store|backend)\b"),
        (3, r"\b(agent|llm) memory\b"),
        (2, r"\b(longmem|mempalace|mem0|rememberer|engram|m_flow|agentmemory)\b"),
        (2, r"\bpersistent memory\b"),
    ]),
    ("A5", "sandbox-runtime", [
        (3, r"\b(sandbox|microvm|container|execution environment)\b.*\bagent\b"),
        (3, r"\b(agent|ai) sandbox\b"),
        (3, r"\b(virtual filesystem|vfs).*\bagent\b"),
        (2, r"\b(NemoClaw|cubesandbox|safehouse|zeroboot|mirage)\b"),
    ]),
    ("A6", "inference-serving", [
        (3, r"\b(inference engine|local inference|serving|llama\.cpp|vllm|tensorrt|gguf|quantization)\b"),
        (3, r"\b(deepseek|kimi|qwen|llama)\b.*\b(inference|engine|local)\b"),
        (2, r"\b(metal|cuda|on-device|local llm)\b"),
        (2, r"\bllm.*\b(inference|router|proxy)\b"),
    ]),

    ("B1", "skills-collection", [
        (4, r"\b(awesome.{0,4}skills|skill collection|skill library|skills bundle|skills pack|installable skills|skills catalog|catalog.{0,10}skills)\b"),
        (4, r"\b(claude skills?|claude-code skills?|agent skills?|knowledge[- ]work plugins?)\b"),
        (4, r"^[\w.-]*skills?$"),
        (4, r"\bdistill .{0,30}(thinks?|思维|mind|认知|cognition)|蒸馏.{0,15}思维|思维方式"),
        (3, r"/skills?$|-skills?$|skills/skills"),
        (3, r"\b1[,]?\d{3}\+? skills?\b|\b\d{3}\+? skills?\b"),
        (3, r"\bskills (for|catalog|directory|marketplace|library)\b"),
        (3, r"\b(persona|colleague|coworker|nuwa|女娲|话术|张雪峰|p8 级|pua) skill\b"),
        (3, r"\b(skill\b.{0,30}(persona|character|role)|(persona|character) skill)"),
        (2, r"\bSKILL\.md\b"),
    ]),
    ("B2", "claude-md-config", [
        (4, r"\b(CLAUDE\.md|claude\.md|AGENTS?\.md|cursor rules|\.cursorrules|cursor\.json)\b"),
        (3, r"\b(claude code (config|setup|configuration|setup-and-best-practices)|coding agent setup)\b"),
        (3, r"\b(prompt|context) engineering\b"),
        (2, r"\b(meta-prompt|super prompt|opinionated config)\b"),
    ]),
    ("B3", "design-md-system", [
        (4, r"\b(DESIGN\.md|design\.md|design-md|design system|design tokens)\b"),
        (3, r"\b(design (skill|spec|systems?))\b"),
        (2, r"\b(brand|figma)\b.*\bagent\b"),
    ]),
    ("B4", "prompt-library", [
        (3, r"\b(prompt (library|collection|gallery|book|guide)|awesome prompts?)\b"),
        (3, r"\b(midjourney|gpt-image|nano banana|seedance|sora) prompts?\b"),
        (2, r"\b(prompts?|提示词)\b.*\b(collection|library|集合|合集)\b"),
    ]),
    ("B5", "awesome-list", [
        (3, r"^awesome[- ]"),
        (3, r"\bawesome (list|collection)\b"),
        (2, r"\bcurated (list|collection)\b"),
    ]),

    ("C1", "design-canvas-app", [
        (3, r"\b(open[- ]design|claude design|canvas|design (tool|editor|generator)|figma alternative)\b"),
        (3, r"\b(slide|deck|ppt|pptx|powerpoint|presentation|幻灯片) (generator|builder|maker|skill|app|application)\b"),
        (3, r"\b(ppt|deck|slides|pptx|powerpoint|短剧|drama|poster|海报|地图海报) (master|gen|生成)\b"),
        (3, r"\b(map[- ]?to[- ]?poster|nano banana.{0,10}(ppt|slide|deck)|ai ppt|vibe ppt|ai short[- ]?form video)\b"),
        (2, r"\b(design app|web designer|landing page generator)\b"),
    ]),
    ("C2", "creator-content", [
        (3, r"\b(content (creator|generation)|video editor|youtube|podcast|tiktok|xiaohongshu|reddit|twitter|substack|短剧|drama production)\b"),
        (3, r"\b(social media|short form|reel|shorts|short[- ]drama) (agent|tool|generator|production)\b"),
        (3, r"\b(screen recor|recording.{0,20}without editing|green screen)\b"),
        (3, r"\b(写作|polish|polishing|elevate.{0,20}writing|ai .{0,15}writing)\b"),
        (2, r"\b(creator|kol|influencer) (tool|kit)\b"),
    ]),
    ("C3", "coding-workflow-orchestration", [
        (3, r"\b(multi[- ]agent (orchestrat|company|team|squad)|agent (orchestration|swarm|company|team))\b"),
        (3, r"\b(zero[- ]human|autonomous) (company|business|startup|companies)\b"),
        (3, r"\b(career[- ]ops|job search|resume|hiring)\b"),
        (3, r"\b(swarm intelligence|swarm (engine|model)|crew|squad of agents)\b"),
        (3, r"\b(agent loop|autonomous (loop|workflow)|agent (council|board))\b"),
        (2, r"\b(workflow|orchestration|automation) (system|engine|platform)\b"),
    ]),
    ("C4", "research-knowledge-work", [
        (3, r"\b(research (agent|tool|copilot|engine)|deep research|knowledge (graph|management|base)|wiki|obsidian|notion)\b"),
        (3, r"\b(autoresearch|deepresearch|paper (reading|reader|search))\b"),
        (3, r"\b(news|stock|market) (intelligence|analysis|aggregat|dashboard)\b"),
        (3, r"\b(ai.{0,10}(news|brief|digest)|news aggregat)\b"),
        (3, r"\b(meeting|note[- ]?taking|second brain)\b"),
        (2, r"\b(arxiv|scholar|academic|literature review)\b"),
    ]),
    ("C5", "browser-web-automation", [
        (3, r"\b(browser automation|headless browser|web (scraping|automation)|web agent|browser-use|firecrawl)\b"),
        (3, r"\b(scrape|crawler|spider) (tool|engine|agent)\b"),
        (2, r"\b(playwright|puppeteer)\b.*\bagent\b"),
    ]),

    ("D1", "training-finetuning", [
        (3, r"\b(fine[- ]?tun|RLHF|GRPO|DPO|PPO|RL training|post[- ]training|reward model)\b"),
        (3, r"\b(unsloth|axolotl|trl|peft|lora|qlora)\b"),
        (2, r"\bdistillation|reasoning training\b"),
    ]),
    ("D2", "model-architecture", [
        (3, r"\b(deepseek|kimi|qwen|llama|mistral|gemma|claude|gpt|grok|nemotron|nanochat)\b\d"),
        (3, r"\b(foundation model|world model|reasoning model|code model)\b"),
        (3, r"\b(architecture|reproduce|reimplementation|first[- ]principles)\b.*\b(LLM|transformer|model)\b"),
        (2, r"\b(MoE|mixture of experts|sparse|reasoning)\b"),
    ]),
    ("D3", "media-gen", [
        (3, r"\b(image (generation|gen)|text[- ]to[- ]image|text[- ]to[- ]video|text[- ]to[- ]speech|tts|stt|voice clon|video gen)\b"),
        (3, r"\b(stable diffusion|sora|seedance|hyperframes|veo|kling|moss-tts|voxcpm)\b"),
        (2, r"\b(audio|music|speech|voice|tts) (model|engine|gen)\b"),
    ]),
    ("D4", "3d-spatial", [
        (3, r"\b(3D (foundation|model|scene|reconstruct)|spatial (intelligence|computing)|world model|gaussian splat|nerf)\b"),
        (2, r"\b(3D|spatial|scene|geometry) (generation|rebuild)\b"),
    ]),
    ("D5", "security-disclosure", [
        (3, r"\b(CVE-\d|vulnerability|disclosure|kernel exploit|LPE|0[- ]day|zero[- ]day|RCE)\b"),
        (3, r"\b(security (research|tool|harness|scanner)|red team)\b"),
        (2, r"\b(exploit|pwn|fuzzer)\b"),
    ]),

    ("E1", "education-training-material", [
        (3, r"\b(training (material|course)|course material|tutorial series|book|textbook|learn .* in)\b"),
        (3, r"\b(rust|go|python|typescript) (training|tutorial|course|learn)\b"),
        (2, r"\b(handbook|cookbook|recipes)\b"),
    ]),
    ("E2", "industrial-hardware-design", [
        (3, r"\b(keyboard|mouse|hardware design|cad|industrial design|3d print)\b"),
        (2, r"\b(electronic|circuit|pcb|firmware)\b"),
    ]),
    ("E3", "fun-utility", [
        (3, r"\b(menu bar|tray app|widget|wallpaper|screen recorder|clipboard|launcher|why is this running|status bar)\b"),
        (3, r"\b(text (measurement|layout|rendering)|font (rendering|engine))\b"),
        (2, r"\b(fun|toy|simple) (utility|tool|app)\b"),
        (2, r"\bcharming\b|\bbeautiful\b.*\bcli\b"),
    ]),
    ("E4", "legal-governance-compliance", [
        (3, r"\b(legal|law|compliance|governance|regulator|gdpr|hipaa|sox)\b"),
        (3, r"\b(legalize|policy|policies) (kit|toolkit|engine)\b"),
        (2, r"\b(audit|certif|sandbox).{0,30}(governance|policy|compliance)\b"),
    ]),
]

def classify(repo):
    text = " ".join([
        repo.get("name",""),
        repo.get("desc","") or "",
        " ".join(repo.get("topics") or []),
    ]).lower()

    scores = {}
    for code, name, rules in CATS:
        s = 0
        for w, pat in rules:
            try:
                if re.search(pat, text, re.I):
                    s += w
            except re.error:
                pass
        if s > 0:
            scores[(code,name)] = s

    if not scores:
        return [("Z", "unclassified", 0)]
    # return all scoring categories sorted desc; primary is the top
    ranked = sorted(scores.items(), key=lambda kv: -kv[1])
    return [(c, n, s) for (c, n), s in ranked]

# run
out = []
unclass = []
for line in open(IN):
    if not line.strip(): continue
    r = json.loads(line)
    cats = classify(r)
    r["categories"] = [{"code": c, "name": n, "score": s} for c,n,s in cats]
    r["primary_cat"] = cats[0][0] if cats else "Z"
    out.append(r)
    if r["primary_cat"] == "Z":
        unclass.append(r)

with open(OUT,"w") as f:
    for r in out: f.write(json.dumps(r, ensure_ascii=False)+"\n")

# stats
print(f"=== classified {len(out)} repos ===\n")

# category histogram
ch = Counter(r["primary_cat"] for r in out)
macro = defaultdict(lambda: {"n":0, "stars":0, "spd":[], "alive":0, "examples":[]})
sub = defaultdict(lambda: {"n":0, "stars":0, "spd":[], "alive":0, "examples":[]})
sub_name = {c:n for c,n,_ in [(c,n,0) for c,n,_ in [(c,n,0) for c,n,*_ in CATS]]}

# proper sub_name
sub_name = {}
for code, name, _ in CATS:
    sub_name[code] = name
sub_name["Z"] = "unclassified"

for r in out:
    p = r["primary_cat"]
    M = p[0]
    sub[p]["n"] += 1
    sub[p]["stars"] += r["stars"]
    sub[p]["spd"].append(r["stars_per_day"])
    if r.get("days_since_push", 999) <= 7: sub[p]["alive"] += 1
    if len(sub[p]["examples"]) < 3:
        sub[p]["examples"].append(f"{r['name']} ({r['stars']:,}★)")
    macro[M]["n"] += 1
    macro[M]["stars"] += r["stars"]
    macro[M]["spd"].append(r["stars_per_day"])
    if r.get("days_since_push", 999) <= 7: macro[M]["alive"] += 1

import statistics
print("=== MACRO ===")
print(f"{'M':<3} {'N':>4} {'totK★':>8} {'medSPD':>7} {'maxSPD':>7} {'alive%':>7}")
for M in sorted(macro):
    s = macro[M]
    print(f"{M:<3} {s['n']:>4} {s['stars']/1000:>8.1f} {statistics.median(s['spd']):>7.1f} {max(s['spd']):>7.0f} {s['alive']/s['n']*100:>6.0f}%")

print("\n=== SUB ===")
print(f"{'code':<4} {'sub-category':<32} {'N':>4} {'totK★':>7} {'medSPD':>7} {'alive%':>7}")
for c in sorted(sub):
    s = sub[c]
    print(f"{c:<4} {sub_name.get(c,'?'):<32} {s['n']:>4} {s['stars']/1000:>7.1f} {statistics.median(s['spd']):>7.1f} {s['alive']/s['n']*100:>6.0f}%   eg: {', '.join(s['examples'])}")

print(f"\n=== Unclassified sample ({len(unclass)}) ===")
for r in unclass[:30]:
    print(f"  {r['stars']:>6,}★ {r['name']:<40} {(r['desc'] or '')[:80]}")
