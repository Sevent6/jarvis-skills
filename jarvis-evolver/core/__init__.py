"""
Jarvis Evolver - Core Modules
技能分析、决策引擎、技能构建器
"""

# 技能分析器
class SkillAnalyzer:
    """技能分析器 - 理解技能本质"""
    
    def __init__(self, skills_dir: str = None):
        import os
        self.skills_dir = skills_dir or os.path.expanduser("~/.openclaw/workspace/skills")
        self.analysis_cache = {}
    
    def analyze(self, skill_name: str):
        """分析一个技能"""
        import os
        skill_path = os.path.join(self.skills_dir, skill_name)
        
        if not os.path.exists(skill_path):
            return {"error": f"Skill {skill_name} not found"}
        
        return {
            "name": skill_name,
            "path": skill_path,
            "core_functions": [],
            "tools_used": [],
            "patterns": []
        }
    
    def list_installed_skills(self):
        """列出所有已安装的技能"""
        import os
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


# 导出
from .auto_analyzer import AutoAnalyzer
from .decision_engine import DecisionEngine
from .skill_builder import SkillBuilder

__all__ = ['SkillAnalyzer', 'AutoAnalyzer', 'DecisionEngine', 'SkillBuilder']