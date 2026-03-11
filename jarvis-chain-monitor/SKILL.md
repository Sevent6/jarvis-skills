---
name: jarvis-chain-monitor
description: 实时链上监控 - BTC价格、链上数据、鲸鱼交易警报
---

# jarvis-chain-monitor

JARVIS 实时链上监控系统，每分钟检查市场数据。

## 功能

- **价格监控**: BTC 价格实时追踪，波动 >2% 自动警报
- **链上数据**: 24h 交易数、交易额、哈希率
- **鲸鱼探测**: 监控高手续费交易（潜在的大额转账）
- **后台运行**: 持续监控，不打扰主进程

## 使用方法

```bash
# 启动监控
node ~/.openclaw/workspace/scripts/whale-alert.js &

# 查看状态
ps aux | grep whale-alert
```

## 告警规则

| 类型 | 阈值 | 动作 |
|------|------|------|
| 价格波动 | >2% | 标记 ⚠️ |
| 高手续费交易 | >100 sat/vB | 标记 🐳 |

## 集成

- 配合 jarvis-trading-core 做交易决策
- 配合 jarvis-comm-core 发送警报到 Telegram