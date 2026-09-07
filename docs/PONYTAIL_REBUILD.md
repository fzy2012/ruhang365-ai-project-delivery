# Ponytail 重做现场（2026-09-07）

## 已完成

- 孵化器新增先基线后增强的证据闸门，明确复用单位、已授权工作连续推进和交付声明边界；官方结构检查通过。
- 先前方法移植草稿可恢复保存在 ignored `runs/ponytail-rebuild-20260907/draft-backup/`。README 与核心 Skill 已精确恢复到 e4866ab；未采用破坏性 reset，也未改 V1 cases/rubric。
- 官方 Ponytail v4.9.0 已下载到 `/private/tmp/ponytail-baseline.IxBSrL/upstream`，HEAD 为 `0a4dd63ad4541f4f655c4108a295916f3c1d8fda`，MIT。
- 本次复用单位为 `skills/ponytail/SKILL.md`，不是整个插件。未执行上游安装器或 Hooks。
- 上游 Skill SHA256：`1316a2f3f95741d2300b116fe0c2d81ce4a9568656ed0a62643f54aaf09957f2`。
- 冻结输入 `runs/ponytail-rebuild-20260907/case.md`，SHA256：`fc0a5805ebd2ff15c3982b5d86bf1fcbe3e238f21a782ecf959af7263c4f3533`。

## 实际运行证据与限制

Codex CLI 显式读取原版 Skill，完成单文件设备借用表。输出保存于 `runs/ponytail-rebuild-20260907/baseline-output.md`。浏览器实际检查通过：空字段阻止登记、完整虚构数据生成记录、HTML 字样按普通文字呈现、刷新清空临时记录。产物为 `/private/tmp/ponytail-baseline.IxBSrL/baseline.html`。

CLI 使用 ignore-user-config、ephemeral、read-only，但仍加载全局 Skills 目录并报告 description budget 截短。请求使用 CLI 默认模型，输出没有 resolved-model 回执。因此这次是原版可行性 smoke，不是干净或可用于增益判断的正式基线。使用量回执为 input 46955、cached input 28672、output 784、reasoning output 83；未换算费用，不能作为纯 Ponytail 的成本。

## 恢复入口

下一步先解决基线运行的全局 Skills 污染并锁定模型/推理与工具环境，用同一冻结输入取得可复现原版结果；再从所选原版组件派生增强层。不能把这次 smoke 或旧版评测继承为增强版通过。验收仍包括原版优势不退化、至少一项用户结果可复现改善及陌生材料复验。

## 隔离修正与组件重做

后续通过本次进程 skills.config 禁用 113 个目录条目，并关闭 plugins、remote_plugin、memories。prompt-input 实测不含 Available skills 或 MEMORY.md。日常配置未改；该隔离排除了技能目录与长期记忆，不声称消除了宿主基础指令。

原版按显式 gpt-5.6-sol / medium 重跑完成，输出与事件在 runs/ponytail-rebuild-20260907/clean-baseline-*。浏览器验证空字段拦截、完整记录、安全文字、刷新清空均通过。usage：input 29305、cached input 13440、output 943、reasoning 174；不据此计算费用或声称成本降低。CLI 无 resolved-model 回执，服务端最终模型身份仍未独立确认。

基于这次有限原版行为证据，已完成本地组件式重做：references/ponytail-v4.9.0.md 保留上游 Skill 原文，SHA256 与上游完全一致；入口实现业务路径判断、逐步引导、验收和交接，只覆盖激活范围及输出方式。MIT 许可随包保留。ECC 未纳入。

增强版同材料运行使用相同配置与 case.md，差别为读取增强入口及其必要引用。它是显式原型对照，不是自动触发评测，不能证明模糊项目或陌生材料稳定增益。

重做开始时公开仓库基线为 e4866ab；重做版的发布与安装状态以当前 Git 历史和安装目录为准。本地重做与真实用户价值验收分别跟踪。

## 首个对照结果

增强版输出 enhanced-output.md 及原始事件已保存。相同浏览器检查（空值拦截、记录、安全文字、刷新清空）通过；实际读取了原版组件，也额外读取 acceptance 和 delivery 模板。增强 usage 为 input 64054、cached input 28032、output 2152、reasoning 826。原版与增强版均未发生真实数据或发布动作。

裁决：该明确小任务中，两版行为均可行，增强版没有证明更好的用户结果，且使用量更多。不能称增益成立，不发布为优于上游的版本。该案例只覆盖显式单文件原型，不覆盖模糊需求、自动路由、完整项目旅程或稳定性。原版和增强版的 resolved-model 均缺失，不将 usage 差异当成受控成本结论。

下一验证只应针对本产品真正的模糊项目引导切口；简单任务继续由原生能力或 Ponytail 处理。不得因这次结构/浏览器通过扩大为完整产品验收。若模糊项目也无稳定增益，应收敛为轻量适配而非继续扩建。
