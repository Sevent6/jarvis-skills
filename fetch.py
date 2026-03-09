#!/usr/bin/env python3
"""
Jarvis 新闻聚合器
支持加密、AI、GitHub 等多源新闻
"""

import argparse
import json
import subprocess
from datetime import datetime

# 配置
SOURCES = {
    'crypto': {
        'cointelegraph': 'https://cointelegraph.com/rss',
        'decrypt': 'https://decrypt.co/feed',
        'cryptoslate': 'https://cryptoslate.com/feed/',
    },
    'ai': {
        'hackernews': 'https://news.ycombinator.com/rss',
        'github': 'https://github.com/trending.rss',
    },
    'github': {
        'github': 'https://github.com/trending.rss',
    },
    'hackernews': {
        'hackernews': 'https://news.ycombinator.com/rss',
    },
    'huggingface': {
        'huggingface': 'https://huggingface.co/feeds/blog',
    }
}

def fetch_rss(url, limit=5):
    """获取 RSS 源"""
    import feedparser
    try:
        feed = feedparser.parse(url)
        items = []
        for entry in feed.entries[:limit]:
            items.append({
                'title': entry.get('title', ''),
                'link': entry.get('link', ''),
            })
        return items
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []

def format_output(data, mode='default'):
    """格式化输出"""
    output = []
    
    if mode == 'morning':
        output.append("📰 今日要闻\n")
    elif mode == 'evening':
        output.append("🌙 晚汇报 - 今日要闻\n")
    else:
        output.append("📊 新闻聚合\n")
    
    for source, items in data.items():
        if not items:
            continue
        
        emoji = {
            'cointelegraph': '📰',
            'decrypt': '🔓',
            'cryptoslate': '🧪',
            'hackernews': '🦄',
            'github': '🐙',
            'huggingface': '🤗'
        }.get(source, '📌')
        
        output.append(f"\n{emoji} {source.upper()}")
        for i, item in enumerate(items, 1):
            title = item['title'][:60] + '...' if len(item['title']) > 60 else item['title']
            output.append(f"{i}. {title}")
    
    return '\n'.join(output)

def fetch_sources(sources, limit=5):
    """获取指定源的数据"""
    results = {}
    
    for source in sources:
        if source in SOURCES:
            all_items = []
            for name, url in SOURCES[source].items():
                items = fetch_rss(url, limit)
                all_items.extend(items)
            
            # 去重
            seen = set()
            unique_items = []
            for item in all_items:
                if item['title'] not in seen:
                    seen.add(item['title'])
                    unique_items.append(item)
            
            results[source] = unique_items[:limit]
        else:
            print(f"Unknown source: {source}")
    
    return results

def main():
    parser = argparse.ArgumentParser(description='Jarvis 新闻聚合器')
    parser.add_argument('--sources', default='crypto,ai', help='数据源 (逗号分隔)')
    parser.add_argument('--limit', type=int, default=5, help='每个源的数量')
    parser.add_argument('--mode', default='default', choices=['default', 'morning', 'evening'])
    parser.add_argument('--json', action='store_true', help='JSON 输出')
    
    args = parser.parse_args()
    
    sources = [s.strip() for s in args.sources.split(',')]
    data = fetch_sources(sources, args.limit)
    
    if args.json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        print(format_output(data, args.mode))

if __name__ == '__main__':
    main()