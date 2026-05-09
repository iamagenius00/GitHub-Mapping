# Addendum · 主 map 之外的"窗口上游"

> 主 map (`2026-05-09-github-3month-map.md`) 用的 query 是 `created:>=2026-02-09 stars:>=1000`,所以**只看新 repo**。
> 但榜单 top 50 的 README 里反复点名了一批 **创建在窗口之外、但被窗口内项目当地基** 的 repo。
> 这一层不补,会得出"skill / agent-harness / design 是凭空爆发"的错误叙事——其实它们站在 4-5 个 200d+ 老仓库的肩膀上。

抓取时间 2026-05-09。源:top 50 enriched README + GitHub API metadata。

---

## 1) 真正的"地基层"(创建在窗口外,但仍在涨)

| repo | stars | age | stars/day | 主 map 中的引用者 | 是什么 |
|---|---|---|---|---|---|
| **openclaw/openclaw** | 369.9k | 165d | 2242 | THU-MAIC/OpenMAIC + 几乎所有 `claw-*` / `claw3D` / `OpenClaw-*` 命名的 repo | "Your own personal AI assistant. Any OS. Any Platform. 🦞" — 整个 `claw` 生态的母船 |
| **NousResearch/hermes-agent** | 139.4k | 290d | 481 | garrytan/gbrain | "The agent that grows with you" |
| **anthropics/skills** | 130.6k | 228d | 573 | (隐式) addyosmani/agent-skills, MiniMax-AI/skills, slavingia/skills 全部对位它 | Anthropic 官方 Skills 仓库——**整个 skills-ecosystem lane 的事实标准** |
| **google-gemini/gemini-cli** | 103.5k | 386d | 268 | santifer/career-ops, Gitlawb/openclaude 等 | Google 官方 Gemini agent CLI |
| **karpathy/nanochat** | 53.1k | 207d | 257 | karpathy/autoresearch (主 map #10) | autoresearch 跑在它上面;两个仓库共生 |
| **multica-ai/multica** | 26.3k | 115d | 229 | nexu-io/open-design (主 map #2) | "managed agents platform";open-design 直接抄它的 daemon-and-runtime 架构 |
| **OpenBMB/VoxCPM** | 17.9k | 234d | 76 | THU-MAIC/OpenMAIC | tokenizer-free 多语言 TTS——voice-audio lane 的真上游 |
| **VoltAgent/voltagent** | 8.7k | 387d | 23 | VoltAgent/awesome-design-md (主 map #4, 73k★) | 老的 TS agent 框架——但 VoltAgent 这个**组织**靠 awesome-design-md 单 repo 突然进入 top |

> **观察**:这 8 个加起来 75 万星,等于**一个隐形的"前 92 天"层**。主 map 看到的爆发,大半是这层在过去 2-12 个月铺好后,过去 90 天突然被引爆。

## 2) 主 map 里被高频引用、但单独没被收录的"姊妹仓库"

这些是榜单 top 50 仓库的衍生/工具,作者把它们拆成多 repo 分发——星数还不够 1k,但跟主仓共生:

| repo | stars | age | 主仓 | 关系 |
|---|---|---|---|---|
| JuliusBrussee/cavekit | 862 | 55d | caveman (#5) | NL→blueprint→build plan,作者另一个工具 |
| sympozium-ai/sympozium | 475 | 74d | (协议层) | "Coordination Layer for Multi-Agent AI" |
| bergside/awesome-design-skills | 426 | 60d | nexu-io/open-design (#2) | 67 个 DESIGN/SKILL 文件,被 open-design 整包 vendoring |
| JuliusBrussee/cavemem | 325 | 21d | caveman (#5) | 同作者的 cross-agent memory |
| garrytan/gbrain-evals | 99 | 16d | garrytan/gstack (#6) | Garry Tan 第三个仓库,evals 配 gstack |

## 3) 同期高星的"刚好擦边"项目(创建在窗口边缘)

VoltAgent/awesome-design-md(38d, 73.5k★)、heygen-com/hyperframes(60d, 16.2k★)、alchaincyf/huashu-design(19d, 12.7k★)、op7418/guizang-ppt-skill(15d, 5.9k★)、OpenCoworkAI/open-codesign(20d, 5.3k★)——这五个都**在窗口内、已经收录**,没问题。但它们和 nexu-io/open-design(主 map #2) 是**同一个内容簇**——open-design 的 README 把这 5 个全列为"开源肩膀"。

把这 6 个看成一个**"design-as-document"集团**:
- design.md (Google) + awesome-design-md (VoltAgent, 73k) — spec 层
- huashu / guizang-ppt — 中文 skill 层
- open-codesign + open-design — 应用层 + 商业对位 Claude Design
- hyperframes — 视频/HTML 输出层

合计已经 14 万+ 星,2 个月内形成。**这是主 map 漏分析的 sub-lane:design-as-document 集团**。

---


## 数据局限

- 只 enrich 了主 map top 50 的 README,所以"被引用"的统计基数小(每个候选 1-4 mention)。
- 没做 anthropics/skills 这种"隐式引用"——很多 skills repo 不直接 link 它,但模式上对位。要更准要做语义匹配。
- openclaw/openclaw 369k 这个数字异常大,需单独 verify(可能是 official 仓库 + 大量 promotion;不像 sybil)。
- 没拉这 8 个上游的 commit timing,无法判断它们和窗口内爆发是否有"协调发布"关系。

数据原料:`_raw/upstream_enriched.json`(刚生成)、`_raw/readmes.json`、`_raw/final_v2.jsonl`。
