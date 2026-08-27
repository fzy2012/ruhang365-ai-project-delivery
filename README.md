# AI 全流程项目共创与交付框架

入行365原创的 AI 项目交付向导，帮助没有代码基础的用户把一个想法推进为可选择、可实施、可验证、可维护和可交接的项目。

## 当前状态

**Preview。** Skill 核心、参考模板和冻结评测已经建立；正式显式评测与隔离环境隐式路由均已通过，GitHub 安装路径也已在隔离目录验证。当前仍需完成真实新用户安装验收和重复稳定性验证，不能把单次受控运行写成长期稳定。

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

- 项目骨架：Phase 1 本地搭建完成
- Skill schema：官方结构验证与本地静态合同已通过
- Codex 项目：已登记到用户指定目录
- 独立前向评测：正式显式评测 3 个案例 × 3 个裁判全部通过，零 critical violation
- 隐式触发：隔离干净环境中 3/3 项目正例正确触发、5/5 普通任务负例未误触发；重复稳定性仍待验证
- 安装路径：官方 GitHub 安装器已在隔离临时目录验证，安装内容与仓库 Skill 一致
- 全局安装：未执行
- 远程仓库：已创建 <https://github.com/fzy2012/ruhang365-ai-project-delivery>，并配置为本仓库 `origin`
- 入行实验室：Preview 已在 RHZL Production 发布，并明确区分简化模板与需要安装的完整 Skill
- 生产发布：RHZL 介绍页已发布；Skill 本身不需要独立部署
- 用户价值：尚未完成真实新用户从发现、安装到首次自动触发的独立验收

本项目采用 [MIT License](LICENSE)。

## 继续开发

下一道产品闸门是邀请一位此前未参与评测的 Codex 用户，按本页安装入口完成首次使用；实现、安装、自动触发和用户是否真正得到帮助分别记录。
