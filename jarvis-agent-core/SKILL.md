---
name: jarvis-agent-core
description: >
  Jarvis 核心多Agent系统 - 任务分发 + 能力进化 + 自主决策。
  基于 capability-evolver, self-evolving-skill-1-0-2, autonomous-feature-planner, multi-agent-cn, multi-agent-roles, jarvis-evolver 精华重构。
  功能：子Agent管理、任务委派、能力分析、自动进化(理解→总结→封装→上传)、决策引擎。
---

# Jarvis Agent Core

 Jarvis 自主研发的核心多Agent技能，整合多个多Agent/自主系统技能的最佳实践。

## 核心功能

- **子Agent管理**: 创建、监控、终止子Agent
- **任务分发**: 根据任务复杂度选择合适的Agent
- **能力分析**: 分析现有技能，提取核心逻辑
- **自动进化**: 技能对比、更新、优化
- **决策引擎**: 基于规则的智能决策
- **记忆管理**: 长期记忆、上下文保持
- **Forum协作**: 多Agent辩论式讨论（借鉴 BettaFish ForumEngine）

## 架构

```
jarvis-agent-core/
├── SKILL.md
├── _meta.json
├── config/
│   ├── agents.json        # Agent 配置
│   ├── rules.json         # 决策规则
│   └── evolution.json     # 进化配置
├── scripts/
│   ├── manager.py         # Agent 管理器
│   ├── dispatcher.py      # 任务分发
│   ├── analyzer.py        # 能力分析
│   ├── evolver.py         # 自动进化
│   └── memory.py          # 记忆管理
└── storage/
    ├── agent_state.json   # Agent 状态
    ├── evolution_log.json # 进化日志
    └── decisions.json     # 决策记录
```

## 使用方式

### Agent 管理

```bash
# 列出子Agent
agent list

# 委派任务
agent delegate --task "分析BTC走势" --to jarvistrx

# 终止 Agent
agent kill jarvistrx
```

### 任务分发

```bash
# 自动选择 Agent
task "分析这个PR" --auto

# 指定 Agent
task "复杂策略分析" --agent jarvistrx

# 本地任务
task "处理私人财务" --agent jarvistrx-private
```

### 能力分析

```bash
# 分析技能
analyze skill bankr

# 分析所有技能
analyze all

# 生成报告
analyze report
```

### 自动进化

```bash
# 检查更新
evolve check

# 执行进化
evolve run

# 查看历史
evolve history
```

### 决策

```bash
# 交易决策
decide trade --symbol BTC --action buy

# 技能选择
decide skill --task "搜索新闻"
```

### Forum 协作（多Agent辩论模式）

```bash
# 启动 Forum 讨论
forum start --topic "BTC未来走势预测" --agents jarvistrx,crypto-news-bot

# 复杂任务：多Agent并行 → 初步分析 → 策略制定 → 深度辩论 → 结论
# 借鉴 BettaFish ForumEngine：每个Agent有独立工具集和思维模式
# 主持人引导讨论，避免同质化，催生集体智能
```

## Forum 协作流程（借鉴 BettaFish）

1. **用户提问** → 主Agent接收
2. **并行启动** → 多个子Agent同时开始工作
3. **初步分析** → 各Agent使用专属工具进行概览
4. **策略制定** → 基于初步结果制定研究策略
5. **深度辩论** (循环):
   - 各Agent基于Forum主持人引导进行专项研究
   - ForumEngine监控发言并生成主持人引导
   - 各Agent根据讨论调整研究方向
6. **结果整合** → 主Agent收集所有分析结果
7. **报告生成** → 输出结构化结论

## Agent 选择规则

| 任务类型 | Agent | 模型 |
|---------|-------|------|
| 简单查询 | main | MiniMax-M2.5 |
| 复杂推理 | jarvistrx | DeepSeek V3 |
| 私人数据 | jarvistrx-private | Qwen3:14b |
| 加密新闻 | crypto-news-bot | Gemini Flash |

## 已整合技能

| 原技能 | 整合功能 |
|--------|---------|
| capability-evolver | 能力进化引擎 |
| self-evolving-skill | 自主进化 |
| autonomous-feature-planner | 自主功能规划 |
| multi-agent-cn | 多Agent协作 |
| multi-agent-roles | Agent角色管理 |
| **BettaFish/ForumEngine** | Agent辩论协作机制 (2026-03-10) |
| **MiroFish** | 群体智能预测引擎 (2026-03-10) |

## 决策规则

### 交易规则
- RSI < 30 → 买入信号
- RSI > 70 → 卖出信号
- MACD 金叉 → 买入
- 资金费率异常 → 预警

### 技能选择规则
- 代码/推理 → jarvistrx
- 搜索/查询 → tavily
- 交易执行 → bankr
- 社交媒体 → x-reader

### 系统维护规则
- 内存 > 150KB → 自动清理
- PM2 进程 down → 重启
- 隧道不可达 → 修复

## 版本历史

- **2026-03-10 v1.2.0**: 整合 BettaFish ForumEngine（Agent辩论协作）+ MiroFish（群体智能预测）
- **2026-03-10 v1.1.0**: 整合 jarvis-evolver 进化框架 → 技能理解→总结→封装→上传
- **2026-03-06 v1.0.0**: 初始版本，整合 5 个多Agent/自主系统技能的核心功能

## 下一步更新计划

- [ ] 添加更多 Agent 类型
- [ ] 完善进化机制
- [ ] 添加学习反馈
- [ ] 增强决策准确性