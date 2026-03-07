---
name: jarvis-search-core
description: >
  Jarvis 核心搜索系统 - 多引擎聚合 + 智能爬虫 + 浏览器自动化。
  基于 multi-search-engine, tavily, browser-automation, deep-scraper, playwright-scraper-skill 精华重构。
  功能：网页搜索、数据抓取、浏览器控制、内容提取。
---

# Jarvis Search Core

 Jarvis 自主研发的核心搜索技能，整合多个搜索/爬虫技能的最佳实践。

## 核心功能

- **多引擎搜索**: 同时调用 SearXNG, Tavily, Brave, Google 等
- **智能爬虫**: 深度抓取、动态页面处理、IP 轮换
- **浏览器自动化**: 截图、表单填写、点击操作、滚动
- **内容提取**: Markdown/HTML 转换、关键信息提取
- **结果聚合**: 去重、排序、相关性评分

## 架构

```
jarvis-search-core/
├── SKILL.md
├── _meta.json
├── config/
│   ├── engines.json       # 搜索引擎配置
│   ├── scraper.json       # 爬虫配置
│   └── browser.json       # 浏览器配置
├── scripts/
│   ├── search.py          # 多引擎搜索
│   ├── scraper.py         # 智能爬虫
│   ├── browser.py         # 浏览器控制
│   └── extractor.py       # 内容提取
└── storage/
    ├── cache.json         # 搜索缓存
    └── results.json       # 历史结果
```

## 使用方式

### 搜索

```bash
# 多引擎搜索
search "Bitcoin price" --engines searxng,tavily

# AI 优化搜索
search "crypto news" --ai

# 聚合结果
search "DeFi yield" --dedup
```

### 爬虫

```bash
# 深度抓取
scrape https://example.com --depth 3

# 动态页面
scrape https://example.com --wait-for selector

# 批量抓取
scrape --urls file.txt --parallel 5
```

### 浏览器

```bash
# 截图
browser screenshot https://example.com

# 截图并点击
browser click --url https://example.com --selector button.submit

# 填写表单
browser fill --url https://example.com --data '{"email": "test@example.com"}'
```

### 内容提取

```bash
# 提取为 Markdown
extract https://example.com --format markdown

# 提取关键信息
extract https://example.com --fields title,author,date
```

## 已整合技能

| 原技能 | 整合功能 |
|--------|---------|
| multi-search-engine | 多引擎搜索聚合 |
| tavily | AI 优化搜索 |
| browser-automation | 浏览器控制 |
| deep-scraper | 深度爬虫 |
| playwright-scraper-skill | Playwright 自动化 |
| stealth-browser | 隐身浏览器 |
| union-search-skill | 28+平台聚合搜索 |
| agent-reach | AI访问全网(小红书/抖音/微信/公众号) |
| defuddle | 网页正文提取去广告 |

## 搜索策略

1. **简单查询**: SearXNG (本地，快速)
2. **AI 理解**: Tavily (语义理解)
3. **综合**: 多引擎聚合 + 去重
4. **爬虫优先级**: 静态 → 动态 → 浏览器

## 缓存策略

- 搜索结果: 24 小时
- 页面内容: 7 天
- 去重: URL + 标题相似度 > 0.8

## 版本历史

- **2026-03-06 v1.2.0**: 整合 agent-reach(中文平台) + defuddle(正文提取)
- **2026-03-06 v1.1.0**: 整合 union-search-skill，新增 28+ 平台支持
- **2026-03-06 v1.0.0**: 初始版本，整合 6 个搜索/爬虫技能的核心功能

## 下一步更新计划

- [x] 添加更多搜索引擎 (Google, Bing, 百度)
- [x] 集成中文平台 (小红书, 抖音, B站, 知乎)
- [x] 正文提取能力 (defuddle)
- [ ] 集成代理池
- [ ] 搜索日志功能