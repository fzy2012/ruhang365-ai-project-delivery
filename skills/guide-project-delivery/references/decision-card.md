# Decision card

Use this template only for a material choice. Present the recommendation before alternatives and translate technical differences into consequences the user can judge.

```markdown
## 需要你决定：<业务决定名称>

### 我的建议

选择 <方案名称>。

### 推荐理由

- <对最终效果的影响>
- <对成本或交付速度的影响>
- <对风险、数据或维护的影响>

### 其他选择

| 选择 | 能得到什么 | 主要代价或限制 | 适合什么情况 |
|---|---|---|---|
| A |  |  |  |
| B |  |  |  |

### 这项决定会影响

- <范围、体验、成本、数据、安全、锁定、维护或可逆性>

### 你只需要回复

回复“选择 A / B”，或补充你不能接受的条件。
```

Rules:

- Offer one option when only one is reasonable.
- Avoid asking the user to choose frameworks, protocols, databases, or infrastructure unless their consequences are the actual decision.
- State unknown cost, capability, or compliance facts as unknown and verify them before irreversible action.
- Do not present an assumption as user confirmation.
