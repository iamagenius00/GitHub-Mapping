# GitHub AI 生态近 6 个月 Mapping

这是一份关于 GitHub AI 热门仓库的系统梳理。

样本看的是过去 6 个月新建、并且达到 2000+ stars 的 AI repo。时间窗口是 `created:2025-11-09..2026-05-09`,一共 703 个仓库。

主报告在这里:

👉 [6month-map.md](./6month-map.md)

## 这份报告看什么

- 过去 6 个月,哪些 AI repo 在 GitHub 上获得了高关注度
- 这些 repo 主要集中在哪些方向:agent infra、skills/prompts、vertical apps、models/training、eval/observability 等
- 哪些项目只是被收藏,哪些更像被 fork、改造、部署或接入工作流
- 为什么 `SKILL.md` / `CLAUDE.md` / `DESIGN.md` 这类 markdown repo 开始成为 AI 软件的一种分发格式
- 哪些 owner 不只是做出一个爆款 repo,而是在围绕同一个入口持续做一组相关项目

## 怎么读

这份报告用 multi-label。每个仓库有 1 个主类和 0-2 个副类;一个 repo 只要主类或副类包含某个方向,就会被算进这个方向。所以不同方向的覆盖率不能直接相加成 100%。

这里的 stars 主要看作 attention 信号:它能说明一个项目被看见、被收藏、被传播,但不能直接代表代码质量、真实用户数或商业价值。报告里会结合 `peak ★/day`、`fork/star`、`issue/star`、最近 push 和 license 一起看。

如果只想快速看结论,可以先读主报告里的:

- `核心判断`
- `1. stars 先看关注度`
- `2. 宏观方向`
- `3. 高星项目集中在 distribution 层`

如果想查具体标签含义,看 `8. 标签说明:子门类详解`。

## 文件说明

```text
README.md          # 当前说明
6month-map.md      # 主报告
_raw/              # 当前报告对应的数据和脚本
```

`_raw/` 里保留的是当前报告会用到的材料:

- `repos-6m.jsonl`:703 个仓库的基础元数据
- `classified-6m.jsonl`:仓库标签和分类结果
- `citations-6m.json`:README 引用关系
- `classify-6m.py`:6 个月样本的分类脚本

## 更新

这份 mapping 会继续按月更新。后续如果样本口径、标签体系或数据源有变化,会直接写在报告开头。
