"""
Jarvis Evolver - 自动技能分析器
自动分析所有已安装技能，定期更新分析结果
"""

import os
import json
from datetime import datetime
from typing import Dict, List, Any, Optional

class AutoAnalyzer:
    """自动技能分析器 - 分析全部技能 + 增量分析新技能"""
    
    def __init__(self, skills_dir: str = None, memory_dir: str = None):
        self.skills_dir = skills_dir or os.path.expanduser("~/.openclaw/workspace/skills")
        self.memory_dir = memory_dir or os.path.expanduser("~/.openclaw/workspace/memory")
        self.analysis_file = os.path.join(self.memory_dir, "skill-analysis.json")
        
        os.makedirs(self.memory_dir, exist_ok=True)
    
    def _analyze_skill(self, skill_name: str) -> Dict[str, Any]:
        """分析单个技能"""
        skill_path = os.path.join(self.skills_dir, skill_name)
        
        if not os.path.exists(skill_path):
            return {"error": f"Skill {skill_name} not found"}
        
        analysis = {
            "name": skill_name,
            "path": skill_path,
            "core_functions": self._extract_core_functions(skill_path),
            "dependencies": self._extract_dependencies(skill_path),
            "tools_used": self._extract_tools(skill_path),
            "patterns": self._extract_patterns(skill_path),
            "improvement_suggestions": self._generate_suggestions(skill_path)
        }
        
        return analysis
    
    def _extract_core_functions(self, skill_path: str) -> List[str]:
        """提取核心功能"""
        functions = []
        skill_md = os.path.join(skill_path, "SKILL.md")
        
        if os.path.exists(skill_md):
            with open(skill_md, 'r') as f:
                content = f.read()
                if "## 功能" in content:
                    start = content.find("## 功能")
                    end = content.find("\n##", start + 1)
                    if end > 0:
                        funcs_text = content[start:end]
                        for line in funcs_text.split('\n'):
                            if line.strip().startswith('- '):
                                functions.append(line.strip()[2:])
        
        return functions
    
    def _extract_dependencies(self, skill_path: str) -> List[str]:
        """提取依赖关系"""
        deps = []
        pkg_file = os.path.join(skill_path, "package.json")
        if os.path.exists(pkg_file):
            try:
                with open(pkg_file, 'r') as f:
                    pkg = json.load(f)
                    deps.extend(pkg.get("dependencies", {}).keys())
            except:
                pass
        
        req_file = os.path.join(skill_path, "requirements.txt")
        if os.path.exists(req_file):
            with open(req_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        deps.append(line)
        
        return deps
    
    def _extract_tools(self, skill_path: str) -> List[str]:
        """提取使用的工具"""
        tools = []
        skill_md = os.path.join(skill_path, "SKILL.md")
        if os.path.exists(skill_md):
            with open(skill_md, 'r') as f:
                content = f.read()
                keywords = ["exec", "read", "write", "browser", "message", "web_search", "tavily"]
                for kw in keywords:
                    if f"`{kw}`" in content or f" {kw} " in content:
                        tools.append(kw)
        
        return list(set(tools))
    
    def _extract_patterns(self, skill_path: str) -> List[str]:
        """提取代码模式"""
        patterns = []
        for root, dirs, files in os.walk(skill_path):
            for file in files:
                if file.endswith(('.py', '.js', '.ts', '.sh')):
                    filepath = os.path.join(root, file)
                    try:
                        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                            if "try:" in content or "try {" in content:
                                patterns.append("error_handling")
                            if "for " in content or "while " in content:
                                patterns.append("loop_processing")
                            if "if " in content:
                                patterns.append("conditional_logic")
                            if "def " in content or "function " in content:
                                patterns.append("function_definition")
                    except:
                        pass
        
        return list(set(patterns))
    
    def _generate_suggestions(self, skill_path: str) -> List[str]:
        """生成改进建议"""
        suggestions = []
        has_test = False
        for root, dirs, files in os.walk(skill_path):
            for f in files:
                if "test" in f.lower():
                    has_test = True
        
        if not has_test:
            suggestions.append("建议添加单元测试")
        
        skill_md = os.path.join(skill_path, "SKILL.md")
        if not os.path.exists(skill_md):
            suggestions.append("缺少 SKILL.md 文档")
        
        return suggestions
    
    def _list_installed_skills(self) -> List[str]:
        """列出所有已安装的技能"""
        if not os.path.exists(self.skills_dir):
            return []
        
        skills = []
        for item in os.listdir(self.skills_dir):
            item_path = os.path.join(self.skills_dir, item)
            if os.path.isdir(item_path):
                if os.path.exists(os.path.join(item_path, "SKILL.md")) or \
                   os.path.exists(os.path.join(item_path, "_meta.json")):
                    skills.append(item)
        
        return sorted(skills)
    
    def analyze_all(self, force: bool = False) -> Dict[str, Any]:
        """分析所有技能"""
        
        existing = {}
        if os.path.exists(self.analysis_file) and not force:
            with open(self.analysis_file, 'r') as f:
                existing = json.load(f)
        
        current_skills = set(self._list_installed_skills())
        existing_skills = set(existing.keys())
        
        new_skills = current_skills - existing_skills
        updated_skills = set()
        
        for skill_name in current_skills:
            skill_path = os.path.join(self.skills_dir, skill_name)
            skill_mtime = os.path.getmtime(skill_path)
            
            if skill_name in existing:
                prev_mtime = existing[skill_name].get('_mtime', 0)
                if skill_mtime > prev_mtime:
                    updated_skills.add(skill_name)
            else:
                new_skills.add(skill_name)
        
        print(f"📊 技能分析: {len(new_skills)} 新增, {len(updated_skills)} 更新")
        
        for skill_name in new_skills | updated_skills:
            try:
                analysis = self._analyze_skill(skill_name)
                skill_path = os.path.join(self.skills_dir, skill_name)
                
                existing[skill_name] = {
                    'functions': analysis.get('core_functions', [])[:5],
                    'tools': analysis.get('tools_used', []),
                    'patterns': analysis.get('patterns', []),
                    'dependencies': analysis.get('dependencies', []),
                    'suggestions': analysis.get('improvement_suggestions', []),
                    '_mtime': os.path.getmtime(skill_path),
                    '_analyzed': datetime.now().isoformat()
                }
            except Exception as e:
                print(f"  ⚠️ {skill_name}: {e}")
        
        with open(self.analysis_file, 'w') as f:
            json.dump(existing, f, indent=2, ensure_ascii=False)
        
        return {
            'total': len(existing),
            'new': len(new_skills),
            'updated': len(updated_skills),
            'analysis_file': self.analysis_file
        }
    
    def get_stats(self) -> Dict[str, Any]:
        """获取统计信息"""
        
        if not os.path.exists(self.analysis_file):
            return {'error': 'No analysis data'}
        
        with open(self.analysis_file, 'r') as f:
            analyses = json.load(f)
        
        tool_count = {}
        pattern_count = {}
        
        for name, data in analyses.items():
            for t in data.get('tools', []):
                tool_count[t] = tool_count.get(t, 0) + 1
            for p in data.get('patterns', []):
                pattern_count[p] = pattern_count.get(p, 0) + 1
        
        return {
            'total_skills': len(analyses),
            'tool_usage': tool_count,
            'pattern_usage': pattern_count,
            'last_analyzed': max(
                (a.get('_analyzed', '') for a in analyses.values()),
                default=''
            )
        }
    
    def categorize_skills(self) -> Dict[str, List[str]]:
        """按功能分类技能"""
        
        categories = {
            '交易/加密': ['binance-pro', 'hyperliquid-cli', 'hyperliquid-trading', 
                        'polymarket-api', 'defi-yield-scanner', 'bankr', 'clanker', 'yoink',
                        'crypto-whale-monitor', 'bankr-signals'],
            '搜索/浏览器': ['multi-search-engine', 'tavily', 'browser-automation', 
                          'stealth-browser', 'deep-scraper', 'playwright-scraper-skill', 'apify'],
            '通讯/社交': ['telegram-bot', 'neynar', 'imsg', 'wacli', 'x-reader'],
            '信息/新闻': ['news-summary', 'news-aggregator', 'crypto-news', 'blogwatcher'],
            '多Agent/自主': ['multi-agent-cn', 'multi-agent-roles', 'autonomous-feature-planner', 
                           'self-evolving-skill-1-0-2', 'capability-evolver', 'evolver'],
            '代码/开发': ['code-review', 'github', 'ollama-local', 'coding-agent'],
            '数据/存储': ['lily-memory', 'memory', 'gog'],
            '生活/效率': ['weather', 'things-mac', 'apple-notes', 'apple-reminders', 'daily-briefing'],
            'OnChain/DeFi': ['onchainkit', 'endaoment', 'ens-primary-name', 'erc-8004', 
                            'botchan', 'veil', 'qrcoin', 'zapper', 'base']
        }
        
        with open(self.analysis_file, 'r') as f:
            analyses = json.load(f)
        
        result = {}
        for cat, skills in categories.items():
            result[cat] = [s for s in skills if s in analyses]
        
        all_categorized = set()
        for skills in categories.values():
            all_categorized.update(skills)
        
        result['未分类'] = [s for s in analyses.keys() if s not in all_categorized]
        
        return result


if __name__ == "__main__":
    analyzer = AutoAnalyzer()
    result = analyzer.analyze_all()
    print("分析结果:", result)
    stats = analyzer.get_stats()
    print("\n统计:", json.dumps(stats, indent=2))
    categories = analyzer.categorize_skills()
    print("\n分类:", json.dumps(categories, indent=2, ensure_ascii=False))