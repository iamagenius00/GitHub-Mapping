# GitHub AI 生态近 6 个月 Mapping

## 研究范围与口径

这份 mapping 看的是过去 6 个月新建、且达到 2000+ stars 的 GitHub AI repo,共 703 个仓库。时间窗口是 `created:2025-11-09..2026-05-09`;stars、forks、issues 等指标来自抓取时点,正文用近似值看量级和结构。

分类方式是:先判断一个仓库最主要在做什么,再记录它明显覆盖的副方向。比如 `openclaw/openclaw` 主类是 agent harness,同时也带 skills 分发;`garrytan/gstack` 主类是 Claude Code skill/tool 包,同时也是 coding workflow;`MemPalace/mempalace` 主类是 agent memory,同时以 skill/hook 方式接入;`steipete/CodexBar` 主类是 usage/cost observability,同时也是 macOS menu bar utility。

因此本文采用 multi-label 覆盖口径:每个仓库有 1 个主类和 0-2 个副类。一个 repo 只要主类或副类包含某个方向,就计入该方向;所以各方向覆盖率和覆盖 stars 不能相加成 100%。完整标签表和子门类解释见 §8。

stars 先看作关注度指标,不直接代表质量、真实用户数或商业价值。本文会结合 `peak ★/day`、`fork/star`、`issue/star`、最近 push 和 license 等信号辅助判断。

## 核心判断

这半年 GitHub AI 生态的主角正在从模型本身转向 **distribution**:把现有模型包装成可安装、可复制、可嵌入日常工作的工具。这里的 distribution 很具体:SKILL.md / CLAUDE.md / DESIGN.md 这类 markdown 交付物,agent harness / plugin / CLI,以及能直接进入 coding、research、design 工作流的配置和工具。

703 个 2000+ 星新仓库里,按 multi-label / 标签覆盖口径,**A 基础设施覆盖 248 个仓库(35.3%)**,**B skills/prompts 覆盖 235 个仓库(33.4%)**,A 或 B 任一覆盖 **417 个仓库(59.3%)**。模型/训练 D 系只覆盖 **29 个仓库(4.1%)**;D/F 模型、媒体生成与 3D 合计覆盖 **65 个仓库(9.2%)**。

关注度也沿着这条线集中:Top 20 仓库拿走 **~1.83M stars(29.4%)**,其中 **17/20** 被 A/B 标签覆盖,**13/20** 被 B 系(skills/prompts/config)标签覆盖。更重要的是,这些项目已经越过“收藏”层面:Top 20 的 median `peak ★/day` 约 **920**,`fork/star`(forks/stars) median 约 **11.5%**;`openclaw/openclaw` 单日最高 **5,608** stars,`ultraworkers/claw-code` 单日最高 **4,814** stars。GitHub 这半年最显眼的竞争点变成了:谁能把 Claude Code / OpenClaw / Codex 包装成可分发、可安装、可复制的工作流。

Markdown 正在变成 AI 软件的交付格式之一。SKILL.md / CLAUDE.md / DESIGN.md 不只是说明文档,而是在 agent 生态里承担 package、policy、workflow template、design spec 和能力分发的功能。GitHub repo 也因此不再只是代码容器,一部分 repo 正在同时承担展示页、收藏夹、分发目录和可安装配置的角色。

同时,爆款不只来自单个 repo,也来自 owner portfolio。HKUDS、vercel-labs、openclaw、OpenAI、Anthropic、VoltAgent 这类 owner 正在用多个仓库成套铺开 agent harness、skills、demo、dashboard、awesome list 和垂直应用。生态势能开始从“一个项目是否火”转向“一个 owner 能否连续制造周边”。

---

## 1. stars 衡量的是关注度,不是质量

本文把 stars 当作注意力和传播结果,不把它直接等同于代码质量、真实用户数或商业价值。质量需要结合维护节奏、issue/PR 处理、contributors、测试、CI、release、许可证和真实使用反馈判断。本文主要使用 stars、forks、open issues、创建时间、最近 push 时间和 license;PR 合并情况、contributors 和 release 节奏不作为本轮统计口径。

这点在 GitHub AI 生态里尤其重要。stars 已经不只是开发者收藏行为,也是一种 attention signal:它会影响 Trending、媒体报道、投资筛选和项目可信度。GitHub 上已经存在成熟的 fake stars / star-buying 市场,AI/LLM 项目又是高风险类别。stars 可以说明一个项目被看见了,但不能直接说明它真的好用、真的被使用,或真的有稳定社区。

| 指标 | 本文怎么用 | 不能直接说明什么 |
|---|---|---|
| `stars` | 注意力、收藏、传播结果 | 代码质量、真实使用量、收入 |
| `peak ★/day` | 单日 star 峰值,看项目是否出现集中扩散 | 长期留存和持续增长 |
| `forks` / `fork/star` | 复制压力:是否被拿去改、跑、部署、二创 | fork 后是否真的成功使用 |
| `open issues` / `issue/star` | 使用摩擦、需求入口、项目活跃度线索 | 维护质量高低;issue 多可能是用户多,也可能是问题多 |
| `pushed` / `days_since_push` | 仓库是否还在被维护 | 维护质量和路线图 |
| license | 商业复用和二次分发边界 | 项目能力本身 |

forks 本身也会被 stars 带着走:越火的项目通常也会有更多 forks。因此本文更关注 `fork/star`,也就是每 100 个 stars 里大约有多少 forks。全样本中位数约 10.4%;超过 14% 已经偏高,超过 30% 往往意味着这个仓库不只是被收藏,还在被大量复制、改装或部署。这类项目常见于教程、可运行替代、本地部署入口和工作流模板。

低 `fork/star` 不能直接证明 fake stars。awesome list、README-first repo 和单文件 skill/config 本来就可能被收藏、复制片段或直接安装,未必表现为 fork。但当一个项目 stars 极高、`fork/star` 极低、issues/PR/维护活动也很弱时,它就更需要被谨慎解读。

下文会用三个信号辅助理解高星项目:`peak ★/day` 看单日传播峰值,`fork/star` 看复制压力,`issue/star` 看使用摩擦和维护压力。平均 `stars/day` 会把爆发日和冷却期抹平,所以 Top 20 段落改用 GH Archive star 事件算出的单日峰值。`fork/star` 超过 ~14% 属于高复制压力,`issue/star` 超过 ~1.4% 则提示项目可能已经遇到较多使用问题或维护请求。这些阈值不是质量评分,只是帮助区分不同类型的高星增长。

| 指标剖面 | 可能对应的传播机制 | 分析含义 |
|---|---|---|
| 高 `peak ★/day` + 高 `fork/star` | 可复制工具/模板 | 不只被收藏,也被拿去改、跑、部署或二创 |
| 高 `peak ★/day` + 低 `fork/star` | attention-heavy / README-first repo | 传播强,但真实使用和工程成熟度需要更多证据 |
| 高 `peak ★/day` + 高 `issue/star` | 高需求 + 高摩擦 | 可能是真实使用带来大量问题,也可能是维护压力或产品不稳定 |
| 低 stars + 高 PR/contributor/activity | 深水区项目 | 不在本文 2000+ stars 样本重点覆盖范围内 |

这个框架的重点不是给项目打分,而是提醒读者:stars 只回答“谁被看见”,forks、issues、PR 和维护节奏才开始接近“谁被使用、谁能持续维护”。

---

## 2. 宏观方向

下表看的是 **宏观方向覆盖**:一个仓库只要主类或副类包含某个方向,就计入该方向。这里统计的是覆盖范围,并非排他归属;覆盖率和覆盖 stars 都不要纵向相加。先看这张横截面,A/B/C 已经构成这批高星新仓的主体。

| 方向 | 覆盖仓库 | 仓库覆盖率 | 覆盖 stars | 占总 stars |
|---|---:|---:|---:|---:|
| **A** Agent Infrastructure | 248 | 35.3% | ~2.97M | 47.7% |
| **B** Skills & Prompts | 235 | 33.4% | ~3M | 48.1% |
| **C** Vertical Applications | 200 | 28.4% | ~1.93M | 30.9% |
| **D** Models & Training | 29 | 4.1% | ~119k | 1.9% |
| **F** Media & 3D Generation | 37 | 5.3% | ~205k | 3.3% |
| **E1** Education | 44 | 6.3% | ~247k | 4.0% |
| **E2** Hardware | 9 | 1.3% | ~73k | 1.2% |
| **E3** Fun-Utility | 77 | 11.0% | ~512k | 8.2% |
| **J** AI Security Tools | 10 | 1.4% | ~214k | 3.4% |
| **K** Eval & Observability | 17 | 2.4% | ~162k | 2.6% |
| **Z** Long-tail | 106 | 15.1% | ~477k | 7.6% |

**三个数字概括主线**:

- **A/B 任一覆盖 417 个仓库(59.3%)**:六成高星仓库都在 agent 运行层、IDE/workflow、skill/prompt 分发层附近。
- **B 系覆盖 235 个仓库(33.4%)**:skills、prompts、markdown config 已经是新一代 AI 软件分发层;其中 B1/B2/B3 覆盖 215 个仓库(30.6%),集中对应 SKILL.md、CLAUDE.md、DESIGN.md 这些可复制、可安装的 markdown 交付物。
- **D/F 任一覆盖 65 个仓库(9.2%)**:模型、训练、媒体生成与 3D 仍然存在,但 GitHub 新仓关注度的重心已经转向上层工具和分发形态。

标签缩写可按下表速查;完整解释见 §8 标签说明。

| 方向 | 含义 | 常见子标签 |
|---|---|---|
| **A** Agent Infrastructure | agent 运行层、IDE、协议、memory、sandbox、serving | A1 harness/CLI; A2 coding IDE; A3 protocol; A4 memory; A5 sandbox; A6 inference |
| **B** Skills & Prompts | skills、prompt、markdown config、awesome list | B1 skills collection; B2 CLAUDE.md; B3 DESIGN.md; B4 prompt library; B5 awesome list |
| **C** Vertical Applications | 设计、内容、coding workflow、research、browser automation、multimodal app | C1 design; C2 creator/content; C3 coding workflow; C4 research/knowledge; C5 browser; C6 multimodal app |
| **D/F** Models, Media & 3D | 模型、训练、媒体生成模型/服务与 3D/spatial;不包含普通设计 app | D1 training; D2 model architecture; D5 security disclosure; F3 media generation; F4 3D/spatial |
| **E/J/K/Z** Other | 教育、硬件、utility、安全、eval/observability、long-tail | E1 education; E2 hardware; E3 utility; J1 AI security tool; K1 eval/observe; Z long-tail |

## 3. 发现一:高星项目正在转向 distribution

这轮数据里最清楚的一条线索是:GitHub 星标主要流向那些能被复制、安装、嵌入 agent 工作流的交付物。这里面包括 markdown skill 包、agent harness、设计/研究/coding workflow,也包括用量、成本和 context 观测工具。开发者集中关注的是可以马上 fork、安装、接入自己工具链的形态。

### 3.1 Top 20

| Top 20 星标 | 占全数据集 | A/B 覆盖 | B 系覆盖 | median peak ★/day | median fork/star |
|---|---|---|---|---:|---:|
| ~1.83M | 29.4% | 17/20 | 13/20 | ~920 | 11.5% |

这里的 `peak ★/day` 来自 [GH Archive](https://www.gharchive.org/) / ClickHouse GitHub events 的 `WatchEvent`,按 repo 和日期聚合后取最高一天。它看的是传播峰值,比平均 `stars/day` 更适合观察集中爆发。`WatchEvent` 记录加星事件,不会扣掉 unstar,所以这里不拿它替代 GitHub 当前 stars 总数。

`fork/star` 不能严格等同于使用率,但可以作为“复制压力”的粗指标:它区分的是“看见并收藏”和“复制、改装、接入自己的工作流”。Top 20 里有 13 个仓库的 `fork/star` 超过 10%,说明这批项目的传播已经越过 GitHub Trending 页面。

| 仓库 | peak ★/day | 峰值日期 |
|---|---:|---|
| `openclaw/openclaw` | 5,608 | 2026-01-31 |
| `ultraworkers/claw-code` | 4,814 | 2026-04-02 |
| `karpathy/autoresearch` | 2,108 | 2026-03-08 |
| `VoltAgent/awesome-design-md` | 1,870 | 2026-04-05 |
| `affaan-m/everything-claude-code` | 1,750 | 2026-01-23 |
| `JuliusBrussee/caveman` | 1,379 | 2026-04-11 |
| `chenglou/pretext` | 1,344 | 2026-03-29 |
| `garrytan/gstack` | 1,236 | 2026-03-14 |
| `forrestchang/andrej-karpathy-skills` | 1,168 | 2026-04-15 |
| `paperclipai/paperclip` | 979 | 2026-03-08 |

| ★ | 标签 | 仓库 | 简介 |
|---|---|---|---|
| ~370k | A1+B1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 |
| ~191k | A1 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | The repo is finally unlocked. enjoy the party! The fastest repo in history to s… |
| ~176k | B1+A2+J1 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | The agent harness performance optimization system. Skills, instincts, memory, s… |
| ~121k | B2+B1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Ka… |
| ~92k | B1+C3 | [garrytan/gstack](https://github.com/garrytan/gstack) | Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO… |
| ~80k | C4+C3 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | AI agents running research on single-GPU nanochat training automatically |
| ~76k | B1+C1 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | An AI SKILL that provide design intelligence for building professional UI/UX mu… |
| ~74k | B3+B5 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | A collection of DESIGN.md files inspired by popular brand design systems. Drop … |
| ~67k | B1+A2 | [mattpocock/skills](https://github.com/mattpocock/skills) | Skills for Real Engineers. Straight from my .claude directory. |
| ~64k | C3+A1 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | Open-source orchestration for zero-human companies |
| ~61k | B1+A2 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | A light-weight and powerful meta-prompting, context engineering and spec-driven… |
| ~60k | C4+A4 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | A Simple and Universal Swarm Intelligence Engine, Predicting Anything. 简洁通用的群体智… |
| ~57k | B1+A2 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% … |
| ~57k | A1+B1 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | omo; the best agent harness - previously oh-my-opencode |
| ~54k | C4 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | Real-time global intelligence dashboard. AI-powered news aggregation, geopoliti… |
| ~52k | A4+B1 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | The best-benchmarked open-source AI memory system. And it's free. |
| ~48k | B1 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | The awesome collection of OpenClaw skills. 5,400+ skills filtered and categoriz… |
| ~46k | E3 | [chenglou/pretext](https://github.com/chenglou/pretext) | Fast, accurate & comprehensive text measurement & layout |
| ~45k | B1+A4 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, an… |
| ~45k | A1+E3 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. … |

### 3.2 各方向的星标分布

| 方向 | 覆盖仓库 | 典型 stars | 覆盖 stars |
|---|---:|---:|---:|
| Agent Infrastructure | 248 | ~4.2k | ~2.97M |
| Skills & Prompts | 235 | ~4.6k | ~3M |
| Vertical Applications | 200 | ~4.5k | ~1.93M |
| Models & Training | 29 | ~3.3k | ~119k |
| Media & 3D Generation | 37 | ~3.4k | ~205k |
| Education | 44 | ~3.8k | ~247k |
| Hardware | 9 | ~3.6k | ~73k |
| Fun-Utility | 77 | ~4k | ~512k |
| AI Security Tools | 10 | ~2.8k | ~214k |
| Eval & Observability | 17 | ~4.7k | ~162k |
| Long-tail | 106 | ~3.6k | ~477k |

这里的“典型 stars”用中位数表示,避免被个别超高星仓库带偏。按这个口径看,B 系 skills/prompts、A 系 agent infrastructure 和 C 系应用层的中位数都在 4k stars 以上,说明关注度不只集中在少数爆款上。结合覆盖 stars,A/B/C 的高星覆盖量说明关注度已经转向“把模型能力分发给 agent 的层”。翻译成产品形态,就是模型本身退到背景里,开发者更愿意传播那些能让模型进入工作流的接口、配置、skill 和 dashboard。

### 3.3 现象级仓库说明什么

| 仓库 | 标签 | stars | peak ★/day | 峰值日期 | forks | fork/star |
|---|---|---:|---:|---|---:|---:|
| `openclaw/openclaw` | A1+B1 | ~370k | 5,608 | 2026-01-31 | ~76k | 20.6% |
| `ultraworkers/claw-code` | A1 | ~191k | 4,814 | 2026-04-02 | ~110k | 57.6% |
| `affaan-m/everything-claude-code` | B1+A2+J1 | ~176k | 1,750 | 2026-01-23 | ~27k | 15.5% |
| `forrestchang/andrej-karpathy-skills` | B2+B1 | ~121k | 1,168 | 2026-04-15 | ~12k | 10.1% |

100k+ 的 4 个仓库里,median `fork/star` 约 18.1%;50k+ 的 16 个仓库里,11 个被 B1/B2/B3 覆盖。这说明“markdown / skill / config”已经进入这轮高传播项目的核心形态,也指向一种新的 distribution pattern 正在成型。

这些仓库更像一种可分发单元:可以 fork,可以上榜,也可以复制进不同 agent harness。star 给它们带来可见度,fork 则说明一部分读者开始复制和改装。

如果把 `fork/star` 单独拿出来看,高比例项目多集中在教程、可运行替代、自动化工作流或本地部署入口。这个指标适合用来观察 AI repo 的复制压力。

| 仓库 | stars | fork/star | 形态 |
|---|---:|---:|---|
| `sanbuphy/learn-coding-agent` | ~12k | 167.1% | coding agent 教程/研究材料 |
| `ZhuLinsen/daily_stock_analysis` | ~35k | 98.9% | 可部署的定时分析工作流 |
| `claude-code-best/claude-code` | ~18k | 88.0% | 本地可运行的 Claude Code 兼容实现 |
| `ultraworkers/claw-code` | ~191k | 57.6% | 高传播 agent runtime |
| `qwibitai/nanoclaw` | ~29k | 44.5% | 轻量替代与容器运行版本 |

### 3.4 从单个爆款到 owner portfolio

| owner | 仓库数 | stars | 覆盖标签分布 |
|---|---:|---:|---|
| HKUDS | 10 | ~143k | A1×4 / B1×3 / C4×3 / A3×2 / A4×2 / C3×2 / A2 / C1 / E1 / K1 |
| vercel-labs | 8 | ~112k | A1×2 / A2×2 / A5×2 / B1×2 / A3 / C1 / C5 / E3 / Z |
| openclaw | 5 | ~391k | A1×2 / B1×2 / A2 / A3 / B5 / E3 / Z |
| openai | 5 | ~66k | A1×2 / B1×2 / D2×2 / C3 |
| anthropics | 5 | ~53k | B1×3 / C4×2 / D2 / E1 |
| alchaincyf | 5 | ~44k | B1×4 / E1×2 / C1 / C4 |
| QuipNetwork | 5 | ~35k | Z×5 |
| op7418 | 5 | ~24k | B1×4 / A1×2 / C1×2 / C2 |
| VoltAgent | 4 | ~129k | B1×2 / B3×2 / A2 / B5 / C1 |
| karpathy | 3 | ~102k | C4×2 / C3 / E3 / K1 |
| NVIDIA | 3 | ~36k | A5×2 / A1 / B1 / F3 |
| zai-org | 3 | ~35k | D2×2 / A1 / F3 |

这里有两种扩散:HKUDS、openclaw、vercel-labs 是组织级成套铺开;alchaincyf、op7418、Karpathy 则是个人品牌把一个工作流拆成多个 markdown/software 交付物。覆盖标签分布会重复计入同一个仓库的主类和副类。

这意味着研究单位可以从“单个爆款 repo”上移到 **owner portfolio**。一个 owner 能不能连续产出 harness、skill、awesome list、dashboard、demo 和垂直版本,比单个仓库的 stars 更能说明它有没有生态生产能力。

### 3.5 从单点爆红到同题材 wave

更深一层看,这批高星项目呈现成组出现的模式。很多项目围绕同一个上游、同一个文件格式、同一种命名入口或同一种社会想象成批冒出。下表是按仓库名、README、简介和 topics 做的关键词线索统计,不是互斥分类;它更适合用来看“一个概念扩散成生态”的速度。

| wave / cluster | 覆盖仓库 | 覆盖 stars | 时间形态 | 代表项目 | 说明 |
|---|---:|---:|---|---|---|
| OpenClaw / Claw 周边 | 141 | ~1.76M | OpenClaw 出现后 60 天内已有 22 个相关仓库;2-3 月又出现 90 个 | `openclaw/openclaw`, `awesome-openclaw-skills`, `nanoclaw`, `picoclaw`, `zeroclaw`, `OpenViking` | 一个上游 agent harness 很快带出 skills、use case、轻量替代、硬件版本、memory/context、管理面板和安全周边。 |
| Claude Code / claw-code 兼容层 | 155 | ~1.99M | 3/31-4/7 一周内出现 27 个相关仓库,合计 ~478k stars | `ultraworkers/claw-code`, `claude-code-best/claude-code`, `openclaude`, `caveman`, `graphify` | 高星同时来自 runtime 本体、可运行实现、性能优化、token 节省、技能包和可视化工具。 |
| DESIGN.md / design agent | 19 | ~340k | `awesome-design-md` 之后 30 天内出现 9 个相关仓库,合计 ~150k stars | `awesome-design-md`, `design.md`, `open-design`, `huashu-design`, `design-extract`, `awesome-claude-design` | 一旦 markdown 成为 agent 可读的设计接口,生态会同时长出规范、集合、提取器、替代产品和品牌化 design skill。 |
| OpenCLI / CLI-Hub | 9 | ~106k | 3/8-3/25 出现 4 个相关仓库,合计 ~65k stars | `CLI-Anything`, `OpenCLI`, `larksuite/cli`, `AutoCLI` | CLI 正在从“人操作工具”变成“agent 调用外部软件的标准入口”。 |
| skill/config packs | 146 | ~1.40M | 1 月有 39 个 skill/config 仓库;3-4 月又有 61 个 | `andrej-karpathy-skills`, `agent-skills`, `awesome-openclaw-skills`, `awesome-design-md`, `vercel-labs/skills` | 不同 agent harness 正在同时争夺“可安装能力包”的目录和格式。 |
| persona / distill skills | 8 | ~66k | 3/30-4/6 一周内出现 6 个相关仓库,合计 ~57k stars | `colleague-skill`, `nuwa-skill`, `ex-skill`, `yourself-skill`, `awesome-persona-distill-skills`, `anti-distill` | 中文社区把 skill 从“工具能力包”推到“人格/关系/方法论蒸馏”:同事、前任、自己、名师、反蒸馏都变成可安装的 agent 行为模板。 |

这张表比单看 Top 20 更能解释为什么高星增长会这么快:一个概念先通过核心仓库获得注意力,随后同一批开发者会迅速补齐生态位,包括 awesome list、hosted wrapper、兼容层、教程、dashboard、插件、技能包和垂直版本。GitHub 上的新 AI 项目越来越像围绕标准、上游和可复制模板的同步扩散。

### 3.6 persona skill:skill wave 的内容化边缘

persona / distill skills 值得保留,但更适合作为边缘信号,不宜当成这轮 AI GitHub 的主线技术结论。它更像 skill wave 的 meme 化外溢:当 skill 可以打包工具能力,同一套格式也会被用来打包人设、关系、表达方式和判断风格。

这类项目的传播逻辑接近内容平台:repo name 像标题,README 像封面页,star 像收藏,awesome list 像合集,skill 则把某种行为模板做成可转发对象。它和工程化 SKILL.md / CLAUDE.md / DESIGN.md 共用同一套 GitHub distribution 通道:低成本展示、低成本复制、低成本二创。两者的交付对象不同:工程化 skill 交付工作流,persona skill 交付可模仿的表达和判断方式。

这个观察提示了一个更广的变化:一部分 AI repo 已经同时承担代码仓库、展示页、收藏夹和内容传播单元的角色。

---

## 4. 发现二:窗口外上游塑造窗口内爆发

6 个月窗口只收“新建仓库”,但 agent 生态的真实引力中心并不总在这个时间窗口内。这里的“时间窗口外”特指仓库创建时间不在 `2025-11-09..2026-05-09` 这 6 个月内,不代表它不重要。不少窗口内的高星仓库,其实是在给时间窗口外的官方/半官方平台做 skill、wrapper、dashboard、中文化、评测、复刻或工作流包装。

| 上游 / 基础项目 | 与本次时间窗口的关系 | 生态作用 |
|---|---|---|
| `anthropics/skills` | 时间窗口外 | SKILL.md 事实标准;许多 B1 仓库隐式对位它。 |
| `openai/codex` | 时间窗口外 | Codex CLI 是 openai/skills、oh-my-codex、codex-plugin-cc 等项目的共同分发目标。 |
| `google-gemini/gemini-cli` | 时间窗口外 | Gemini CLI 被许多 skill/harness 仓库列为兼容目标,也是 Google 系 agent 工具的入口。 |
| `NousResearch/hermes-agent` | 时间窗口外 | Hermes 生态催生 gbrain、hermes web UI、Hermes 教程和 memory/workspace 周边。 |
| `openclaw/openclaw` | 时间窗口内,但更像上游 | 数据集内最大的中心项目;openclaw skills、clawhub、OpenClaw connector、OpenClaw 教程和 fork 都围绕它扩散。 |

这轮观察可以理解为:上游 agent harness 和 skills 规范先出现,然后在 6 个月内被 markdown skill、agent workflow、观测工具和垂直应用迅速产品化、社区化。

---

## 5. 交叉结构:哪些能力经常被打包在一起

下表看的是标签共现:只要两个标签同时出现在同一个仓库的主类/副类里,就计数。它回答的问题是:哪些能力经常被放进同一个 repo。按这个口径,skills/prompts 经常和 coding IDE、research、design、memory 一起出现,说明许多高星仓库已经从单点工具长成可安装的 workflow 包。

| 组合 | 数量 | 含义 |
|---|---:|---|
| A2 + B1 | 33 | coding-agent-ide + skills-collection |
| B1 + C4 | 31 | skills-collection + research-knowledge-work |
| A1 + C3 | 24 | agent-harness-cli + coding-workflow-orchestration |
| B1 + C1 | 21 | skills-collection + design-canvas-app |
| B1 + C3 | 17 | skills-collection + coding-workflow-orchestration |
| A1 + A2 | 14 | agent-harness-cli + coding-agent-ide |
| A1 + B1 | 14 | agent-harness-cli + skills-collection |
| A4 + B1 | 13 | agent-memory + skills-collection |
| A1 + A5 | 12 | agent-harness-cli + sandbox-runtime |
| B1 + C2 | 11 | skills-collection + creator-content |
| B1 + E3 | 11 | skills-collection + fun-utility |
| A2 + E3 | 10 | coding-agent-ide + fun-utility |

这些组合解释了为什么只看单一归属会丢掉关键信息:

- `B1 + C4`:研究/知识工作不一定做成 SaaS,更多时候做成 skill 包。
- `A2 + B1`:coding workflow 被压缩成可安装的 skill,不一定表现为一个新 IDE。
- `B1 + C1`:设计能力被 markdown 化,DESIGN.md / SKILL.md 成为 design system 的新包装。
- `A1 + B1`:agent harness 不再只是运行框架,还会自带 skill marketplace。
- `A4 + B1`:memory/context 基础设施也开始以 skill/plugin 形态分发。
- `E3 + K1`:用量、成本和 context 观测通常长得像菜单栏/statusline,但核心价值是观测。

## 6. 结构性观察

### 6.1 谁在做:个人仍多,组织开始生产线化

| owner_type | n | % |
|---|---|---|
| User | 414 | 58.9% |
| Organization | 289 | 41.1% |

Top 20 里个人账号仓库是 11/20,组织账号仓库是 9/20:个人品牌仍然强,但组织已经开始用多个仓库成套铺开。HKUDS、Vercel Labs、OpenAI、Anthropic、openclaw 都呈现出多项目扩散。

### 6.2 语言:TypeScript 和 Markdown 形态共同上升

| language | n | % |
|---|---|---|
| TypeScript | 206 | 29.3% |
| Python | 189 | 26.9% |
| — | 59 | 8.4% |
| JavaScript | 51 | 7.3% |
| Rust | 46 | 6.5% |
| Shell | 28 | 4.0% |
| Go | 26 | 3.7% |
| HTML | 22 | 3.1% |
| Swift | 19 | 2.7% |
| C | 11 | 1.6% |
| C++ | 8 | 1.1% |
| C# | 5 | 0.7% |
| Java | 5 | 0.7% |
| Kotlin | 5 | 0.7% |

TypeScript 仍是 agent 生态的胶水语言;B 系里也有一部分仓库没有传统主要语言。全数据集中 language 为空或未识别的仓库有 59 个,其中 42 个被 B 系覆盖。这类仓库的“代码”往往就是 Markdown:SKILL.md、CLAUDE.md、DESIGN.md 或目录化 prompt/config。即使有 Python/TypeScript 外壳,核心可复制单元也常常是这些 markdown 文件。

### 6.3 许可证:MIT 主导,但 no-license 风险很高

| license | n | % |
|---|---|---|
| MIT | 331 | 47.1% |
| Apache-2.0 | 116 | 16.5% |
| none | 113 | 16.1% |
| NOASSERTION | 72 | 10.2% |
| AGPL-3.0 | 42 | 6.0% |
| GPL-3.0 | 16 | 2.3% |
| CC0-1.0 | 4 | 0.6% |
| GPL-2.0 | 3 | 0.4% |
| Unlicense | 2 | 0.3% |
| CC-BY-SA-4.0 | 2 | 0.3% |

这也符合“小型个人项目 + markdown 交付物”的生态形态:传播快,商业复用边界不总是清楚。

### 6.4 创建时间:关注度窗口很短

| age | n | median avg ★/d | max avg ★/d | stars |
|---|---|---|---|---|
| ≤14d | 10 | 348 | 3117 | ~62k |
| 15-30d | 39 | 150 | 679 | ~191k |
| 31-60d | 162 | 85 | 5020 | ~1.41M |
| 61-90d | 151 | 52 | 1267 | ~1.14M |
| 91-120d | 156 | 39 | 1586 | ~1.64M |
| 121-180d | 185 | 29 | 2242 | ~1.8M |

这张表只做年龄校正,看的是当前 stars 除以仓库年龄后的平均速率,不和 §3.1 的单日峰值混用。它能提示一个粗略现象:新仓如果前期没有进入可见传播链路,后续自然抬升会更难。

---

## 7. 进一步判断

### 7.1 爆发单位从单个 repo 变成 wave

过去看开源项目,常常按“某个 repo 是否成功”来理解。现在更像是一个上游、一个格式或一个命名入口先被看见,随后在几周内长出一组相似项目:skills、awesome list、hosted wrapper、替代实现、可视化面板、教程和垂直版本。OpenClaw、DESIGN.md、CLI-Hub 都呈现这种 wave 形态。

### 7.2 命名和文件格式本身就是传播入口

`OpenClaw`、`Claude Code`、`DESIGN.md`、`CLI-Anything` 这类名字不只是项目名,也在充当搜索词、兼容声明和生态入口。B1/B2/B3 对应的 skills、CLAUDE.md、DESIGN.md 看起来像文档,实际更接近 agent 可执行的配置层。它们可复制、可安装、可组合,传播摩擦明显低于 SDK/package。

### 7.3 应用能力没有消失,而是在围绕上游拆分

研究、设计、浏览器自动化、创作者工具里,相当一部分表现为 B1 + C 系组合,不一定是独立 app。C 系按主类只有 96 个,按覆盖口径是 200 个,这 104 个差额说明应用能力正在被压进 skill/package,并围绕 Claude Code、OpenClaw、Codex、Gemini CLI 这类上游重新组织。

### 7.4 下一个值得看的问题:谁能形成周边

如果一个新项目只能自己增长,它更像单点应用;如果它能在短时间内带出 skills、awesome list、CLI、hosted wrapper、observability、教程和垂直版本,它就开始具备生态势能。这个口径比单看 stars 更能解释为什么某些仓库会迅速变成 GitHub 上的新中心。

GitHub AI repo 的高星增长至少包含三种不同机制:attention、replication 和 operation。stars 只能说明 attention;fork/star 才能观察 replication;issue/star 则提示真实使用后的 operational load。因此,这轮 GitHub AI 生态不是单纯“哪些 repo 最火”,而是哪些项目能从被看见走向被复制、被接入、被维护。

---

## 8. 标签说明:子门类详解

以下所有 N 和 stars 都是标签覆盖口径:主类或副类包含该标签即计入。

### A1 · agent-harness-cli

**覆盖仓库=125 · 覆盖 stars=~1.72M**

**做什么** · agent 的母仓和运行框架:CLI、gateway、personal assistant、agent OS。

**高星代表**
- **openclaw/openclaw** — ~370k★ · Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞
- **ultraworkers/claw-code** — ~191k★ · The repo is finally unlocked. enjoy the party! The fastest repo in history to surpass 100K stars.
- **paperclipai/paperclip** — ~64k★ · Open-source orchestration for zero-human companies

### A2 · coding-agent-ide

**覆盖仓库=67 · 覆盖 stars=~814k**

**做什么** · 绑定 IDE、编辑器或 coding UI 的 coding agent 工作台。

**高星代表**
- **affaan-m/everything-claude-code** — ~176k★ · The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Openco…
- **mattpocock/skills** — ~67k★ · Skills for Real Engineers. Straight from my .claude directory.
- **gsd-build/get-shit-done** — ~61k★ · A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

### A3 · agent-protocol

**覆盖仓库=33 · 覆盖 stars=~180k**

**做什么** · MCP / A2A / ACP 等协议,以及把外部工具暴露给 agent 的 server。

**高星代表**
- **HKUDS/CLI-Anything** — ~34k★ · "CLI-Anything: Making ALL Software Agent-Native"
- **jackwener/OpenCLI** — ~19k★ · Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime. Transform any website, Electron app, or local binary into a standardized…
- **vercel-labs/skills** — ~18k★ · The open agent skills tool - npx skills

### A4 · agent-memory

**覆盖仓库=34 · 覆盖 stars=~345k**

**做什么** · 给 agent 加记忆:memory system、context database、vector memory、persistent memory。

**高星代表**
- **666ghj/MiroFish** — ~60k★ · A Simple and Universal Swarm Intelligence Engine, Predicting Anything. 简洁通用的群体智能引擎，预测万物
- **MemPalace/mempalace** — ~52k★ · The best-benchmarked open-source AI memory system. And it's free.
- **safishamsi/graphify** — ~45k★ · AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, and more). Turn any folder of code, SQL schemas, R scripts, shell script…

### A5 · sandbox-runtime

**覆盖仓库=19 · 覆盖 stars=~121k**

**做什么** · agent 在哪跑:sandbox、microVM、container、virtual filesystem、受控运行环境。

**高星代表**
- **qwibitai/nanoclaw** — ~29k★ · A lightweight alternative to OpenClaw that runs in containers for security. Connects to WhatsApp, Telegram, Slack, Discord, Gmail and other messaging…
- **NVIDIA/NemoClaw** — ~20k★ · Run OpenClaw more securely inside NVIDIA OpenShell with managed inference
- **alibaba/OpenSandbox** — ~11k★ · Secure, Fast, and Extensible Sandbox runtime for AI agents.

### A6 · inference-serving

**覆盖仓库=18 · 覆盖 stars=~112k**

**做什么** · 模型怎么跑起来:本地推理、serving、量化、Apple Silicon / MLX / provider 选择。

**高星代表**
- **AlexsJones/llmfit** — ~26k★ · Hundreds of models & providers. One command to find what runs on your hardware.
- **Alishahryar1/free-claude-code** — ~23k★ · Use claude-code for free in the terminal, VSCode extension or discord like OpenClaw (voice supported)
- **jundot/omlx** — ~13k★ · LLM inference server with continuous batching & SSD caching for Apple Silicon — managed from the macOS menu bar

### B1 · skills-collection

**覆盖仓库=206 · 覆盖 stars=~2.77M**

**做什么** · 打包好的 SKILL.md / .claude/skills / agentic skills 包;装到 agent 上就能用。

**高星代表**
- **openclaw/openclaw** — ~370k★ · Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞
- **affaan-m/everything-claude-code** — ~176k★ · The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Openco…
- **forrestchang/andrej-karpathy-skills** — ~121k★ · A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.

### B2 · claude-md-config

**覆盖仓库=7 · 覆盖 stars=~140k**

**做什么** · CLAUDE.md / AGENTS.md / system prompt 单文件 super-prompt。

**高星代表**
- **forrestchang/andrej-karpathy-skills** — ~121k★ · A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.
- **drona23/claude-token-efficient** — ~5.2k★ · One CLAUDE.md file. Keeps Claude responses terse. Reduces output verbosity on heavy workflows. Drop-in, no code changes.
- **danveloper/flash-moe** — ~3.8k★ · Running a big model on a small laptop

### B3 · design-md-system

**覆盖仓库=5 · 覆盖 stars=~95k**

**做什么** · DESIGN.md 规范、design system token、给 coding agent 用的视觉规范。

**高星代表**
- **VoltAgent/awesome-design-md** — ~74k★ · A collection of DESIGN.md files inspired by popular brand design systems. Drop one into your project and let coding agents generate a matching UI.
- **google-labs-code/design.md** — ~12k★ · A format specification for describing a visual identity to coding agents. DESIGN.md gives agents a persistent, structured understanding of a design s…
- **Dammyjay93/interface-design** — ~4.8k★ · Design engineering for Claude Code. Craft, memory, and enforcement for consistent UI.

### B4 · prompt-library

**覆盖仓库=10 · 覆盖 stars=~90k**

**做什么** · 纯 prompt 集合或 prompt library;如果是 SKILL.md 形态则也会被 B1 覆盖。

**高星代表**
- **Leey21/awesome-ai-research-writing** — ~22k★ · Elevate your AI research writing, no more tedious polishing ✨
- **EvoLinkAI/awesome-gpt-image-2-API-and-Prompts** — ~14k★ · GPT-Image-2 API and Prompts
- **YouMind-OpenLab/awesome-nano-banana-pro-prompts** — ~12k★ · 🍌 World's largest Nano Banana Pro prompt library — 10,000+ curated prompts with preview images, 16 languages. Google Gemini AI image generation. Fre…

### B5 · awesome-list

**覆盖仓库=17 · 覆盖 stars=~161k**

**做什么** · 传统 awesome-X 列表;awesome-X-skills 这类会同时被 B1 覆盖。

**高星代表**
- **VoltAgent/awesome-design-md** — ~74k★ · A collection of DESIGN.md files inspired by popular brand design systems. Drop one into your project and let coding agents generate a matching UI.
- **hesamsheikh/awesome-openclaw-usecases** — ~31k★ · A community collection of OpenClaw use cases for making life easier.
- **openclaw/clawhub** — ~8.5k★ · Skill Directory for OpenClaw

### C1 · design-canvas-app

**覆盖仓库=34 · 覆盖 stars=~322k**

**做什么** · 用 agent 做设计的产品:画板、PPT、Figma 替代、AI 设计应用。

**高星代表**
- **nextlevelbuilder/ui-ux-pro-max-skill** — ~76k★ · An AI SKILL that provide design intelligence for building professional UI/UX multiple platforms
- **nexu-io/open-design** — ~34k★ · 🎨 Local-first, open-source alternative to Anthropic's Claude Design. ⚡ 19 Skills · ✨ 71 brand-grade Design Systems 🖼 Generate web · desktop · mobil…
- **pbakaus/impeccable** — ~26k★ · The design language that makes your AI harness better at design.

### C2 · creator-content

**覆盖仓库=21 · 覆盖 stars=~167k**

**做什么** · 视频、写作、短剧、屏幕录制、创作者工作流。

**高星代表**
- **jamiepine/voicebox** — ~25k★ · The open-source AI voice studio. Clone, dictate, create.
- **blader/humanizer** — ~18k★ · Claude Code skill that removes signs of AI-generated writing from text
- **heygen-com/hyperframes** — ~16k★ · Write HTML. Render video. Built for agents.

### C3 · coding-workflow-orchestration

**覆盖仓库=63 · 覆盖 stars=~663k**

**做什么** · 多 agent 编排、coding workflow、零人公司、autonomous workflow、swarm。

**高星代表**
- **garrytan/gstack** — ~92k★ · Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA
- **karpathy/autoresearch** — ~80k★ · AI agents running research on single-GPU nanochat training automatically
- **paperclipai/paperclip** — ~64k★ · Open-source orchestration for zero-human companies

### C4 · research-knowledge-work

**覆盖仓库=66 · 覆盖 stars=~743k**

**做什么** · AI 做研究、读论文、新闻/市场监控、知识工作和分析应用。

**高星代表**
- **karpathy/autoresearch** — ~80k★ · AI agents running research on single-GPU nanochat training automatically
- **666ghj/MiroFish** — ~60k★ · A Simple and Universal Swarm Intelligence Engine, Predicting Anything. 简洁通用的群体智能引擎，预测万物
- **koala73/worldmonitor** — ~54k★ · Real-time global intelligence dashboard. AI-powered news aggregation, geopolitical monitoring, and infrastructure tracking in a unified situational a…

### C5 · browser-web-automation

**覆盖仓库=20 · 覆盖 stars=~137k**

**做什么** · agent 开浏览器、headless browser for AI、web automation、爬虫 agent。

**高星代表**
- **vercel-labs/agent-browser** — ~32k★ · Browser automation CLI for AI agents
- **Panniantong/Agent-Reach** — ~19k★ · Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.
- **browser-use/browser-harness** — ~12k★ · Browser Harness / Self-healing harness that enables LLMs to complete any task.

### C6 · multimodal-app

**覆盖仓库=14 · 覆盖 stars=~89k**

**做什么** · 内置/调用图像、视频、语音生成的面向用户产品。

**高星代表**
- **Anionex/banana-slides** — ~14k★ · 一个基于nano banana pro🍌的原生AI PPT生成应用，迈向真正的＂Vibe PPT＂; 支持上传任意模板图片；上传任意素材&智能解析；一句话/大纲/页面描述自动生成PPT；口头修改指定区域、一键导出可编辑ppt - An AI-native slides generator bas…
- **hugohe3/ppt-master** — ~14k★ · AI generates natively editable PPTX from any document — real PowerPoint shapes with native animations, not images · by Hugo He
- **waooAI/waoowaoo** — ~12k★ · 首家工业级全流程 AI 影视生产平台。Industry-first professional AI Agent platform for controllable film & video production. From shorts to live-action with Hollywood-…

### D1 · training-finetuning

**覆盖仓库=5 · 覆盖 stars=~27k**

**做什么** · LoRA / DPO / GRPO / RL 等训练或微调框架。

**高星代表**
- **huggingface/skills** — ~10k★ · Give your agents the power of the Hugging Face ecosystem
- **elder-plinius/OBLITERATUS** — ~5.4k★ · OBLITERATE THE CHAINS THAT BIND YOU
- **Gen-Verse/OpenClaw-RL** — ~5.3k★ · OpenClaw-RL: Train any agent simply by talking

### D2 · model-architecture

**覆盖仓库=20 · 覆盖 stars=~79k**

**做什么** · 模型架构、从头复现、foundation model 实现、推理优化研究。

**高星代表**
- **kyegomez/OpenMythos** — ~12k★ · A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.
- **maderix/ANE** — ~6.7k★ · Training neural networks on Apple Neural Engine via reverse-engineered private APIs
- **zai-org/GLM-OCR** — ~6.3k★ · GLM-OCR: Accurate × Fast × Comprehensive

### D5 · security-disclosure

**覆盖仓库=5 · 覆盖 stars=~18k**

**做什么** · CVE 披露、kernel exploit、AI 安全漏洞披露。

**高星代表**
- **gommzystudio/device-activity-tracker** — ~4.9k★ · A phone number can reveal whether a device is active, in standby or offline (and more). This PoC demonstrates how delivery receipts + RTT timing leak…
- **aloshdenny/reverse-SynthID** — ~3.8k★ · reverse engineering Gemini's SynthID detection
- **theori-io/copy-fail-CVE-2026-31431** — ~3.6k★ · Copy Fail (CVE-2026-31431): 9-year-old Linux kernel LPE found by Theori's Xint Code

### F3 · media-gen-model

**覆盖仓库=26 · 覆盖 stars=~160k**

**做什么** · TTS、图像、视频、语音克隆、音乐生成等模型或生成服务本身。

**高星代表**
- **zai-org/Open-AutoGLM** — ~25k★ · An Open Phone Agent Model & Framework. Unlocking the AI Phone for Everyone
- **jamiepine/voicebox** — ~25k★ · The open-source AI voice studio. Clone, dictate, create.
- **nikopueringer/CorridorKey** — ~13k★ · Perfect Green Screen Keys

### F4 · 3d-spatial

**覆盖仓库=11 · 覆盖 stars=~45k**

**做什么** · 3D 重建、世界模型、空间智能。

**高星代表**
- **apple/ml-sharp** — ~8.3k★ · Sharp Monocular View Synthesis in Less Than a Second
- **microsoft/TRELLIS.2** — ~6.7k★ · Native and Compact Structured Latents for 3D Generation
- **Robbyant/lingbot-map** — ~6k★ · A feed-forward 3D foundation model for reconstructing scenes from streaming data

### E1 · education

**覆盖仓库=44 · 覆盖 stars=~247k**

**做什么** · 课程、tutorial、handbook、AI 工程学习路线、vibe coding 教学。

**高星代表**
- **HKUDS/DeepTutor** — ~24k★ · "DeepTutor: Agent-Native Personalized Learning Assistant"
- **2025Emma/vibe-coding-cn** — ~20k★ · <!-- ------------------------------------------------------------------------------- 项目头部区域 (HEADER) ------------------------------------------------…
- **THU-MAIC/OpenMAIC** — ~17k★ · Open Multi-Agent Interactive Classroom — Get an immersive, multi-agent learning experience in just one click

### E2 · hardware

**覆盖仓库=9 · 覆盖 stars=~73k**

**做什么** · 键盘、雷达、e-paper、机械臂、ESP32、真实物理产品。

**高星代表**
- **sipeed/picoclaw** — ~29k★ · Tiny, Fast, and Deployable anywhere — automate the mundane, unleash your creativity
- **NawfalMotii79/PLFM_RADAR** — ~20k★ · Open-source, low-cost 10.5 GHz PLFM phased array RADAR system
- **memovai/mimiclaw** — ~5.4k★ · MimiClaw: Run OpenClaw on a $5 chip. No OS(Linux). No Node.js. No Mac mini. No Raspberry Pi. No VPS. Hardware agents OS.

### E3 · fun-utility

**覆盖仓库=77 · 覆盖 stars=~512k**

**做什么** · 菜单栏、桌面 widget、账号切换、CLI helper、本地便利工具和 AI 周边。

**高星代表**
- **chenglou/pretext** — ~46k★ · Fast, accurate & comprehensive text measurement & layout
- **rtk-ai/rtk** — ~45k★ · CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies
- **lbjlaq/Antigravity-Manager** — ~29k★ · Professional Antigravity Account Manager & Switcher. One-click seamless account switching for Antigravity Tools. Built with Tauri v2 + React (Rust).专…

### J1 · ai-security-tool

**覆盖仓库=10 · 覆盖 stars=~214k**

**做什么** · 给 AI agent / LLM app 加安全防护的 guardrail、审计、red team、auth 工具。

**高星代表**
- **affaan-m/everything-claude-code** — ~176k★ · The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Openco…
- **nearai/ironclaw** — ~12k★ · IronClaw is an Agent OS focused on privacy, security and extensibility
- **mukul975/Anthropic-Cybersecurity-Skills** — ~6.1k★ · 754 structured cybersecurity skills for AI agents · Mapped to 5 frameworks: MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, D3FEND & NIST AI RMF · agentskil…

### K1 · eval-observe

**覆盖仓库=17 · 覆盖 stars=~162k**

**做什么** · eval、benchmark、leaderboard、observability/tracing、usage/cost/context 观测。

**典型代表**
- **jarrodwatts/claude-hud** — ~22k★ · A Claude Code plugin that shows what's happening - context usage, active tools, running agents, and todo progress
- **Wei-Shaw/sub2api** — ~19k★ · Sub2API-CRS2 一站式开源中转服务,让 Claude、Openai 、Gemini、Antigravity订阅统一接入,支持拼车共享,更高效分摊成本,原生工具无缝使用。
- **karpathy/llm-council** — ~19k★ · LLM Council works together to answer your hardest questions

### Z · long-tail

**覆盖仓库=106 · 覆盖 stars=~477k**

**做什么** · 跟 AI 生态没有直接关系或长尾 off-topic。

**高星代表**
- **xai-org/x-algorithm** — ~16k★ · Algorithm powering the For You feed on X
- **pranshuparmar/witr** — ~15k★ · Why is this running?
- **microsoft/RustTraining** — ~14k★ · Beginner, advanced, expert level Rust training material

---

## 9. 注意事项

1. `stars` 是关注度指标,不能直接代表质量;质量判断还需要结合 forks、issue/PR 处理、contributors、维护节奏、license 和真实使用反馈。
2. Top 20 的 `peak ★/day` 来自 GH Archive / ClickHouse GitHub events 的 `WatchEvent`,用于观察单日传播峰值。`WatchEvent` 只记录加星事件,不会扣掉 unstar;当前 stars 总数仍以 GitHub 展示值为准。
3. 公开研究已经显示 GitHub 存在 fake stars 和 star-buying 市场。本文没有检测 stargazer 账号行为异常,因此不对单个仓库的 stars 真伪做判断;所有 stars 相关结论只用于观察 attention、replication 和 operation 的相对结构。
4. 数据集只覆盖 `created:2025-11-09..2026-05-09 stars:>=2000`,窗口外上游项目仍然很重要,比如 `anthropics/skills`、`openai/codex`、`google-gemini/gemini-cli`。
5. 分类依赖标签定义和人工判断,边界类 K1/E3、A1/A2 仍然可能有个案争议。
6. 本文主统计按标签覆盖计数;同一仓库可以同时计入多个方向,所以跨类覆盖率和覆盖 stars 不应相加成 100%。

---

## 10. 配套材料

| 材料 | 说明 |
|---|---|
| 分类结果 | 703 条仓库的主类、副类和依据 |
| 标签说明 | 28 个标签定义、边界规则和清洗规则 |
| 全量分类表 | 便于阅读的仓库级分类表 |
| 原始输入 | 仓库元数据和 README 摘要 |
| 数据说明 | 样本口径、字段说明和复现说明 |

---

## 参考文件

- 数据说明:样本口径、字段说明和复现说明
- 全量分类表:仓库级标签、stars、forks 和 README 摘要
- 标签说明:标签定义和边界规则
