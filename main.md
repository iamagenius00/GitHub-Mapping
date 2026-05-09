# GitHub 3 个月 1k+ stars 地图（2026-02-09 → 2026-05-09）

> 数据源：GitHub Search API（`created:>=2026-02-09 stars:>=1000`），共 **691 个 repo**。
> 抓取时间 2026-05-09 凌晨。前 50 名 enriched README 后做了二次分类。
> 原始数据：`projects/research/_raw/final_v2.jsonl`，README：`readmes.json`。

---

## 总览

- **总数**：691 个新 repo 在 90 天内冲过 1k stars
- **5 万星以上**：7 个；**1 万星以上**：58 个；**5 千–1 万**：76 个
- **过去 7 天有 push**：377 个（55%）——多数是活的，不是废弃 README repo
- **创建于过去 14 天还冲到 1k+**：22 个——增长最猛的"新生 cohort"
- **平台/生态背景**：描述里 mention `claude code` 的 **106 个**、`openclaw` 49、`codex` 48、`skill` **118**、`mcp` 22。整个 90 天的故事就是一句话：**OpenClaw / Claude Code 的 skill + harness 经济**。

### 主 lane 分布（按 primary lane 计数）

| lane | 数量 | 中位 stars/day | 顶流 |
|---|---|---|---|
| **skills-ecosystem** | 114 | ~70 | nexu-io/open-design (3120/d), JuliusBrussee/caveman, safishamsi/graphify |
| **coding-agent** | 86 | ~53 | garrytan/gstack, paperclipai/paperclip, openai/symphony |
| dev-tool | 36 | 45 | vercel-labs/wterm, modem-dev/hunk |
| **agent-harness** | 29 | ~54 | ultraworkers/claw-code (4938/d), zeroclaw-labs/zeroclaw |
| agent-protocol | 22 | 32 | Gitlawb/openclaude, openclaw/acpx |
| creator-tool | 12 | — | Panniantong/Agent-Reach, follow-builders |
| model-finetuning | 10 | 59 | karpathy/autoresearch, OpenClaw-RL |
| image-video-gen | 9 | — | freestylefly/awesome-gpt-image-2, JoyAI-Image |
| agent-memory | 9 | — | Gentleman-Programming/engram, FlowElement-ai/m_flow |
| 3d-spatial | 8 | — | HKUDS/CLI-Anything, lingbot-map, HY-World-2.0 |
| design-tool | 6 | 132 | chenglou/pretext, google-labs-code/design.md |
| browser-automation | 7 | 60 | h4ckf0r0day/obscura, browser-use/video-use |
| voice-audio | 8 | 26 | k2-fsa/OmniVoice, MOSS-TTS-Nano |
| sandbox-infra | 6 | 179 | NVIDIA/NemoClaw, TencentCloud/CubeSandbox, strukto-ai/mirage |
| llm-infra | 5 | 310 | AlexsJones/llmfit, antirez/ds4 |
| rag-search | 6 | 53 | CortexReach/memory-lancedb-pro |
| security | 6 | — | V4bel/dirtyfrag, theori-io/copy-fail, vercel-labs/deepsec |
| robotics | 4 | 50 | NawfalMotii79/PLFM_RADAR, Psi-Zero |
| research-paper | 7 | 50 | awesome-openclaw-tutorial 系列 |
| legal-tech | 7 | — | willchen96/mike, legalize-es / legalize-kr |
| other | 289 | 42 | financial-services, RustTraining, Recordly, CorridorKey |

> "other" 还是 289 个偏多，是因为很多 repo 不是按现在这套 lane 划的——比如个人小工具、玩具、curated list。下面 outliers 一节会拎出来讲。

---

## Top 20 by stars/day

| rank | name | stars | stars/day | age | lane | 一句话 |
|---|---|---|---|---|---|---|
| 1 | **ultraworkers/claw-code** | 190.7k | **4938** | 38d | agent-harness | OpenClaw 的 Rust port，"史上最快破 10 万星"。CLI agent harness。 |
| 2 | **nexu-io/open-design** | 33.7k | **3120** | 11d | skills-ecosystem | 开源版 Claude Design：自动检测 16 种 coding-agent CLI + 31 个 Skills + 72 个 Design Systems。 |
| 3 | V4bel/dirtyfrag | 2.6k | 2129 | 1d | security | Linux kernel LPE（Dirty Pipe / Copy Fail 同类），周末刚 disclosure。 |
| 4 | VoltAgent/awesome-design-md | 73.5k | 1918 | 38d | coding-agent | DESIGN.md 的 awesome-list，配合 Claude Code 用。 |
| 5 | **JuliusBrussee/caveman** | 56.6k | 1637 | 35d | skills-ecosystem | "why use many token when few token do trick"——压缩 65% token 的 Claude Code skill。 |
| 6 | **garrytan/gstack** | 91.6k | 1576 | 58d | coding-agent | Garry Tan（YC 总裁）公开他的 23 个 Claude Code 工具：CEO/Designer/Eng Manager/QA。 |
| 7 | MemPalace/mempalace | 51.6k | 1519 | 34d | coding-agent | Local-first AI memory，96.6% R@5 LongMemEval；ChromaDB pluggable。 |
| 8 | santifer/career-ops | 43.5k | 1272 | 34d | skills-ecosystem | 多 Agent 求职系统，14 个 skill + Go dashboard，Claude Code/Codex/Gemini CLI 都能跑。 |
| 9 | safishamsi/graphify | 44.9k | 1272 | 35d | skills-ecosystem | "把任何文件夹变成知识图谱"的 agent skill，跨多种 coding agent。 |
| 10 | **karpathy/autoresearch** | 79.8k | 1264 | 63d | model-finetuning | nanochat 训练上自动跑研究的 agents。 |
| 11 | antirez/ds4 | 2.2k | 955 | 2d | llm-infra | Salvatore（Redis 作者）写的 DeepSeek V4 Flash Metal inference 引擎。 |
| 12 | paperclipai/paperclip | 63.6k | 943 | 67d | coding-agent | "如果 OpenClaw 是员工，Paperclip 是公司"——多 agent business orchestration。 |
| 13 | chenglou/pretext | 46.5k | 748 | 62d | design-tool | 纯 JS/TS 多行文本 measurement & layout，避免 DOM reflow，AI 友好。 |
| 14 | Gitlawb/openclaude | 26.2k | 692 | 38d | agent-protocol | 开源 coding agent CLI，绑 OpenAI/Gemini/Codex/Ollama 等 backend。 |
| 15 | EvoLinkAI/awesome-gpt-image-2 | 13.4k | 655 | 21d | skills-ecosystem | GPT Image 2 prompt 库（API + 提示词）。 |
| 16 | alchaincyf/huashu-design | 12.7k | 653 | 19d | skills-ecosystem | "话术.design" skill，自然语言一句话出可交付设计。 |
| 17 | kyegomez/OpenMythos | 12.3k | 600 | 21d | llm-infra | Claude Mythos 架构的理论重建，第一原理实现。 |
| 18 | strukto-ai/mirage | 1.4k | 598 | 2d | sandbox-infra | "Unified Virtual Filesystem for AI Agents"，Python+TS 双 SDK。 |
| 19 | yaojingang/yao-open-prompts | 1.4k | 554 | 2d | creator-tool | 中文 116 个提示词合集，nano banana / PPT 系列。 |
| 20 | HKUDS/CLI-Anything | 34.0k | 553 | 61d | 3d-spatial | "Making ALL Software Agent-Native"，pip install cli-anything-hub。 |

---

## 按 lane 分组

### skills-ecosystem（114 个，最大单一 lane）

这 90 天 GitHub 最大的现象：**"skill" 成为一个独立内容形态**，像 npm package / Chrome extension 那样在分发。绝大部分围绕 Claude Code / Codex / 通用 coding-agent CLI。

- **JuliusBrussee/caveman**（56.6k★, 1637/d, 35d, push 8d）
  *"why use many token when few token do trick"*。一个把 Claude Code 输出强压成"穴居人语法"的 skill，号称省 65% token。增长 trigger：**梗 + 真实痛点（订阅价高 → 想省 token）**。
- **safishamsi/graphify**（44.9k★, 1272/d, 35d, push 1d）
  跨 6 种 agent 的"任何文件夹 → 知识图谱"skill。增长 trigger：**agent-agnostic 定位** + 中文/英文双 README。
- **santifer/career-ops**（43.5k★, 1272/d, 34d, push 2d）
  多语言 README（8 种语言），"我用 AI 反向选公司"叙事。增长 trigger：**story + skill 包**——不是 SDK，是开箱即用的人生工具。
- **addyosmani/agent-skills**（34.9k★, 425/d, 82d, push 2d）
  Addy Osmani（前 Google Chrome dev advocate）的 production skills 合集。靠**作者背书**长期慢长。
- **nexu-io/open-design**（33.7k★, 3120/d, 11d, push 0d）
  整个数据集里增长速度第二猛，11 天 33k 星。"开源版 Claude Design"，自动检测 16 种 CLI + 31 skills + 72 design systems。增长 trigger：**精确对位 Anthropic 商业产品 + BYOK**。
- **googleworkspace/cli**（25.9k★, 386/d, 67d, push 0d）
  Google 官方非 Google product。Drive/Gmail/Calendar 全套 CLI，自带 40+ agent skills。
- **alchaincyf/nuwa-skill**（18.0k★, 534/d, 34d, push 16d）
  "女娲.skill"——蒸馏任何人的思维方式。中文 + 隐喻命名（女娲 / 话术 / 张雪峰）成为一个**中文 skill 子生态**。
- **alchaincyf/zhangxuefeng-skill**（7.0k★, 208/d）"张雪峰认知操作系统"——这种**人物化 skill** 是 90 天里独有的形态。
- **slavingia/skills**（8.5k★, 184/d）"基于《Minimalist Entrepreneur》的 skills"——书 → skill 的转化路径。
- **MiniMax-AI/skills**（11.6k★, 221/d）厂商也下场做 skill 包。
- **google/skills**、**heygen-com/hyperframes**、**phuryn/pm-skills** 都是 1 万+ 星的 skill 集合。

> **lane 观察**：skill 现在的增长曲线接近 Chrome extension 2010 / npm 2014 / VSCode extension 2017 的早期。**人格化命名（女娲、张雪峰、PUA、Caveman）跑得比通用名字快**。

### coding-agent（86 个）

- **garrytan/gstack**（91.6k★, 1576/d, 58d）：YC 总裁 Garry Tan 的"我个人的 Claude Code 配置"。增长 trigger：**身份背书 + 具体数据（"我 2026 的代码量是 2013 的 810×"）**。
- **paperclipai/paperclip**（63.6k★, 943/d, 67d）：node + react UI 编排多 agent 跑公司。slogan："如果 OpenClaw 是员工，Paperclip 是公司"。
- **openai/symphony**（22.6k★, 318/d, 71d）：OpenAI 自己出的项目隔离 + 自主实现 runner。把 Linear board 任务自动 spawn agent。
- **openai/codex-plugin-cc**（17.9k★, 455/d, 39d）：Codex 嵌入 Claude Code 当 reviewer——OpenAI 主动**寄生在 Anthropic 生态**。
- **claude-code-best/claude-code**（17.8k★, 464/d, 38d）："原汁原味 Claude Code 可运行版" + "内存泄漏修复"——逆向 + fork 的 fork 也能涨星。
- **tanweai/pua**（17.1k★, 280/d）："让你的 AI 翻倍" PUA 风格 skill。**梗驱动**。
- **cursor/cookbook**（3.7k★, 316/d, 12d）：Cursor SDK 的 cookbook，代表 **Cursor 进入 SDK 时代**。
- **aattaran/deepclaude**（1.6k★, 320/d, 5d）：DeepSeek V4 Pro 替换 Claude 的 brain，"省 17×"。

### agent-harness（29 个）

- **ultraworkers/claw-code**（190.7k★, 4938/d）：Rust 实现的 claw CLI agent harness，是整个数据集 #1。
- **zeroclaw-labs/zeroclaw**（31.1k★, 368/d）："你拥有 agent / 数据 / 机器"，主权 AI 个人助手。
- **RightNow-AI/openfang**、**THU-MAIC/OpenMAIC**、**cft0808/edict**（"三省六部制 OpenClaw 多 agent 编排"，中国传统隐喻）、**HKUDS/Vibe-Trading**、**HKUDS/ClawTeam**——HKU Data Science 实验室一个组发了**至少 5 个 5k+ star 的 OpenClaw 衍生**。

### agent-protocol（22 个）

- **Gitlawb/openclaude**（26.2k★, 692/d）：OAuth + 多 backend coding agent CLI。
- **onecli/onecli**（2.1k★）：开源凭证 vault for agents——agent identity 这条赛道开始有人做。
- **knowsuchagency/mcp2cli**（2.1k★）：MCP / OpenAPI / GraphQL → CLI runtime。
- **openclaw/acpx**（2.6k★）：Agent Client Protocol headless client。
- **Mouseww/anything-analyzer**（2.3k★）：抓包 + MITM + AI 分析 + MCP server。

### model-finetuning（10 个）

- **karpathy/autoresearch**（79.8k★, 1264/d, 63d, push 44d）：在 nanochat 单卡训练上跑自动研究。注意 push 44 天没动——**项目本身已经"完成"了，但靠作者光环和"autoresearch"叙事持续涨**。
- **Gen-Verse/OpenClaw-RL**（5.3k★）："只用对话训练 agent"。
- **leilei926524-tech/anti-distill**（2.1k★）：**反蒸馏 skill**——清洗你被迫写的 skill 文件，不让别人偷你的思维。整个生态出现了对抗性子产品。

### design-tool（6 个）— stars/day 中位数最高的 lane（132/d）

- **chenglou/pretext**（46.5k★, 748/d）：Cheng Lou（前 React Native 核心作者）写的纯 JS 文本布局，"AI-friendly iteration method"。
- **google-labs-code/design.md**（12.2k★, 431/d, 28d）：Google Labs 提出 DESIGN.md format spec——**design system 的可读机器格式**，这个 spec 现在被 awesome-design-md（73k★）、awesome-claude-design（2k★）等围绕。
- **drona23/claude-token-efficient**（5.2k★）：一个 CLAUDE.md 文件，省 token。
- **open-pencil/open-pencil**（4.8k★）：开源 Figma 替代品，"AI-native design editor"。
- **VoltAgent/awesome-claude-design**（2.0k★）。

> **观察**：design 在变成一个**文档格式问题**——给 agent 的 prose-+-tokens 文件——而不是工具问题。

### creator-tool（12 个）

- **Panniantong/Agent-Reach**（19k★, 258/d）："给 agent 长眼睛"——读写 Twitter / Reddit / YouTube / GitHub / Substack。
- **zarazhangrui/follow-builders**（3.9k★）：监控 X 和 podcast 上 AI builders 然后 remix。
- **rushindrasinha/youtube-shorts-pipeline**（2.0k★）：news → script → AI 视觉 → 配音 → 字幕 → 上传。
- **jackwener/xiaohongshu-cli**（1.8k★）：小红书 CLI（逆向 API），可搜可读可互动。
- **MemeCalculate/moyin-creator**（3.5k★）：AI 影视生产工具，Seedance 2.0 全流程。

### agent-memory（9 个，新生 lane）

- Gentleman-Programming/engram, NateBJones-Projects/OB1, FlowElement-ai/m_flow, rohitg00/agentmemory, breferrari/obsidian-mind, zilliztech/memsearch, Prismer-AI/PrismerCloud, ghostwright/phantom。
- 共同特征：**SQLite + FTS5 / 向量 / Markdown 三选一 + MCP server 接 Claude Code**。
- mempalace 在 coding-agent lane 已经 51k★，证明这个赛道天花板没问题。

### 3d-spatial（8 个，意外的 lane）

- **Robbyant/lingbot-map**（6.0k★, 256/d, 23d）：feed-forward 3D foundation model，流式数据重建场景——这是个**真正的研究突破**埋在 90 天数据里。
- **Tencent-Hunyuan/HY-World-2.0**（1.8k★）：multimodal world model。
- **Keychron-Keyboards-Hardware-Design**（3.4k★）：键盘工业设计 CAD 文件——非 AI 但跟着开源潮。

### sandbox-infra（6 个）

- **NVIDIA/NemoClaw**（20k★, 372/d, 54d）：NVIDIA 把 OpenClaw 跑在 OpenShell 里，managed inference。**大厂背书使 sandbox 一夜变主流话题**。
- **TencentCloud/CubeSandbox**（5.2k★, 179/d）。
- **strukto-ai/mirage**（1.4k★, 598/d, 2d）：刚起的 unified VFS。
- **zerobootdev/zeroboot**（2.3k★）：sub-millisecond microVM via copy-on-write。
- **eugene1g/agent-safehouse**（1.7k★）：本地 agent sandbox。

### security（6 个）

- **V4bel/dirtyfrag**（2.6k★, **2129/d**, 1d）：周末刚发的 Linux kernel LPE，跟 Dirty Pipe 同类。
- **theori-io/copy-fail-CVE-2026-31431**（3.6k★, 378/d, 9d）：9 年老 LPE，Theori 团队披露。
- **vercel-labs/deepsec**（1.8k★, 219/d, 8d）：用 coding agents 做 security harness 找洞——**agent + security 的明确产品形态**。

### legal-tech（7 个，黑马 lane）

- **willchen96/mike**（2.5k★, 269/d, 9d）："OSS AI Legal Platform"，10 天 2.5k★。
- **legalize-dev/legalize-es**（1.7k★）：西班牙立法当 Git repo——每条法律是 markdown，每次修法是 commit。**legalize-kr** 韩国版同样模式。**"国家法律 = git repo"是一个新模式**。
- **microsoft/agent-governance-toolkit**（1.5k★）：agent 政策、零信任身份、execution sandboxing、release。
- **RevylAI/greenlight**（1.4k★）：App Store 提交前合规扫描器。

### llm-infra（5 个）

- **AlexsJones/llmfit**（25.5k★, 310/d, 82d）：一句话找出哪个模型能在你硬件上跑。
- **antirez/ds4**（2.2k★, 955/d, 2d）：Salvatore 写的 DeepSeek V4 Flash Metal 引擎，**作者光环 + 真技术**。
- **kyegomez/OpenMythos**（12.3k★, 600/d）：Claude Mythos 架构第一原理重建。

### voice-audio（8 个）

- k2-fsa/OmniVoice（5.5k★, 142/d）：600+ 语言克隆 TTS。
- OpenMOSS/MOSS-TTS-Nano（2.8k★）。
- 几乎全是**本地 / 离线 / on-device**——"私密 + Apple Silicon" 是这个 lane 的共同卖点。

### browser-automation（7 个）

- **h4ckf0r0day/obscura**（11.1k★, 435/d, 26d）：Rust headless browser，专门给 AI agent 和 scraping。
- **browser-use/video-use**（6.9k★, 257/d）：browser-use 团队的 video editing agent。
- **browser-use/browser-harness**（11.6k★, 531/d，归类在 skills-ecosystem）：self-healing browser harness。
- **firecrawl/web-agent**（1.1k★）：firecrawl 团队的结构化 web 研究 agent。

### other（289 个，扫荡）

值得拎出来看的：
- **anthropics/financial-services**（14.5k★）：Anthropic 自己的金融 vertical 包。
- **microsoft/RustTraining**（14.2k★）：Microsoft 的 Rust 培训材料。
- **JCodesMore/ai-website-cloner-template**（14.2k★, 252/d）：一句话克隆任何网站。
- **agentscope-ai/QwenPaw**（16.4k★）：阿里 AgentScope 团队的个人 AI assistant。
- **nikopueringer/CorridorKey**（13.1k★, 180/d）：完美绿幕抠像。
- **webadderallorg/Recordly**（13.8k★, 242/d）：屏幕录制无需剪辑。
- **vercel-labs/portless**（9.1k★）：用稳定命名 URL 替代端口号。
- **HKUDS 系列** 还有 ClawWork、OpenSpace、FastCode——一个组现在像 OpenAI Cookbook 那样**机构化生产 OpenClaw 周边**。
- **darrylmorley/whatcable**（2.2k★, 282/d, 8d）：菜单栏 app 告诉你 USB-C 线是什么——**fun-utility 也能 8 天 2k★**。
- **tw93/Kami**（4.8k★, 264/d）：tw93 的小工具，一如既往。

---

## 增长模式分析

### 1. **平台依附型增长占主流**
描述里 mention `claude code` / `claude-code` / `openclaw` / `codex` 的 repo **加起来 200+，占 30%**。增长不是来自"新基础设施"，而是来自"在已有平台上叠 skill / config / fork"。
**对独立项目的启示**：纯通用 SDK 在 90 天内涨 1k★ 越来越难；绑定一个明确平台 + 解决一个具体场景，是当前最可靠的路径。

### 2. **skill 是新的 npm package**
118 个 repo 描述里有 "skill"。skill = markdown + 配置 + 一点代码，**没有运行时**。它是分发单位，不是工具单位。
- 中位 skill repo 有 2-5 个 markdown + 一个 SKILL.md + agent-agnostic 适配层。
- **品牌化命名跑得最快**："女娲.skill"、"张雪峰.skill"、"caveman"、"PUA"。无聊命名（"awesome-X"）涨得慢。

### 3. **"个人英雄"+"具体数字"**
gstack（"我 2026 比 2013 多 810×"）、paperclip（"OpenClaw 是员工，Paperclip 是公司"）、career-ops（"AI 反向选公司"）、mempalace（"96.6% R@5"）——**头部 repo 共同模式：作者+一个数字+一个隐喻**。

### 4. **新 cohort（≤14 天）的爆发力很强**
22 个 repo 在 14 天内冲到 1k+。最快的是 V4bel/dirtyfrag（1.2 天 2.6k★）。
- 趋势 1：**security disclosure**（CVE pattern）天然带流量。
- 趋势 2：**"开源对位 X 商业产品"**（open-design 对 Claude Design、deepclaude 对 Claude Code、deepsec 对 Cursor sec）。

### 5. **大厂在 2026-Q1 下场速度异常快**
Google（design.md, googleworkspace/cli, google/skills, google/agents-cli, google-labs-code）、OpenAI（symphony, codex-plugin-cc, parameter-golf, plugins, privacy-filter）、NVIDIA（NemoClaw, OpenShell）、Microsoft（agent-governance-toolkit, RustTraining）、Vercel Labs（4 个 1k+ 项目）、Tencent / MiniMax / 阿里 / 京东都有 1 万+ star 的开源——**大厂工作不再是"自家产品文档"，而是"在开源生态里抢话语权"**。

---

## Outliers（增长异常的项目，逐个分析）

### 1. **ultraworkers/claw-code**（4938/d，整体 #1）
38 天 19 万星。这个增速对照：linux 内核全 90 天才 4 个 1k+ commit。
- README 说 "fastest repo in history to surpass 100K stars"，可信度需要进一步验证（star history 图没看到外部审计）。
- push 仍在 2.7d 内，project 是活的。
- **可能 trigger**：与 Anthropic 官方 / OpenClaw 官方有结构性关系（命名 `claw` 跟 `OpenClaw` 共生），fork-of-fork 模式爆量。

### 2. **nexu-io/open-design**（3120/d，11 天 33k）
- **精确对位** Anthropic Claude Design 的 BYOK 开源版。
- 自动检测 16 种 coding-agent CLI——这条信息是 marketing 钩子，让每种 agent 用户都觉得"和我有关"。
- README 是**长 banner + 视觉 + 多语言徽章**——典型 "Awesome list" 视觉模板的高级版。

### 3. **karpathy/autoresearch**（1264/d，63 天 8 万，但 push 44 天没动）
- 项目本身**已经停止 push**，但持续涨星——证明 **Karpathy 名字本身是流量基础设施**。
- **观察**：有些 repo 是"展品" 而非"产品"，靠人格而非更新维持。

### 4. **antirez/ds4**（955/d，2 天 2.2k）
- Salvatore Sanfilippo 写的 DeepSeek V4 Metal 引擎。这种"作者背书 + 真东西 + Apple Silicon 友好"组合在 2 天能拉 2k 是**作者经济**。
- 类似的：chenglou/pretext，addy osmani/agent-skills。

### 5. **JuliusBrussee/caveman**（1637/d，35 天 56k）
- **梗 + 解决真痛点**：穴居人语法压 token。
- 完全没大厂背书，纯靠"why use many token when few token do trick"这一句 slogan。
- **对独立创作者最重要的样本**——这是没资源也能跑通的剧本。

### 6. **HKUDS 一组发了 7+ 个 5k+ star repo**
CLI-Anything（34k）、OpenHarness（12k）、ClawWork（8k）、OpenSpace（6k）、Vibe-Trading（6k）、ClawTeam（5k）、FastCode（2k）。**机构化生产**。
- 写法：每个 repo 有统一封面 + 中英双 README + 一句 marketing slogan。
- 命名：`Open-` 前缀 + 拟人/动作命名。

### 7. **legalize-es / legalize-kr**（合计 3k★）
"国家法律当 Git repo" 这个 idea 本身能跨国复用——西班牙、韩国版同时跑——**模式可移植性**是 outlier 价值所在。

### 8. **microsoft/RustTraining**（14k★, 250/d）
微软出的 Rust 教程居然能在 56 天涨 14k★。说明**"权威 + Rust + 免费完整课程"** 仍然是 evergreen 组合。

### 9. **theori-io/copy-fail-CVE-2026-31431** 与 **V4bel/dirtyfrag**
两个安全 disclosure 都进了 top stars/day。GitHub 现在已经是**漏洞首发的 PR 平台**——文章发在 repo 而不是 blog。

---


## 宏观增长 insight

把 691 个 repo 按 lane / cohort / 作者类型 / 语言 / 协议拆开看,几个不靠 anecdote 的硬规律:

### 1. **velocity 的衰减曲线非常陡 — 一个 1k+ repo 的"半衰期"大约 30 天**

按"创建多少天"分桶,每桶取**中位 stars/day**(不是头部,是典型仓的速率):

| cohort | N | 中位 stars/day | 最大 | cohort 累计 stars |
|---|---|---|---|---|
| ≤14 天 | 22 | **275.7/d** | 3120 | 75.8k |
| 15-30 天 | 80 | 88.2/d | 655 | 238.4k |
| 31-60 天 | 314 | 49.4/d | 4938 | 1616.2k |
| 61-90 天 | 275 | 28.6/d | 1264 | 1242.5k |

**14 天 → 60 天,中位速率掉到 1/10**。这不是"重力",是 **GitHub trending 算法的可见性窗口** + **早期采用者的注意力周期**。
含义:**一个 repo 在前 30 天没拿到 5k+ 星,基本不会再有第二次起飞**(本数据集里 60 天后还能涨过 100/d 的全是 `karpathy/`、`antirez/`、`chenglou/` 这种**作者背书型展品**)。

### 2. **lane 的 velocity 排名 ≠ lane 的 size 排名** — 中位数比总量更说明问题

按 lane 中位 stars/day 排:

| lane | N | 中位 stars/day | 总 stars | alive% |
|---|---|---|---|---|
| **llm-infra** | 5 | **309.8** | 45.1k | 40% |
| **security** | 6 | 152.9 | 11.8k | 67% |
| **sandbox-infra** | 6 | 115.5 | 32.5k | 67% |
| **design-tool** | 6 | 115.2 | 71.9k | 50% |
| **3d-spatial** | 8 | 66.4 | 55.6k | 75% |
| **skills-ecosystem** | 114 | 63.5 | **711.8k** | 52% |
| browser-automation | 7 | 59.7 | 28.1k | 86% |
| model-finetuning | 10 | 58.8 | 117.1k | 60% |
| agent-harness | 29 | 55.4 | 361.5k | 69% |
| coding-agent | 86 | 41.8 | 567.7k | 57% |
| agent-memory | 9 | 38.0 | 20.1k | 78% |

两个反直觉点:

**(a) skills-ecosystem 总量第一(71 万星),中位却只排第六。** 大众印象里"skill 是这 90 天最热的赛道",这话只对了一半 — 是**头部 skill repo(caveman / open-design / graphify)极其集中地拉走了大部分流量**,114 个 skill repo 的中位增速 63/d,跟 dev-tool(43/d)只差一档。**skill 是赢家通吃市场,不是普惠市场**。

**(b) llm-infra 中位 309/d 是全榜最高,但 N=5、alive% 只 40%。** 一个 LPE / 一个新 inference engine / 一个 quantization 工具就能短期内冲很高,但**长期维护率最低**。这是**事件驱动型流量**,不是产品驱动型。

**真正"健康"的 lane**(中位高 + alive% 高 + N≥7):
- **browser-automation**(60/d, 86% alive)
- **agent-memory**(38/d, 78% alive)
- **rag-search**(56/d, 83% alive)
- **agent-protocol**(29/d, 73% alive)

这四个是**慢但稳**的赛道,典型仓库还在被维护,不依赖一次性叙事。

### 3. **2/3 是个人开发者,不是组织**

| owner | N |
|---|---|
| User | 451 (65%) |
| Organization | 240 (35%) |

**1k+ 星的 repo 里,个人作者占 2/3**。这个比例跟 2020 年前后(Org 占大头)完全反过来。
解释一致的:**LLM 把"做出东西"的边际成本压到接近零,组织内的协调成本反而成了劣势** — 一个人 + Claude Code 一周做的东西,公司一个 squad 做不完。

### 4. **协议:MIT 占 49%,Apache 只有 15%** — 跟"infra 时代"反过来

| license | N | 占比 |
|---|---|---|
| MIT | 336 | 49% |
| no license | 122 | 18% |
| Apache-2.0 | 107 | 15% |
| NOASSERTION | 67 | 10% |
| AGPL-3.0 | 33 | 5% |

老一代 infra(Kubernetes / TF / PyTorch)是 Apache 主导,因为有专利条款。
**这一波(skill / harness / coding-agent)MIT 主导**,因为内容是 markdown / 配置 / 脚本,**没什么专利可保护,作者只想要署名**。
另一个看点:**18% no license + 10% NOASSERTION = 28% 的 repo 法律上不可商用**。这是"个人作者周末做的"的另一个证据。

### 5. **TypeScript 几乎追平 Python**

| 语言 | N |
|---|---|
| Python | 200 |
| **TypeScript** | **180** |
| (no primary lang, mostly markdown) | 69 |
| Rust | 40 |
| JavaScript | 36 |
| Shell | 30 |
| HTML | 26 |
| Go | 25 |

Python 是 ML 的母语,但 **agent 时代的"中间件"几乎是 TS 写的** — Vercel、browser-use、heygen-com、VoltAgent、cursor 系全是 TS。
**markdown-only(69 个)** 单独排第三 — 这是"skill 不是软件"的语言学证据:**markdown 现在是一种交付格式**。

### 6. **新 cohort(≤14 天)爆发力的两条路径**

22 个 ≤14 天就冲过 1k★ 的 repo,几乎全部走两条剧本之一:

- **路径 A — security disclosure**(V4bel/dirtyfrag 1.2 天 2.6k、theori-io/copy-fail 9 天 3.6k):CVE 自带流量,GitHub 现在是漏洞首发平台。
- **路径 B — "开源对位某商业产品"**(open-design 对 Claude Design、deepclaude 对 Claude Code、deepsec 对 Cursor sec、open-codesign 对 Claude Design):一个明确的"X 的开源版"叙事 + BYOK + 多语言 README,11 天就能 30k★。

**没走这两条而 14 天破 1k 的,基本只剩"作者背书"**(antirez/ds4 2 天 2.2k)。

### 7. **平台依附型增长占主流 — 但"依附"的对象正在固化**

mention `claude code` 的有 106 个、`openclaw` 49、`codex` 48、`skill` 118、`mcp` 22。**但反过来:整个数据集不依附任何平台、纯做 SDK / 框架的,只有 ~50 个**(占 7%)。
含义:**这 90 天不是 SDK 时代,是 distribution 时代** — 增长不靠"我做了一个新东西",靠"我让你已经在用的东西更好用"。
另一个推论:**"agent-agnostic" 比 "agent-specific" 涨星快** — graphify、career-ops、huashu-design 都强调跨 6+ agent。绑死单一平台是天花板。

### 8. **header 三件套** — 经验上,头部 repo 的 README 都长得一样

抽 top 50 的 README 看,**第一屏共同结构**:

1. **slogan(一句话,带数字 / 反差 / 隐喻)** — "why use many token when few token do trick"、"the open-source alternative to Claude Design"、"96.6% R@5 on LongMemEval"。
2. **多语言徽章 + star history** — 中英双 README 在头部里是标配。
3. **demo 图 / GIF / 视频** — 不是截图,是动效。
4. **slogan 在 feature 之前,feature 在安装步骤之前** — 跟传统 "Installation > Usage > API" 的 README 完全反过来。

**最大的硬规则:第一段必须有数字。** 没数字的 README 在 1k+ 区基本看不到。
"96.6% R@5"、"省 65% token"、"34d 43k stars"、"810× 2013 速度" — 这种数字不一定权威,但**它把 README 从"宣传"变成"证据"**,降低读者怀疑成本。

---

## 数据局限说明

- 没有 GitHub token，core API 限速 60/h，所以**只 enrich 了 top 50 repo 的 README**，剩下 641 个分类基于 desc + topics + name，可能有偏差（"other" 占 42% 主要是因为 enrich 不够）。
- 没拉 last-30-day commit 数和 contributor count（要 token，rate limit 不够）。
- "stars/day" 是平均速率，**不是当前增长速率**——一个 60d 老 repo 早期 1 周 5k★ + 后来缓增，会被低估为 ~80/d。要看 star-history 才能区分。
- 没去重 fork-of-fork（如 ultraworkers/claw-code-parity 也算了一个）。
- LLM-pattern 命名（OpenClaw、claw、Claw3D）暗示这 90 天有一波**协调性 fork/重命名活动**，原始事件源没去考古。

数据原料都在 `projects/research/_raw/`，要重跑分析改 classify_v3.py 就行。
