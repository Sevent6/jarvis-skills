---
name: jarvis-comm-core
description: >
  Jarvis 核心通讯系统 - 多平台消息聚合 + 社交媒体监控。
  基于 telegram-bot, neynar, x-reader, imsg, wacli 精华重构。
  功能：Telegram 消息、Farcaster Cast、X/Twitter 读取、WhatsApp 同步。
---

# Jarvis Comm Core

 Jarvis 自主研发的核心通讯技能，整合多个通讯/社交技能的最佳实践。

## 核心功能

- **Telegram**: 消息发送/读取、群组管理、机器人命令
- **Farcaster**: Cast 读取/发送、用户搜索、频道订阅
- **X/Twitter**: 帖子读取、用户分析、趋势追踪
- **WhatsApp**: 消息同步、群组管理
- **iMessage**: 消息读取（本地）
- **统一收件箱**: 跨平台消息聚合

## 架构

```
jarvis-comm-core/
├── SKILL.md
├── _meta.json
├── config/
│   ├── platforms.json     # 平台配置
│   ├── filters.json        # 消息过滤规则
│   └── notifications.json  # 通知规则
├── scripts/
│   ├── telegram.py        # Telegram 处理
│   ├── farcaster.py        # Farcaster 处理
│   ├── twitter.py          # X/Twitter 处理
│   ├── inbox.py            # 统一收件箱
│   └── monitor.py          # 消息监控
└── storage/
    ├── messages.json       # 消息历史
    └── contacts.json       # 联系人
```

## 使用方式

### Telegram

```bash
# 发送消息
comm send telegram --chat-id 123456 --message "Hello"

# 读取消息
comm read telegram --chat-id 123456 --limit 10

# 群组管理
comm telegram groups --list
```

### Farcaster

```bash
# 读取 Cast
cast read --fid 123

# 发送 Cast
cast post "Hello Warpcast!"

# 搜索
cast search "ethereum"
```

### X/Twitter

```bash
# 读取帖子
x read @username --limit 10

# 读取帖子链接
x read https://x.com/user/status/123

# 用户信息
x user @username
```

### 统一收件箱

```bash
# 聚合消息
inbox --platforms telegram,farcaster,x

# 搜索所有平台
inbox search "bitcoin"
```

## 已整合技能

| 原技能 | 整合功能 |
|--------|---------|
| telegram-bot | Telegram 机器人 |
| neynar | Farcaster API |
| x-reader | X/Twitter 读取 |
| imsg | iMessage 读取 |
| wacli | WhatsApp 同步 |
| baoyu-skills | 小红书/公众号/X自动发布 |

## 监控规则

1. **关键词监控**: BTC, ETH, DeFi, 重要新闻
2. **用户监控**: 关注 KOL、机构账号
3. **趋势追踪**: 热门话题、趋势标签
4. **异常检测**: 大额转账、关键新闻

## 版本历史

- **2026-03-06 v1.1.0**: 整合 baoyu-skills，新增小红书/公众号/X自动发布
- **2026-03-06 v1.0.0**: 初始版本，整合 5 个通讯/社交技能的核心功能

## 下一步更新计划

- [x] 内容自动发布 (小红书/公众号/X)
- [ ] 添加更多平台 (Discord, Slack)
- [ ] 完善情感分析
- [ ] 添加定时报告