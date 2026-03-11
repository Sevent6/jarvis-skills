"""
Jarvis Evolver - 技能构建器
将消化后的知识封装成新的个性化技能
"""

import os
import json
import shutil
from datetime import datetime
from typing import Dict, List, Any, Optional
from pathlib import Path

class SkillBuilder:
    """技能构建器 - 封装新技能"""
    
    def __init__(self, workspace_dir: str = None, storage_dir: str = None):
        self.workspace_dir = workspace_dir or os.path.expanduser("~/.openclaw/workspace")
        self.storage_dir = storage_dir or os.path.join(
            self.workspace_dir, "skills/jarvis-evolver/storage"
        )
        self.skills_dir = os.path.join(self.workspace_dir, "skills")
        
        os.makedirs(self.storage_dir, exist_ok=True)
        os.makedirs(os.path.join(self.storage_dir, "skills"), exist_ok=True)
    
    def create_skill(self, name: str, description: str, 
                     core_functions: List[str] = None,
                     template: str = "basic") -> Dict[str, Any]:
        """创建新技能"""
        
        # 技能路径
        skill_path = os.path.join(self.skills_dir, name)
        
        if os.path.exists(skill_path):
            return {"error": f"Skill {name} already exists"}
        
        # 创建目录
        os.makedirs(skill_path, exist_ok=True)
        
        # 创建 SKILL.md
        self._create_skill_md(skill_path, name, description, core_functions or [])
        
        # 创建 _meta.json
        self._create_meta_json(skill_path, name, description)
        
        # 创建核心代码
        if template == "advanced":
            self._create_advanced_skill(skill_path, name, description)
        else:
            self._create_basic_skill(skill_path, name)
        
        return {
            "success": True,
            "name": name,
            "path": skill_path,
            "message": f"Skill {name} created successfully"
        }
    
    def _create_skill_md(self, skill_path: str, name: str, description: str,
                         functions: List[str]) -> None:
        """创建 SKILL.md"""
        
        content = f"""---
name: {name}
description: >
  {description}
---

## 功能

"""
        for func in functions:
            content += f"- {func}\n"
        
        if not functions:
            content += "- （待添加功能）\n"
        
        content += f"""

## 使用方式

```bash
# 使用此技能
{name} <command>
```

## 注意事项

- 创建时间: {datetime.now().strftime("%Y-%m-%d %H:%M")}
- 基于 Jarvis Evolver 框架生成
- 需要根据实际使用情况进行调整

## 演进日志

- **{datetime.now().strftime("%Y-%m-%d")}**: 初始版本创建
"""
        
        with open(os.path.join(skill_path, "SKILL.md"), 'w') as f:
            f.write(content)
    
    def _create_meta_json(self, skill_path: str, name: str, description: str) -> None:
        """创建 _meta.json"""
        
        meta = {
            "name": name,
            "description": description,
            "version": "1.0.0",
            "created": datetime.now().isoformat(),
            "author": "Jarvis Evolver",
            "tags": ["auto-generated", "custom"]
        }
        
        with open(os.path.join(skill_path, "_meta.json"), 'w') as f:
            json.dump(meta, f, indent=2)
    
    def _create_basic_skill(self, skill_path: str, name: str) -> None:
        """创建基础技能结构"""
        
        # 创建主文件
        main_py = f'''#!/usr/bin/env python3
"""
{name} - Auto-generated skill
"""

import sys

def main(args):
    """主入口"""
    print(f"Executing {name}...")
    print(f"Args: {{args}}")
    return {{"success": True}}

if __name__ == "__main__":
    main(sys.argv[1:])
'''
        
        with open(os.path.join(skill_path, f"{name}.py"), 'w') as f:
            f.write(main_py)
    
    def _create_advanced_skill(self, skill_path: str, name: str, description: str) -> None:
        """创建高级技能结构"""
        
        # 创建高级版本
        self._create_basic_skill(skill_path, name)
        
        # 创建配置
        config = {
            "name": name,
            "description": description,
            "version": "1.0.0",
            "dependencies": [],
            "permissions": [],
            "settings": {
                "auto_run": False,
                "timeout": 30
            }
        }
        
        with open(os.path.join(skill_path, "config.json"), 'w') as f:
            json.dump(config, f, indent=2)
        
        # 创建测试文件
        test_py = f'''#!/usr/bin/env python3
"""测试用例"""

import unittest
import {name}

class Test{name}(unittest.TestCase):
    def test_basic(self):
        result = {name}.main(["test"])
        self.assertTrue(result.get("success"))

if __name__ == "__main__":
    unittest.main()
'''
        
        with open(os.path.join(skill_path, f"test_{name}.py"), 'w') as f:
            f.write(test_py)
    
    def fork_skill(self, original_name: str, new_name: str, 
                   modifications: Dict = None) -> Dict[str, Any]:
        """基于现有技能创建分支"""
        
        original_path = os.path.join(self.skills_dir, original_name)
        
        if not os.path.exists(original_path):
            return {"error": f"Original skill {original_name} not found"}
        
        new_path = os.path.join(self.skills_dir, new_name)
        
        if os.path.exists(new_path):
            return {"error": f"Skill {new_name} already exists"}
        
        # 复制文件
        shutil.copytree(original_path, new_path)
        
        # 修改元数据
        meta_file = os.path.join(new_path, "_meta.json")
        if os.path.exists(meta_file):
            with open(meta_file, 'r') as f:
                meta = json.load(f)
            
            meta["name"] = new_name
            meta["forked_from"] = original_name
            meta["created"] = datetime.now().isoformat()
            meta["version"] = "1.0.0"
            
            with open(meta_file, 'w') as f:
                json.dump(meta, f, indent=2)
        
        return {
            "success": True,
            "name": new_name,
            "forked_from": original_name,
            "path": new_path,
            "message": f"Forked {original_name} to {new_name}"
        }
    
    def export_to_github(self, skill_name: str, repo_url: str = None) -> Dict[str, Any]:
        """导出技能到 GitHub"""
        
        skill_path = os.path.join(self.skills_dir, skill_name)
        
        if not os.path.exists(skill_path):
            return {"error": f"Skill {skill_name} not found"}
        
        # 生成导出说明
        export_info = {
            "skill_name": skill_name,
            "path": skill_path,
            "exported_at": datetime.now().isoformat(),
            "repo_url": repo_url or "https://github.com/<your-repo>/<skill-name>",
            "instructions": f"""
# 导出说明

## 上传步骤

1. 创建 GitHub 仓库
2. 复制技能文件:
   cp -r {skill_path} /path/to/repo

3. 添加 ClawHub 配置:
   {skill_name}/
   ├── SKILL.md
   ├── _meta.json
   └── ...

4. 推送到 GitHub:
   git add .
   git commit -m "Add {skill_name} skill"
   git push

5. 分享给他人安装:
   clawhub install <your-repo>/{skill_name}
"""
        }
        
        # 保存导出信息
        export_file = os.path.join(self.storage_dir, f"export_{skill_name}.json")
        with open(export_file, 'w') as f:
            json.dump(export_info, f, indent=2)
        
        return export_info
    
    def list_custom_skills(self) -> List[Dict[str, Any]]:
        """列出自定义技能"""
        
        custom_skills = []
        
        for item in os.listdir(self.skills_dir):
            item_path = os.path.join(self.skills_dir, item)
            
            # 查找元数据
            meta_file = os.path.join(item_path, "_meta.json")
            if os.path.exists(meta_file):
                try:
                    with open(meta_file, 'r') as f:
                        meta = json.load(f)
                    
                    if "Jarvis Evolver" in str(meta.get("author", "")) or \
                       "auto-generated" in meta.get("tags", []):
                        custom_skills.append({
                            "name": item,
                            "path": item_path,
                            "meta": meta
                        })
                except:
                    pass
        
        return custom_skills


if __name__ == "__main__":
    builder = SkillBuilder()
    
    # 创建测试技能
    result = builder.create_skill(
        name="test-skill",
        description="测试技能",
        template="basic"
    )
    print("创建结果:", result)
    
    # 列出自定义技能
    print("\n自定义技能:", builder.list_custom_skills())