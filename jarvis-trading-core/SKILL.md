---
name: jarvis-trading-core
description: >
  Jarvis 核心交易系统 - 多交易所聚合 + 投资组合管理 + 信号检测 + 鲸鱼监控 + AI多Agent决策。
  基于 binance-pro, hyperliquid-trading, bankr, polymarket-api, defi-yield-scanner, crypto-whale-monitor, virattt/ai-hedge-fund 精华重构。
  支持：Binance, Hyperliquid, Base, Ethereum, Polygon, Solana, Unichain。
  功能：现货/合约交易、仓位管理、收益率扫描、交易信号、鲸鱼追踪、AI投资人团队决策。
---

# Jarvis Trading Core

 Jarvis 自主研发的核心交易技能，整合多个交易技能的最佳实践。

## 核心功能

- **多交易所支持**: Binance (现货/合约), Hyperliquid (合约), Base (链上), Ethereum, Polygon, Solana
- **投资组合聚合**: 跨交易所资产汇总，计算总 PnL
- **交易执行**: 市价/限价单、杠杆管理、仓位控制
- **信号检测**: RSI, MACD, 布林带等技术指标信号
- **收益率扫描**: DeFi 收益率对比，Yield Farming 机会
- **鲸鱼追踪**: 大户钱包监控，潜在信号检测
- **预测市场**: Polymarket 事件预测
- **AI多Agent决策**: 12位传奇投资人+4分析Agent+风控团队

## 决策规则

### AI Hedge Fund 多Agent决策（借鉴 virattt/ai-hedge-fund）

#### 12位传奇投资人Agent
- Warren Buffett - 寻找伟大公司，合理价格买入
- Charlie Munger - Wonderful business at fair price
- Bill Ackman - 激进投资者，敢于重仓
- Cathie Wood - 成长投资，创新与颠覆
- Michael Burry - 反向交易，深度价值
- Ben Graham - 安全边际，保守估值
- Peter Lynch - 寻找10倍股
- Phil Fisher - 深入调研，"scuttlebutt"方法
- Mohnish Pabrai - 低风险套利
- Stanley Druckenmiller - 不对称机会
- Aswath Damodaran - 估值专家
- Rakesh Jhunjhunwala - 印度Big Bull

#### 4个分析Agent
- Valuation Agent - 内在价值计算
- Sentiment Agent - 市场情绪分析
- Fundamentals Agent - 基本面分析
- Technicals Agent - 技术指标分析

#### 决策流程
```
12投资人Agent → 4分析Agent → Risk Manager → Portfolio Manager → 最终决策
```

### 开仓条件
- RSI < 30 (超卖) 或 RSI > 70 (超买)
- MACD 金叉/死叉
- 布林带触及上下轨

### 仓位控制
- 单笔不超过总资金 10%
- 杠杆根据波动率调整 (2x-5x)
- 止损 2%，止盈 6%

### 信号优先级
- 鲸鱼地址大额转账 → 关注
- 多指标共振 → 强烈信号
- 合约资金费率异常 → 预警

## 已整合技能

| 原技能 | 整合功能 |
|--------|---------|
| binance-pro | Binance API 交易 |
| hyperliquid-trading | Hyperliquid 合约 |
| bankr | 多链交易、NLP 命令 |
| polymarket-api | 预测市场 |
| defi-yield-scanner | 收益率扫描 |
| crypto-whale-monitor | 鲸鱼监控 |
| bankr-signals | 交易信号 |
| virattt/ai-hedge-fund | 多Agent投资人团队决策 (2026-03-10) |

## 使用方式

### 投资组合

```bash
# 查看总资产
portfolio

# 查看各交易所资产
portfolio --detail

# 计算 PnL
pnl --period 24h
```

### 交易

```bash
# 开多仓
buy BTC 0.01 --leverage 5 --exchange hyperliquid

# 开空仓
sell ETH 0.1 --leverage 3 --exchange binance
```

### 信号

```bash
# 技术信号
signal BTC --indicators rsi,macd,bb

# 交易信号建议
signal --action analyze
```

### AI Hedge Fund 多Agent决策

```bash
# 启动AI投资团队分析
analyze BTC --team

# 启动特定风格投资人分析
analyze BTC --agent warren,cathie,michael_burry

# 风险检查
analyze BTC --risk-check
```

## 版本历史

- **2026-03-10 v1.2.0**: 整合 virattt/ai-hedge-fund - 多Agent投资人团队决策（12传奇投资人+4分析Agent+风控）
- **2026-03-06 v1.1.0**: 新增扑克交易理念框架
- **2026-03-06 v1.0.0**: 初始版本，整合 7 个交易技能的核心功能