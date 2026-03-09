# Jarvis 新闻聚合器

 Jarvis 专用的多源新闻聚合技能，基于 cclank/news-aggregator-skill 优化。

## 功能

- 🤖 AI/Tech: Hugging Face, Hacker News, GitHub, Product Hunt
- 📰 加密: Cointelegraph, Decrypt, The Block, CryptoSlate
- 🎙️ 播客: Lex Fridman, Latent Space
- ✍️ 长文: Paul Graham, Wait But Why

## 使用方法

```bash
# 安装依赖
cd ~/.openclaw/workspace/skills/jarvis-news-aggregator
pip3 install -r requirements.txt

# 运行
python3 fetch.py --sources crypto,ai,github --limit 5

# 早报模式
python3 fetch.py --mode morning

# 晚汇报
python3 fetch.py --mode evening
```

## 支持的数据源

| 源 | 说明 | 命令 |
|---|---|---|
| crypto | 加密货币新闻 | --sources crypto |
| ai | AI/科技新闻 | --sources ai |
| github | GitHub Trending | --sources github |
| hackernews | Hacker News | --sources hackernews |
| huggingface | Hugging Face 论文 | --sources huggingface |

## 集成到早报

在 morning-report.sh 中添加:
```bash
python3 ~/.openclaw/workspace/skills/jarvis-news-aggregator/fetch.py --mode morning --limit 3
```