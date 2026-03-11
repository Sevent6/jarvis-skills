---
name: Jarvis Evolver
description: >
  Jarvis 自主进化框架 - 技能消化、经验封装、自动化决策。
  核心功能：理解技能本质 → 总结最佳实践 → 封装成自己的版本 → 上传GitHub。
  适用于：深度理解复杂技能、创建个性化工作流、构建决策支持系统。
---

## 核心理念

**技能不在于多，而在于理解、使用、总结，然后封装成自己的版本。**

## 功能

- **技能消化器**: 深入理解现有技能的原理，提取核心逻辑
- **经验总结器**: 从使用记录中提取模式，形成最佳实践
- **技能封装器**: 将消化后的知识封装成新的个性化技能
- **决策引擎**: 基于历史决策构建判断框架，辅助未来决策

## 架构

```
jarvis-evolver/
├── SKILL.md                   # 本文档
├── core/
│   ├── skill_analyzer.py      # 技能分析器 - 理解技能本质
│   ├── pattern_extractor.py  # 模式提取器 - 从使用中学习
│   ├── skill_builder.py       # 技能构建器 - 封装新技能
│   ├── decision_engine.py    # 决策引擎 - 辅助判断
│   └── memory.py             # 记忆持久化
├── templates/                 # 技能模板
│   ├── basic-skill.yaml
│   └── advanced-skill.yaml
└── storage/                   # 数据存储
    ├── patterns.json         # 提取的模式
    ├── decisions.json        # 历史决策
    └── skills/               # 封装的技能
```

## 核心算法

### 1. 技能分析 (Skill Analysis)

```python
analyzer = SkillAnalyzer()
analysis = analyzer.analyze(skill_path)

# 输出:
# - core_functions: 核心功能列表
# - dependencies: 依赖关系
# - patterns: 使用模式
# - improvement_suggestions: 改进建议
```

### 2. 模式提取 (Pattern Extraction)

从使用历史中提取重复模式：
- 命令序列模式
- 决策树模式
- 错误恢复模式
- 成功路径模式

### 3. 决策框架 (Decision Framework)

```
输入 → 特征提取 → 历史相似度匹配 → 决策建议 → 执行 → 结果记录
```

## 使用方式

### 分析现有技能

```bash
# 分析一个技能的核心逻辑
analyze-skill <skill-name>

# 提取使用模式
extract-patterns --days 7

# 生成技能报告
skill-report <skill-name>
```

### 封装新技能

```bash
# 基于分析结果创建新技能
create-skill --name "my-custom-skill" --template advanced

# 添加决策规则
add-decision --skill <skill-id> --condition "market_volatility > 0.3" --action "reduce_exposure"
```

### 决策支持

```bash
# 获取决策建议
decide --context "BTC price action" --history-similarity 0.8

# 记录决策结果
record-decision --context "..." --decision "hold" --result "success"
```

## 决策原则

### 交易决策
- **趋势跟随**: MACD 金叉买入，死叉卖出
- **风险管理**: 单笔亏损不超过 2%
- **仓位控制**: 根据波动率调整仓位

### 技能选择
- **复杂度匹配**: 简单任务用简单技能
- **可靠性优先**: 优先选择评分高的技能
- **自主度**: 可自主完成 vs 需要人工批准

### 系统维护
- **预防优先**: 定期检查健康状态
- **快速恢复**: 问题发生后立即尝试修复
- **记忆持久化**: 重要决策必须记录

## 文件位置

| 路径 | 说明 |
|------|------|
| `~/.openclaw/workspace/skills/jarvis-evolver` | 技能根目录 |
| `~/.openclaw/workspace/skills/jarvis-evolver/storage` | 数据存储 |

## 演进日志

- **2026-03-06**: 初始版本，基于 autonomous-feature-planner 和 self-evolving-skill 的思想创建
- 核心目标：理解 → 总结 → 封装 → 上传