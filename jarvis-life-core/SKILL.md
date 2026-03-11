---
name: jarvis-life-core
description: >
  Jarvis 核心生活系统 - 日程管理 + 提醒 + 备忘录 + 天气 + 个人信息。
  基于 weather, things-mac, apple-notes, apple-reminders, daily-briefing 精华重构。
  功能：日历、提醒、笔记、天气、生活助手。
---

# Jarvis Life Core

 Jarvis 自主研发的核心生活技能，整合多个生活/效率技能的最佳实践。

## 核心功能

- **日程管理**: 日历查看、事件创建、冲突检测
- **提醒事项**: 待办、定时提醒、重复任务
- **备忘录**: Apple Notes / Bear 笔记管理
- **天气查询**: 当前天气、预报、空气质量
- **个人助理**: 生日提醒、健康跟踪、家庭事务
- **日常简报**: 每日摘要、新闻推送、晚间总结

## 架构

```
jarvis-life-core/
├── SKILL.md
├── _meta.json
├── config/
│   ├── preferences.json   # 用户偏好
│   ├── schedule.json      # 日程配置
│   └── routines.json      # 日常routine
├── scripts/
│   ├── calendar.py        # 日历管理
│   ├── reminders.py       # 提醒管理
│   ├── notes.py           # 笔记管理
│   ├── weather.py         # 天气查询
│   └── briefing.py        # 日常简报
└── storage/
    ├── schedule.json      # 日程数据
    └── briefing_history.json # 历史简报
```

## 使用方式

### 日程

```bash
# 今日日程
today

# 本周日程
week

# 添加事件
event "团队会议" --time 14:00 --date 2026-03-07
```

### 提醒

```bash
# 列出提醒
reminders list

# 添加提醒
reminder "检查邮件" --at 09:00 --repeat daily

# 完成提醒
reminder done 1
```

### 笔记

```bash
# 列出笔记
notes list

# 创建笔记
note create "会议记录" --content "..."

# 搜索笔记
notes search "项目"
```

### 天气

```bash
# 当前天气
weather

# 天气预报
weather forecast 3d
```

### 简报

```bash
# 早间简报
morning-brief

# 晚间简报
evening-brief
```

## 已整合技能

| 原技能 | 整合功能 |
|--------|---------|
| weather | 天气查询 |
| things-mac | Things 3 任务管理 |
| apple-notes | Apple 备忘录 |
| apple-reminders | Apple 提醒事项 |
| daily-briefing | 每日简报 |

## 日常 Routine

### 早上 8:00
- 天气检查
- 日程查看
- 加密新闻推送

### 下午
- 定时提醒检查
- 重要事件预警

### 晚上 22:00
- 交易总结
- 晚间简报
- 记忆整理

## 用户偏好

- 语言: 中文
- 时区: CST (GMT-6)
- 重要日期: 伟伟健康、小八月生日、宠物成长

## 版本历史

- **2026-03-06 v1.0.0**: 初始版本，整合 5 个生活/效率技能的核心功能

## 下一步更新计划

- [ ] 添加更多日历集成 (Google Calendar)
- [ ] 完善提醒重复规则
- [ ] 添加 AI 笔记整理
- [ ] 增强简报个性化