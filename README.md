# AI 项目引导

帮助非技术项目负责人描述目标后，调查现成产品、开源项目和 API，选择合适路线，并逐步获得可用结果。引导 Skill 独立工作；需要开发时可与 Ponytail 的实现简化能力配合。

## 当前状态

**2026-09-27 互动引导 Preview。** 需求确认后，项目引导在方案取舍、首次可体验和重要反馈处主动与负责人讨论，把回答转成受影响的需求与验收，再继续已授权工作。实施、专业任务和续聊仍承接原目标；独立问答及小修改保持轻量。隔离行为结果见 [互动试用记录](evals/guidance-dialogue-result.2026-09-27.md)；成本、真实项目长期表现和用户验收仍未证实。公开仓库分发、安装和真实使用效果分别验收。Ponytail v4.10.0 的核心 Skill 与保留的 v4.9.0 原文一致，来源核对见 [许可与上游说明](skills/guide-project-delivery/references/ponytail-license.md)。

**2026-09-10 本地候选记录。** 本项目内的真实项目请求由项目规则引导加载 `skills/guide-project-delivery/SKILL.md`；显示名称已调整，技术路径保持兼容。当时尚未将候选同步到公开仓库。这里的迭代是规则与案例改进，不是模型训练；自动触发、实际引导效果及成本仍需真实使用验证。

以下为已有 Preview 的历史说明，不是本轮候选的验收结果。

**Ponytail 重做版处于 Preview。** 原版 v4.9.0 Skill 以原文组件随包保留，入口负责项目引导与激活范围适配；不包含上游插件 Hooks。来源、运行证据和限制见 [重做回执](docs/PONYTAIL_REBUILD.md)。以下旧版评测与公开状态对应 e4866ab，不能继承为重做版通过。

当前精简 Preview 将实施原则精简进入口，原文仅在核查来源或上游行为时读取。用户只描述目标，在需要时看到简明进度和业务决定，交付以真实可用结果为准。成本验收上限为同等质量、同一目标下相对 Codex 单独使用增加不超过 10%，优先持平或下降；这是待验证要求，尚未证明达标。对照口径见 [评测协议](evals/protocol.md#outcome-and-cost-gate--2026-09-08)。代码分发、安装成功与行为和成本达标分别验收。

**旧版 Preview 证据。** Skill 核心、参考模板和冻结评测已经建立；正式显式评测与隔离环境隐式路由曾通过，GitHub 安装路径也已在隔离目录验证。当前仍需完成真实新用户安装验收和重复稳定性验证，不能把单次受控运行写成长期稳定。

## 核心承诺

> 用户牢牢控制目标、体验、成本和风险；AI 判断“买、配、连、改、建”的合理路径，并对技术实现和验证证据负责。

它解决的不是“如何让零代码用户学会指挥程序员”，而是五个更直接的问题：

1. 这个目标是否真的需要开发？
2. 哪种交付方式最适合当前阶段？
3. 用户真正需要决定什么？
4. 做到什么程度才算完成？
5. 完成后如何使用、维护、恢复和交接？

## 工作流

```text
目标与能力预检
→ 任务复杂度路由
→ 买 / 配 / 连 / 改 / 建
→ 推荐优先的关键决策
→ 用户验收 + 工程验收
→ 明确授权后实施
→ 真实运行与证据
→ 项目交付卡
```

## 仓库结构

```text
skills/guide-project-delivery/  可安装 Skill 核心
docs/                           产品规格、验收和实验室接入合同
evals/                          冻结案例、协议和评分标准
scripts/validate_project.py     本地静态合同验证
runs/                           独立评测原始输出，默认不进入 Git
```

## V1 使用场景

- 完全不会代码的用户想从零完成一个项目；
- 需要先比较现成产品、配置集成、低代码、局部开发和自研；
- 需要把业务目标转成决策、验收和交付闭环；
- 现有项目将发生范围、数据、权限、成本或上线方式的重要变化。

以下任务默认不走完整流程：

- 明确的小 Bug；
- 单一文案或样式修改；
- 只读代码审查或问题解释；
- 一次性低风险命令。

除非用户明确要求完整交付流程，这些任务应使用轻量模式。

## 安装到 Codex

以下远程安装命令获取公开仓库 `main` 上的版本；本项目内的试用由 `AGENTS.md` 加载本地源文件。安装后的内容应与目标提交的 Skill 目录核对。

最简单的方式是在 Codex 中发送下面这句话：

```text
请安装这个 Skill：https://github.com/fzy2012/ruhang365-ai-project-delivery/tree/main/skills/guide-project-delivery
安装完成后告诉我，并提醒我新建一个 Codex 任务开始使用。
```

也可以使用 Codex 自带的官方安装器：

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo fzy2012/ruhang365-ai-project-delivery \
  --path skills/guide-project-delivery
```

安装成功后，新建一个 Codex 任务，直接描述项目想法即可，例如：

```text
我想做一个帮助新员工完成入职手续的内部工具，但不知道应该购买、配置现有系统，还是自己开发。请带我一步步推进。
```

日常使用不需要点名 `guide-project-delivery`。Codex 会在“非技术用户、目标模糊、需要比较交付路径或端到端推进”的项目场景中自动匹配；纯问答、代码审查、故障诊断、状态报告和孤立小修改不会进入完整项目流程。

### 更新、停用与恢复

- 更新：先关闭 Codex，把 `~/.codex/skills/guide-project-delivery` 移到 Skill 目录之外作为备份，再重新执行安装；验证新版本后再处理备份。
- 临时停用：把该目录移出 `~/.codex/skills/`，然后新建 Codex 任务验证它不再被发现。
- 恢复：关闭 Codex，把备份目录移回 `~/.codex/skills/guide-project-delivery`，再新建任务使用。
- 安装器发现同名目录时会停止，不要覆盖现有目录；先保留备份，确保回退路径有效。

## 本地验证

```bash
python3 /Users/fzy/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/guide-project-delivery
python3 scripts/validate_project.py
python3 -m json.tool evals/cases/cases.v1.json >/dev/null
git diff --check
```

## 状态边界

以下旧版行为证据对应 e4866ab，不代表当前精简 Preview 通过；安装版本需要在使用者本机单独核验。

- 项目骨架：Phase 1 本地搭建完成
- Skill schema：官方结构验证与本地静态合同已通过
- Codex 项目：已登记到用户指定目录
- 独立前向评测：正式显式评测 3 个案例 × 3 个裁判全部通过，零 critical violation
- 隐式触发：隔离干净环境中 3/3 项目正例正确触发、5/5 普通任务负例未误触发；重复稳定性仍待验证
- 安装路径：官方 GitHub 安装器已在隔离临时目录验证，安装内容与仓库 Skill 一致
- 全局安装：按使用者环境单独执行；应从已推送的精确版本安装，核对文件一致性并保留旧版备份，不能由代码发布推断本机已更新
- 远程仓库：已创建 <https://github.com/fzy2012/ruhang365-ai-project-delivery>，并配置为本仓库 `origin`
- 入行实验室：Preview 已在 RHZL Production 发布，并明确区分简化模板与需要安装的完整 Skill
- 生产发布：RHZL 介绍页已发布；Skill 本身不需要独立部署
- 用户价值：尚未完成真实新用户从发现、安装到首次自动触发的独立验收

本项目采用 [MIT License](LICENSE)。

## 继续开发

先在本项目中用真实需求试用“AI 项目引导”，检查是否主动发现合适的现成方案、给出有依据的推荐并推进到约定结果。针对实际缺口迭代，保留冻结评测；按评测协议做同材料对照后，才判断增强是否有效。与 Ponytail 组合时需单独检验两者是否冲突以及总成本，不能用安装成功代替组合效果。公开发布和实验室接入分别验收。
