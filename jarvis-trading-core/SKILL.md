---
name: jarvis-trading-core
description: >
  Jarvis 核心交易系统 - 多交易所聚合 + 投资组合管理 + 信号检测 + 鲸鱼监控。
  基于 binance-pro, hyperliquid-trading, bankr, polymarket-api, defi-yield-scanner, crypto-whale-monitor 的精华重构。
  支持：Binance, Hyperliquid, Base, Ethereum, Polygon, Solana, Unichain。
  功能：现货/合约交易、仓位管理、收益率扫描、交易信号、鲸鱼追踪。
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

## 架构

```
jarvis-trading-core/
├── SKILL.md                   # 本文档
├── _meta.json                 # 元数据
├── config/                    # 配置文件
│   ├── exchanges.json        # 交易所配置
│   ├── signals.json          # 信号规则
│   └── whale_watch.json      # 鲸鱼监控列表
├── scripts/                  # 执行脚本
│   ├── portfolio.py          # 组合管理
│   ├── signals.py            # 信号检测
│   ├── scanner.py            # 收益率扫描
│   └── whale.py              # 鲸鱼追踪
└── storage/                  # 数据存储
    ├── positions.json        # 当前仓位
    ├── pnl.json              # 盈亏记录
    └── signals.json          # 历史信号
```

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

# 市价成交
market BTC/USDT --side buy --amount 0.01

# 限价单
limit BTC 50000 --amount 0.01 --side sell
```

### 信号

```bash
# 技术信号
signal BTC --indicators rsi,macd,bb

# 交易信号建议
signal --action analyze

# 历史信号
signal --history
```

### 收益率扫描

```bash
# 扫描收益率
yield --chain base

# 找最佳收益
yield --sort apy
```

### 鲸鱼监控

```bash
# 查看大户动态
whale --watch

# 添加监控地址
whale --add 0x...

# 历史追踪
whale --history
```

## 决策规则

### 1. 开仓条件
- RSI < 30 (超卖) 或 RSI > 70 (超买)
- MACD 金叉/死叉
- 布林带触及上下轨

### 2. 仓位控制
- 单笔不超过总资金 10%
- 杠杆根据波动率调整 (2x-5x)
- 止损 2%，止盈 6%

### 3. 信号优先级
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

## 版本历史

- **2026-03-06 v1.0.0**: 初始版本，整合 7 个交易技能的核心功能
  - 多交易所支持
  - 投资组合聚合
  - 技术信号检测
  - 收益率扫描
  - 鲸鱼监控

## 下一步更新计划

- [ ] 添加 AI 交易策略模块
- [ ] 集成更多链 (Arbitrum, Optimism)
- [ ] 添加期权交易支持
- [ ] 完善风控系统