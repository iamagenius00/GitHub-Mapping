# GitHub AI 生态 6 个月 Mapping

## 一句话总结

过去 6 个月 GitHub 上的 AI 仓库,本质是 **"在 Claude Code / OpenClaw / Codex 三家 agent harness 上叠 markdown 形态的 skill"**。703 个 2k+ 星仓库里, **191 个 (27%)** 直接是 agent 基础设施 / harness, **158 个 (22%)** 是 skill / 配置 / DESIGN.md 分发层, 只有 **26 个 (3.7%)** 真正在做模型或训练。**这不是模型时代,是 distribution 时代;不是 SDK 时代,是 markdown 时代。**

---

## 一、九大方向

> 一句话:**A** 是基础设施,**B** 是给 agent 看的指令(markdown),**C** 是 agent 帮你干的活,**D** 是模型本身,**F** 是图像/视频/语音生成,**G** 是教育与教程,**H** 是硬件,**I** 是工具(开发者周末项目),**Z** 是长尾。

| 大方向 | 中文名 | 仓数 | 总 ★ |
|---|---|---:|---:|
| **A** Agent Infrastructure | 基础设施 | **191** | 2081k |
| **B** Skills & Prompts | Skill 与提示词 | **158** | 1978k |
| **C** Vertical Applications | 垂直应用 | **102** | 1008k |
| **D** Models & Training | 模型与训练 | **26** | 100k |
| **F** Multimodal Generation | 多模态生成(图/视频/语音) | **29** | 152k |
| **G** Education & Tutorials | 教育与教程 | **37** | 184k |
| **H** Hardware | 硬件 | **9** | 50k |
| **I** Fun-Utility | 工具(开发者周末项目) | **65** | 345k |
| **Z** Long-tail | 长尾 / 未归类 | **86** | 341k |

**两个数字定调子**:

- **A+B 加起来 349 个,占 50%** —— 一半的 2k+ 星仓库是"基础设施 + 分发层"。
- **D(模型 / 训练)只有 26 个,占 3.7%** —— 这 6 个月,"做模型 / 做训练"的人在 GitHub 1k+ 区已经成了少数派。绝大部分热度被分发层(B)和基础设施(A)吸走了。
- **B 类从 90 天版的 7% 涨到 6 个月版的 22%** —— skill / CLAUDE.md / DESIGN.md 这种 markdown 形态不仅没退,反而是 6 个月里增长最猛的一类。

---

## 二、子门类详解

> 9 大方向 → 24 个细分。每一类讲清楚:**做什么 / 典型 3 个代表**。

### A. 基础设施(Agent Infrastructure)

agent 跑起来需要什么——CLI / 协议 / 内存 / sandbox / inference。**整个数据集 27% 在这一层**。

#### A1 · Agent Harness / CLI

**N=113 · 总 ★=1622k**

**做什么** · agent 的运行框架、CLI 工具——OpenClaw、Claude Code、Codex CLI 这种。整个生态的母仓。

**典型代表**
  - **openclaw/openclaw** — 370.0k★ · Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞
  - **ultraworkers/claw-code** — 190.8k★ · The repo is finally unlocked. enjoy the party! The fastest repo in history to surpass…
  - **code-yeongyu/oh-my-openagent** — 56.7k★ · omo; the best agent harness - previously oh-my-opencode


---

#### A2 · Coding Agent / IDE

**N=21 · 总 ★=128k**

**做什么** · 在 IDE / 终端里帮你写代码的 agent——AutoGLM、generative UI、各种 wrapper。

**典型代表**
  - **zai-org/Open-AutoGLM** — 25.2k★ · An Open Phone Agent Model & Framework. Unlocking the AI Phone for Everyone
  - **manaflow-ai/cmux** — 16.5k★ · Ghostty-based macOS terminal with vertical tabs and notifications for AI coding agent…
  - **vercel-labs/json-render** — 14.7k★ · The Generative UI framework


---

#### A3 · Agent Protocol

**N=12 · 总 ★=39k**

**做什么** · agent 之间怎么通信的标准——MCP server、ACP、A2A。

**典型代表**
  - **epiral/bb-browser** — 5.0k★ · Your browser is the API. CLI + MCP server for AI agents to control Chrome with your l…
  - **excalidraw/excalidraw-mcp** — 4.4k★ · Fast and streamable Excalidraw MCP App
  - **jacob-bd/notebooklm-mcp-cli** — 4.3k★ · 


---

#### A4 · Agent Memory

**N=21 · 总 ★=151k**

**做什么** · 给 agent 加记忆——向量数据库 / SQLite / markdown / vector memory 各种流派。

**典型代表**
  - **MemPalace/mempalace** — 51.7k★ · The best-benchmarked open-source AI memory system. And it's free.
  - **volcengine/OpenViking** — 23.7k★ · OpenViking is an open-source context database designed specifically for AI Agents(suc…
  - **garrytan/gbrain** — 13.9k★ · Garry's Opinionated OpenClaw/Hermes Agent Brain


---

#### A5 · Sandbox / Runtime

**N=13 · 总 ★=69k**

**做什么** · agent 跑在哪——microVM / 沙箱 / 虚拟文件系统。

**典型代表**
  - **NVIDIA/NemoClaw** — 20.2k★ · Run OpenClaw more securely inside NVIDIA OpenShell with managed inference
  - **alibaba/OpenSandbox** — 10.5k★ · Secure, Fast, and Extensible Sandbox runtime for AI agents.
  - **Lakr233/vphone-cli** — 5.9k★ · 


---

#### A6 · Inference / Serving

**N=11 · 总 ★=71k**

**做什么** · 模型怎么跑起来——本地推理引擎、serving 框架、量化工具。

**典型代表**
  - **AlexsJones/llmfit** — 25.5k★ · Hundreds of models & providers. One command to find what runs on your hardware.
  - **jundot/omlx** — 12.8k★ · LLM inference server with continuous batching & SSD caching for Apple Silicon — manag…
  - **TheTom/turboquant_plus** — 6.7k★ · 


---

### B. Skill 与提示词(Skills & Prompts)

agent 需要哪些指令、哪些规范——SKILL.md / CLAUDE.md / DESIGN.md / prompt 库。**markdown 形态的 "软件"。这一层是 6 个月里增长最猛的**。

#### B1 · Skills 集合

**N=130 · 总 ★=1606k**

**做什么** · 打包好的 SKILL.md 文件集合,装到 Claude Code / Codex 上就能用。

**典型代表**
  - **affaan-m/everything-claude-code** — 176.1k★ · The agent harness performance optimization system. Skills, instincts, memory, securit…
  - **garrytan/gstack** — 91.8k★ · Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Desi…
  - **nextlevelbuilder/ui-ux-pro-max-skill** — 75.7k★ · An AI SKILL that provide design intelligence for building professional UI/UX multiple…


---

#### B2 · CLAUDE.md / 配置文件

**N=5 · 总 ★=143k**

**做什么** · 单文件 super-prompt 或 CLAUDE.md 配置,告诉 agent 怎么干活。

**典型代表**
  - **forrestchang/andrej-karpathy-skills** — 121.1k★ · A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy…
  - **Piebald-AI/claude-code-system-prompts** — 10.1k★ · All parts of Claude Code's system prompt, 24 builtin tool descriptions, sub agent pro…
  - **drona23/claude-token-efficient** — 5.2k★ · One CLAUDE.md file. Keeps Claude responses terse. Reduces output verbosity on heavy w…


---

#### B3 · DESIGN.md 系

**N=5 · 总 ★=95k**

**做什么** · 用 markdown 描述 design system / 品牌的规范,让 agent 生成符合品牌的 UI。

**典型代表**
  - **VoltAgent/awesome-design-md** — 73.8k★ · A collection of DESIGN.md files inspired by popular brand design systems. Drop one in…
  - **google-labs-code/design.md** — 12.2k★ · A format specification for describing a visual identity to coding agents. DESIGN.md g…
  - **Dammyjay93/interface-design** — 4.8k★ · Design engineering for Claude Code. Craft, memory, and enforcement for consistent UI.


---

#### B4 · Prompt 库

**N=8 · 总 ★=73k**

**做什么** · 提示词集合,主要是图像生成的(nano banana、gpt-image-2)。

**典型代表**
  - **Leey21/awesome-ai-research-writing** — 22.4k★ · Elevate your AI research writing, no more tedious polishing ✨
  - **EvoLinkAI/awesome-gpt-image-2-API-and-Prompts** — 13.6k★ · GPT-Image-2 API and Prompts
  - **YouMind-OpenLab/awesome-nano-banana-pro-prompts** — 11.9k★ · 🍌 World's largest Nano Banana Pro prompt library — 10,000+ curated prompts with previ…


---

#### B5 · Awesome List

**N=10 · 总 ★=61k**

**做什么** · 传统的 awesome-X curated list。

**典型代表**
  - **hesamsheikh/awesome-openclaw-usecases** — 30.9k★ · A community collection of OpenClaw use cases for making life easier.
  - **cporter202/API-mega-list** — 5.1k★ · This GitHub repo is a powerhouse collection of APIs you can start using immediately t…
  - **mnfst/awesome-free-llm-apis** — 4.2k★ · List of Permanent Free LLM API  (API Keys)


---

### C. 垂直应用(Vertical Applications)

agent 帮你干什么——设计 / 创作 / 研究 / 浏览网页 / 自动跑公司。

#### C1 · Design / Canvas 应用

**N=10 · 总 ★=108k**

**做什么** · 用 agent 做设计——PPT 生成、海报生成、画板、Figma 替代。

**典型代表**
  - **nexu-io/open-design** — 34.3k★ · 🎨 Local-first, open-source alternative to Anthropic's Claude Design. ⚡ 19 Skills · ✨…
  - **Anionex/banana-slides** — 14.4k★ · 一个基于nano banana pro🍌的原生AI PPT生成应用，迈向真正的＂Vibe PPT＂; 支持上传任意模板图片；上传任意素材&智能解析；一句话/大纲/页面描述…
  - **JCodesMore/ai-website-cloner-template** — 14.3k★ · Clone any website with one command using AI coding agents


---

#### C2 · 创作 / 内容工具

**N=16 · 总 ★=113k**

**做什么** · 视频剪辑、屏幕录制、绿幕、AI 写作、短剧生成。

**典型代表**
  - **heygen-com/hyperframes** — 16.3k★ · Write HTML. Render video. Built for agents.
  - **webadderallorg/Recordly** — 13.8k★ · Create polished screen recordings without editing. Mac/Windows/Linux
  - **nikopueringer/CorridorKey** — 13.1k★ · Perfect Green Screen Keys


---

#### C3 · 编排 / 自主公司

**N=31 · 总 ★=271k**

**做什么** · 多 agent 协作、'零人公司'、自主 workflow。

**典型代表**
  - **paperclipai/paperclip** — 63.6k★ · Open-source orchestration for zero-human companies
  - **multica-ai/multica** — 26.3k★ · The open-source managed agents platform. Turn coding agents into real teammates — ass…
  - **openai/symphony** — 22.7k★ · Symphony turns project work into isolated, autonomous implementation runs, allowing t…


---

#### C4 · Research / 知识工作

**N=34 · 总 ★=432k**

**做什么** · AI 做研究、读论文、新闻聚合、股票分析、知识图谱。

**典型代表**
  - **karpathy/autoresearch** — 79.8k★ · AI agents running research on single-GPU nanochat training automatically
  - **666ghj/MiroFish** — 59.7k★ · A Simple and Universal Swarm Intelligence Engine, Predicting Anything. 简洁通用的群体智能引擎，预测…
  - **koala73/worldmonitor** — 53.8k★ · Real-time global intelligence dashboard. AI-powered news aggregation, geopolitical mo…


---

#### C5 · 浏览器 / Web 自动化

**N=11 · 总 ★=84k**

**做什么** · agent 怎么开浏览器干活——browser-use 系、agent-browser、爬虫 agent。

**典型代表**
  - **vercel-labs/agent-browser** — 32.3k★ · Browser automation CLI for AI agents
  - **browser-use/browser-harness** — 11.7k★ · Browser Harness | Self-healing harness that enables LLMs to complete any task.
  - **h4ckf0r0day/obscura** — 11.2k★ · The headless browser for AI agents and web scraping


---

### D. 模型与训练(Models & Training)

做模型本身——训练框架、模型架构、安全披露。**只有 26 个,在生态里是少数派**。

#### D1 · 训练 / 微调

**N=4 · 总 ★=20k**

**做什么** · LoRA / DPO / GRPO / RL 训练框架。

**典型代表**
  - **maderix/ANE** — 6.7k★ · Training neural networks on Apple Neural Engine via reverse-engineered private APIs
  - **elder-plinius/OBLITERATUS** — 5.4k★ · OBLITERATE THE CHAINS THAT BIND YOU
  - **Gen-Verse/OpenClaw-RL** — 5.3k★ · OpenClaw-RL: Train any agent simply by talking


---

#### D2 · 模型架构

**N=15 · 总 ★=57k**

**做什么** · 重新实现 / 从头复现某个模型的架构 / 推理优化。

**典型代表**
  - **kyegomez/OpenMythos** — 12.3k★ · A theoretical reconstruction of the Claude Mythos architecture, built from first prin…
  - **zai-org/GLM-OCR** — 6.3k★ · GLM-OCR: Accurate ×  Fast × Comprehensive
  - **openai/parameter-golf** — 5.0k★ · Train the smallest LM you can that fits in 16MB. Best model wins!


---

#### D5 · 安全 / 漏洞披露

**N=7 · 总 ★=22k**

**做什么** · CVE 披露、kernel exploit、AI security harness。

**典型代表**
  - **gommzystudio/device-activity-tracker** — 4.9k★ · A phone number can reveal whether a device is active, in standby or offline (and more…
  - **aloshdenny/reverse-SynthID** — 3.8k★ · reverse engineering Gemini's SynthID detection
  - **theori-io/copy-fail-CVE-2026-31431** — 3.6k★ · Copy Fail (CVE-2026-31431): 9-year-old Linux kernel LPE found by Theori's Xint Code


---

### F. 多模态生成(Multimodal Generation)

图像 / 视频 / 语音 / 3D 生成。模型是上一类(D),这一类是**模型的输出形式**——多模态本质是 user-facing 的内容生成。

#### F3 · 图像 / 视频 / 语音生成

**N=19 · 总 ★=109k**

**做什么** · 多模态生成模型——TTS、图像生成、视频生成、语音克隆。

**典型代表**
  - **jamiepine/voicebox** — 24.9k★ · The open-source AI voice studio. Clone, dictate, create.
  - **QwenLM/Qwen3-TTS** — 11.2k★ · Qwen3-TTS is an open-source series of TTS models developed by the Qwen team at Alibab…
  - **Tongyi-MAI/Z-Image** — 11.2k★ · 


---

#### F4 · 3D / 空间

**N=10 · 总 ★=43k**

**做什么** · 3D 重建、世界模型、空间智能。

**典型代表**
  - **apple/ml-sharp** — 8.3k★ · Sharp Monocular View Synthesis in Less Than a Second
  - **microsoft/TRELLIS.2** — 6.7k★ · Native and Compact Structured Latents for 3D Generation
  - **Robbyant/lingbot-map** — 6.0k★ · A feed-forward 3D foundation model for reconstructing scenes from streaming data


---

### G. 教育与教程

vibe coding 课程、Claude Code tips、Rust 教程、AI 工程学习路线。**这是上一版被错放进 "相邻领域" 的一大块**——其实跟 AI 完全相关。

#### E1 · 教育与教程

**N=37 · 总 ★=184k**

**做什么** · 课程材料、tutorial、handbook、AI 工程学习路线、vibe coding 教学。

**典型代表**
  - **2025Emma/vibe-coding-cn** — 20.4k★ · 
  - **THU-MAIC/OpenMAIC** — 17.0k★ · Open Multi-Agent Interactive Classroom — Get an immersive, multi-agent learning exper…
  - **microsoft/RustTraining** — 14.2k★ · Beginner, advanced, expert level Rust training material


---

### H. 硬件

非 AI 但跟着 AI 浪潮涨星的物理产品——键盘 CAD、电路、雷达、e-paper 固件、机械臂。

#### E2 · 硬件 / 工业设计

**N=9 · 总 ★=50k**

**做什么** · 键盘 CAD、雷达、e-paper firmware、机械臂、ESP32 机器人。

**典型代表**
  - **NawfalMotii79/PLFM_RADAR** — 19.8k★ · Open-source, low-cost 10.5 GHz PLFM phased array RADAR system
  - **memovai/mimiclaw** — 5.4k★ · MimiClaw: Run OpenClaw on a $5 chip. No OS(Linux). No Node.js. No Mac mini. No Raspbe…
  - **crosspoint-reader/crosspoint-reader** — 4.4k★ · Firmware for the Xteink X4 e-paper display reader


---

### I. 工具(Fun-Utility)

**这是数据集里第二个意外大类(N=65)**——开发者周末项目搭着 AI 浪潮涨星。菜单栏小工具、桌面 widget、文本布局、聊天导出器、字体工具等。

#### E3 · Fun-Utility / 周末项目

**N=65 · 总 ★=345k**

**做什么** · 菜单栏小工具、桌面 widget、好玩的 cli、文本布局工具、字体、字典、本地工具。

**典型代表**
  - **chenglou/pretext** — 46.5k★ · Fast, accurate & comprehensive text measurement & layout
  - **pranshuparmar/witr** — 15.1k★ · Why is this running?
  - **OpenHub-Store/GitHub-Store** — 12.8k★ · 🩵 A free, open-source app store for GitHub releases — browse, discover, and install a…


---

### Z. 长尾(Long-tail / Misc)

**N=86 · 总 ★=341k**

**做什么** · 跟 AI 生态没有直接关系的仓库——非 AI 平台 CLI、独立 messaging app、CMS、社区代码库、纯算法 / 协议 repo 等。

**典型代表**
  - **xai-org/x-algorithm** — 16.5k★ · Algorithm powering the For You feed on X
  - **QuipNetwork/quip-protocol** — 12.0k★ · experimental quip protocol network node
  - **emdash-cms/emdash** — 10.4k★ · EmDash is a full-stack TypeScript CMS based on Astro; the spiritual successor to Word…
  - **larksuite/cli** — 9.5k★ · The official Lark/Feishu CLI tool, maintained by the larksuite team — built for human…
  - **fluxerapp/fluxer** — 8.5k★ · A free and open source instant messaging and VoIP platform built for friends, groups,…


---

## 三、五大核心仓 — 真正的引力中心

**注意:这五个仓库都创建在 6 个月窗口外,所以严格来说没进数据集。但 6 个月里榜内 70% 的高星仓库都是它们的衍生 / 配置 / 加层 / 中文版**。

| 核心仓 | ★ | 创建时间 | 定位 | 在数据集中的衍生 / 周边 |
|---|---:|:---:|---|---|
| **openclaw/openclaw** | 370k | 2025-11-24 | "your own personal AI assistant. Any OS. Any Platform. 🦞" | claw-code 191k(fork)、Gen-Verse/OpenClaw-RL、HKUDS/ClawTeam、cft0808/edict 等 |
| **NousResearch/hermes-agent** | 140k | 2025-07-22 | "the agent that grows with you" | hermes-webui 6k、hermes-workspace 4k、awesome-hermes-agent 3k、garrytan/gbrain 等 10+ 个明确标注的衍生 |
| **anthropics/skills** | 131k | 2025-09-22 | Anthropic 官方 Agent Skills 仓库,定义 SKILL.md 格式 | 整个 B1 类(130 个 skills 集合仓)都按这个格式来——mattpocock/skills 67k、antigravity-awesome-skills 37k、vercel-labs/agent-skills 26k 等 |
| **google-gemini/gemini-cli** | 103k | 2024-11-12 | Google 官方 Gemini agent CLI | sickn33/antigravity-awesome-skills 等 skill 仓声明同时支持 Gemini CLI;googleworkspace/cli 26k 标注 `gemini-cli-extension` |
| **openai/codex** | 81k | 2025-04-13 | OpenAI 官方 Codex CLI | openai/skills 19k(Codex 官方 skills 目录)、Yeachan-Heo/oh-my-codex 28k(社区做的 codex 增强);openai/symphony 23k 是 OpenAI 同期的 agent 项目但跟 codex 没直接绑 |

**这五个仓加起来 825k 星**,加上数据集内的衍生,合计**生态规模超过 200 万星**。

*为什么把它们单独拎出来:这五个是过去 6 个月所有"高速增长"的真实地基。**OpenClaw 370k / Hermes 140k 是同一种东西的两个流派**——都是"open-source 的、跨平台的、个人 AI assistant"叙事。它们碰巧创建时间差 4 个月,所以一个进了我们这个 6 个月窗口的边缘,一个被切掉了。但生态作用上完全平起平坐。*

**接下来 Top 20 那张表(下一节)是 6 个月窗口内创建的仓**——这五个核心仓不在里面,但每个仓基本都是其中某一条的衍生。

---

## 四、Top 20 by stars

| ★ | 速率 | 龄 | repo | 类 | desc |
|---|---|---|---|---|---|
| 369,969 | 2242/d | 165d | **openclaw/openclaw** | A1 | Your own personal AI assistant. Any OS. Any Platform.  |
| 190,770 | 5020/d | 38d | **ultraworkers/claw-code** | A1 | The repo is finally unlocked. enjoy the party! The fas |
| 176,069 | 1586/d | 111d | **affaan-m/everything-claude-code** | B1 | The agent harness performance optimization system. Ski |
| 121,141 | 1188/d | 102d | **forrestchang/andrej-karpathy-skills** | B2 | A single CLAUDE.md file to improve Claude Code behavio |
| 91,814 | 1583/d | 58d | **garrytan/gstack** | B1 | Use Garry Tan's exact Claude Code setup: 23 opinionate |
| 79,849 | 1267/d | 63d | **karpathy/autoresearch** | C4 | AI agents running research on single-GPU nanochat trai |
| 75,704 | 476/d | 159d | **nextlevelbuilder/ui-ux-pro-max-skill** | B1 | An AI SKILL that provide design intelligence for build |
| 73,756 | 1941/d | 38d | **VoltAgent/awesome-design-md** | B3 | A collection of DESIGN.md files inspired by popular br |
| 67,002 | 713/d | 94d | **mattpocock/skills** | B1 | Skills for Real Engineers. Straight from my .claude di |
| 63,632 | 950/d | 67d | **paperclipai/paperclip** | C3 | Open-source orchestration for zero-human companies |
| 61,010 | 421/d | 145d | **gsd-build/get-shit-done** | B1 | A light-weight and powerful meta-prompting, context en |
| 59,694 | 364/d | 164d | **666ghj/MiroFish** | C4 | A Simple and Universal Swarm Intelligence Engine, Pred |
| 56,785 | 1670/d | 34d | **JuliusBrussee/caveman** | B1 | 🪨 why use many token when few token do trick — Claude  |
| 56,719 | 361/d | 157d | **code-yeongyu/oh-my-openagent** | A1 | omo; the best agent harness - previously oh-my-opencod |
| 53,785 | 448/d | 120d | **koala73/worldmonitor** | C4 | Real-time global intelligence dashboard. AI-powered ne |
| 51,663 | 1520/d | 34d | **MemPalace/mempalace** | A4 | The best-benchmarked open-source AI memory system. And |
| 48,266 | 469/d | 103d | **VoltAgent/awesome-openclaw-skills** | B1 | The awesome collection of OpenClaw skills. 5,400+ skil |
| 46,482 | 750/d | 62d | **chenglou/pretext** | E3 | Fast, accurate & comprehensive text measurement & layo |
| 45,154 | 1290/d | 35d | **safishamsi/graphify** | B1 | AI coding assistant skill (Claude Code, Codex, OpenCod |
| 44,892 | 424/d | 106d | **rtk-ai/rtk** | A1 | CLI proxy that reduces LLM token consumption by 60-90% |

**观察**:top 20 里 **15 个是 A(基础设施)/ B(skill / 提示词分发)** —— "基础设施 + 分发" 占头部 75%。Top 1 openclaw/openclaw 369k 星 / 165 天龄,等于一个项目就贡献了全数据集 6.24M 星里的 **5.9%**。

---

## 五、新仓的注意力周期(cohort 分析)

| 龄段 | N | 中位 ★/d | max ★/d | cohort 总 ★ |
|---|---|---|---|---|
| ≤14d | 10 | **360** | 3117 | 62k |
| 15-30d | 39 | **150** | 679 | 191k |
| 31-60d | 162 | **87** | 5020 | 1410k |
| 61-90d | 151 | **52** | 1267 | 1136k |
| 91-120d | 156 | **39** | 1586 | 1641k |
| 121-180d | 185 | **29** | 2242 | 1799k |

**14 天龄中位 ~350/d → 180 天龄中位 ~30/d, 12× 衰减**。这不是引力,是 **GitHub trending 算法的可见性窗口** + **早期采用者注意力周期**。推论:**一个仓库前 30 天没拿到 5k+ 星基本不会再起飞**——本数据集里 60 天后还能涨过 100/d 的全是 `karpathy/`、`antirez/`、`chenglou/`、`mattpocock/` 这种**作者背书型展品**。

---

## 六、引用图:谁是谁的地基

从 enriched README 里 grep github.com 链接,看哪些 repo 被反复点名当地基。**前 15 名**:

| 被引次数 | 在数据集里? | repo | 状态 |
|---|---|---|---|
| 9 | ✅ | **openclaw/openclaw** | 370k A1 |
| 8 | ⏰ | openai/codex | 81k(2025-04 创建,窗口外) |
| 7 | ⏰ | anthropics/skills | 131k(2025-09 创建,窗口外,事实标准) |
| 7 | ⏰ | google-gemini/gemini-cli | 103k(2024-11 创建,窗口外) |
| 3 | ⏰ | badlogic/pi-mono | 外部 / 窗口外 |
| 3 | ✅ | **vercel-labs/agent-skills** | 26k B1 |
| 3 | ⏰ | anthropics/claude-code | 巨大,Anthropic 官方 |
| 3 | ⏰ | astral-sh/uv | 40k+,Python 包管理器 |
| 2 | ✅ | **yeachan-heo/oh-my-codex** | 28k A1 |
| 2 | ✅ | **multica-ai/multica** | 26k C3 |
| 2 | ⏰ | voltagent/voltagent | 8.7k,VoltAgent 母组织 |
| 2 | ⏰ | openclaw/skills | OpenClaw 官方 skills repo |
| 2 | ✅ | **affaan-m/everything-claude-code** | 176k B1 |

**这张表说明**:
- **anthropics/skills(131k)、google-gemini/gemini-cli(103k)、openai/codex(81k)** 是"窗口外的隐形地基"——它们创建早(2024-2025),所以没出现在 6 个月 cohort 里,但榜内 top repo 一半都点名它们。**真实的引力中心不一定在数据里**。
- **openclaw/openclaw 在数据集内被自家衍生引用 9 次**——它是数据集内的真 hub。

---

## 七、结构性观察

### 7.1 个人 vs 组织(几乎一半一半)

- **User**: 414 (59%)
- **Organization**: 289 (41%)

- 相比上次 90 天 map(User 65% / Org 35%),6 个月窗口里 **个人作者占比下降到 59%**——窗口越长,组织(包括大厂、机构、HKUDS 这种生产线团队)越浮出水面。
- 但**头部 still User-heavy**:Top 20 里 14 个是个人账号(garrytan、karpathy、forrestchang、affaan-m、JuliusBrussee、mattpocock 类型)。

### 7.2 语言:TS 反超 Python

- **TypeScript**: 206 (29%)
- **Python**: 189 (27%)
- **—**: 59 (8%)
- **JavaScript**: 51 (7%)
- **Rust**: 46 (7%)
- **Shell**: 28 (4%)
- **Go**: 26 (4%)
- **HTML**: 22 (3%)
- **Swift**: 19 (3%)
- **C**: 11 (2%)

- **TypeScript 29% > Python 27%**——上次 90 天 map 还是 Python 微胜。这是 agent 生态"TS 中间件化"的硬证据。
- **markdown-only(no primary lang)~8%**——59 个 skill / awesome-list / DESIGN.md repo 里没有任何代码。**markdown 是 2026 年 GitHub 上的新一等公民语言**。
- **Swift 19 个排第 9**——这是上次 90 天没看到的;6 个月窗口里有不少 macOS 菜单栏 / Swift 周末项目(都在 I 类 fun-utility 里)。

### 7.3 协议:MIT 47%,no-license 16%

| license | N | 占比 |
|---|---|---|
| MIT | 331 | 47% |
| Apache-2.0 | 116 | 17% |
| none | 113 | 16% |
| NOASSERTION | 72 | 10% |
| AGPL-3.0 | 42 | 6% |
| GPL-3.0 | 16 | 2% |
| CC0-1.0 | 4 | 1% |
| GPL-2.0 | 3 | 0% |

- **MIT 47%** 主导。和老一代 infra(Kubernetes/TF/PyTorch 用 Apache)反过来——agent skill / harness / markdown 没专利可保,作者只要署名。
- **no license + NOASSERTION 合计 ~26%**——四分之一的 repo 法律上不可商用。**这是"个人作者周末项目"的另一个侧证**。

---

## 八、增长模式 / 八条规律

### 1. 一个仓的"注意力半衰期"约 30 天

新仓在前 14 天能获得的关注度,**到第 60 天会衰减到 1/4,到 180 天衰减到 1/12**——这是一条很陡的指数曲线。

> **实操含义**:你想做 agent 工具,前 30 天的 traction 决定一切。30 天内没拿到 5k+ 星,基本不用指望第二次起飞——除非你是 Karpathy / antirez 这种作者背书型。

### 2. "涨得最快"和"做得最多"是两件事

- **B3 design-md 只有 5 个仓**,但头部 awesome-design-md 73k、open-design 34k、design.md 12k——**赢家通吃**,要做就做头三个。
- **B1 skills-collection 130 个仓**,总星 1.6M,头部、腰部、长尾都有——**普惠市场**,做一个中等质量的 skill 包也能拿几千星。

### 3. 头部 70% 是 A+B(基础设施 + 分发)

Top 20 里 15 个是 agent harness 或 skills,只有 5 个是真应用产品(paperclip、autoresearch、worldmonitor、MiroFish 等)。

> **意味着**:普通用户能直接用的产品很少,大部分星在"开发者给开发者做的工具"里。

### 4. 真上游不在数据集里

anthropics/skills(131k 2025-09)、openai/codex(81k 2025-04)、google-gemini/gemini-cli(103k 2024-11)三家**都创建在 6 个月窗口外**。**真正的引力中心是窗口外的官方平台,不是榜内的衍生**。

> 这跟 npm / Chrome Extension 早期一模一样——平台官方先做出来,生态后来跟进。

### 5. 人格化命名跑赢通用命名 3-5×

"caveman"(57k)、"女娲"、"张雪峰"、"PUA"、"colleague"(17k)——**个人 / 角色 / 梗命名跑赢同期 awesome-X 类至少 3-5 倍**。

> **这是 skill 和 npm package 的根本区别**:npm 名字是工具用法,skill 名字是人格隐喻。

### 6. README 头部三件套已固化

Top 50 共同结构:

(a) **slogan**(一句话,带数字 / 反差 / 隐喻)
(b) **多语言徽章 + star history**
(c) **demo 图 / 视频**(不是截图,是动效)

> **最硬规则:第一段必须有数字。** 没数字的 README 在 1k+ 区基本不见。

### 7. ≤14 天破 2k 星只有两条剧本

(a) **security disclosure**(V4bel/dirtyfrag 1.2 天 3k,CVE 自带流量)
(b) **"开源对位某商业产品"**(open-design 对 Claude Design,11 天 33k)

没走这两条而 14 天破 2k 的,基本只剩"作者背书"(antirez 类型)。

### 8. 大厂集体下场,但中文 sub-生态他们没下手

Google(design.md / googleworkspace/cli / google/skills)、OpenAI(symphony / codex-plugin-cc / skills)、NVIDIA(NemoClaw / personaplex)、Microsoft(agent-governance / RustTraining)、Vercel Labs(4 个 1k+ 仓)、Tencent / MiniMax / 阿里 / 京东都有 1 万+ 项目。

> **但中文 skill 子生态(女娲、话术、张雪峰、姚金刚提示词、xiaohongshu-cli 类)大厂全没下手** —— 这是中文创作者的明确窗口期。

## 九、数据局限

- **stars/day 是平均速率,不是当前速率**——一个 60d 老 repo 早期 1 周 5k★ + 后期缓增,会被低估;反之亦然。要看 star-history 才能区分。
- **没拉 last-30d commit 数 / contributor count**——所以"这个仓库到底还有多少人在用"这个问题没法严格回答。
- **分类用 LLM 重做了一遍**(703 个仓全部读 README 头 1500 字),改掉了规则版 426 个错分(主要是 B1 / I / G 三类)。残留误差应该 < 5%,但仍有边界模糊的(单仓既是 skill 又是 CLI 的怎么算)。
- **引用图基于 README mention**,有些 repo 的依赖关系在代码 / package.json 里,这套抓不到。
- **没去重 fork-of-fork**(如 ultraworkers/claw-code-parity 这类衍生)。
- **上游 hub 的星数都是当前(2026-05-09)的**,不是窗口结束时的——所以引力中心定位是 directional 准的,不是历史精确。

数据原料: `_raw_6m/repos.jsonl` `_raw_6m/readmes.json` `_raw_6m/citations.json` `_raw_6m/final_categories.json` `_raw_6m/reclassify_reasons.json`。