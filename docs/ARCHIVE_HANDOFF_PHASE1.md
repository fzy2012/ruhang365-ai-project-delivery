# Phase 1 归档交接

## 可验收目标

把“零代码用户项目交付母 Prompt”升级为独立源码项目、可安装 Skill、冻结评测和入行实验室接入合同，并由独立 Codex 任务承接 Phase 2。

## 已完成

- 独立项目位于 `/Users/fzy/其他项目/ruhang365-AI 全流程项目共创与交付框架`。
- `main` 的核心提交为 `6d267a5`，Phase 1 回执提交为 `d75850e`。
- `guide-project-delivery` 已覆盖轻量/完整/高保障路由、“买配连改建”、推荐优先决策、双层验收、证据状态和项目交付卡。
- 官方 Skill 校验、项目静态合同、评测 JSON 和 Git 差异检查均已通过。
- Codex 独立项目 ID 为 `54ab7e82-b102-441c-9ffc-879e966f0e94`。
- 续作任务为 `01a008a2-768a-73e1-b00c-89e8bfd4c2a0`，已完整读取原任务、原始需求对话和当前仓库，并重新核验 Phase 1 基线。

## 当前证据边界

- 全局 Skill：未安装。
- 前向评测：三个案例已冻结，尚无独立模型运行结果。
- Git 远程与推送：未创建、未执行。
- RHZL：只有接入合同，未修改。
- Preview、Production、公开证明、用户验收和业务结果：均未执行或未取得。

## 已确认产品边界

- 本仓库是方法、Skill、模板、评测和版本的真相源。
- RHZL 只负责入行实验室介绍、发现入口、场景推荐和 Workflow 承接。
- “加入入行实验室”不等于建设独立网站，也不等于已授权修改 RHZL 或发布生产。
- 专业开发 Skill 负责具体实现；本 Skill 负责编排，不发展成吸收所有技术领域的超级 Skill。

## 下一步

1. Phase 2A 先在被忽略的 `runs/` 中创建并冻结两个确定性 fixture。
2. 在 Skill 尚未全局安装时运行三个 baseline 独立任务。
3. 保存原始输出并按冻结 rubric 评分，完成后停在安装闸门。
4. 用户明确授权后再进入全局安装、三个显式触发和三个隐式触发评测。
5. 远程仓库、公开 Core、RHZL 接入和生产发布继续保持独立授权与证据链。

## 不要重复

- 不要重新讨论是否做成独立项目或重做 Phase 1。
- 不要先安装 Skill 再补 baseline，否则会污染对照组。
- 不要向被测任务泄露 expected behavior、forbidden behavior 或 rubric。
- 不要把结构验证或单次模型结果包装成用户价值、生产可用或因果提升。
- 不要在 RHZL 当前共享脏工作区直接接入；届时从最新远端基线建立干净 worktree。

## Reactivation prompt

```text
继续开发 AI 全流程项目共创与交付框架。先读取 AGENTS.md、docs/PHASE1_RECEIPT.md、docs/ARCHIVE_HANDOFF_PHASE1.md、evals/protocol.md 和当前 Git 状态。Phase 1 已完成，直接从 Phase 2A 开始：在 runs/ 中建立并冻结两个确定性 fixture，运行三个安装前 baseline，保存原始证据并按冻结 rubric 评分；完成后停在全局 Skill 安装闸门。不得安装 Skill、推送、修改 RHZL、部署、发布或使用生产数据，除非老板在续作任务中明确授权。
```

## 归档判定

原评估与建项任务在本文件、Leon 交接、Codex 记忆候选完成落盘并通知续作任务后可以归档。Phase 2 属于独立项目的新生命周期。
