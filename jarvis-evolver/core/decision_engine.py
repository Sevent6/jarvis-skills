"""
Jarvis Evolver - 决策引擎
基于历史决策构建判断框架，辅助未来决策
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Any, Optional
from pathlib import Path

class DecisionEngine:
    """决策引擎 - 辅助判断"""
    
    def __init__(self, storage_dir: str = None):
        self.storage_dir = storage_dir or os.path.expanduser(
            "~/.openclaw/workspace/skills/jarvis-evolver/storage"
        )
        os.makedirs(self.storage_dir, exist_ok=True)
        
        self.decisions_file = os.path.join(self.storage_dir, "decisions.json")
        self.rules_file = os.path.join(self.storage_dir, "rules.json")
        
        self.decisions = self._load_json(self.decisions_file, [])
        self.rules = self._load_json(self.rules_file, {})
    
    def _load_json(self, filepath: str, default: Any) -> Any:
        """加载 JSON 文件"""
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r') as f:
                    return json.load(f)
            except:
                pass
        return default
    
    def _save_json(self, filepath: str, data: Any) -> None:
        """保存 JSON 文件"""
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    # ========== 交易决策规则 ==========
    
    TRADING_RULES = {
        "macd_cross": {
            "condition": "macd_histogram > 0 AND previous_histogram < 0",
            "action": "BUY",
            "confidence": 0.7
        },
        "macd_death_cross": {
            "condition": "macd_histogram < 0 AND previous_histogram > 0",
            "action": "SELL",
            "confidence": 0.7
        },
        "high_volatility": {
            "condition": "volatility > 0.3",
            "action": "REDUCE_POSITION",
            "confidence": 0.8
        },
        "low_volatility": {
            "condition": "volatility < 0.1",
            "action": "INCREASE_POSITION",
            "confidence": 0.6
        },
        "overbought": {
            "condition": "rsi > 70",
            "action": "TAKE_PROFIT",
            "confidence": 0.75
        },
        "oversold": {
            "condition": "rsi < 30",
            "action": "BUY_DIP",
            "confidence": 0.75
        }
    }
    
    # ========== 技能选择规则 ==========
    
    SKILL_SELECTION_RULES = {
        "simple_query": {
            "keywords": ["what", "how", "explain", "define"],
            "preferred_skill": "mini-max-m2.5",
            "confidence": 0.9
        },
        "complex_reasoning": {
            "keywords": ["analyze", "compare", "evaluate", "strategy"],
            "preferred_skill": "jarvistrx",
            "confidence": 0.85
        },
        "web_search": {
            "keywords": ["search", "find", "look up", "查"],
            "preferred_skill": "tavily",
            "confidence": 0.8
        },
        "code_task": {
            "keywords": ["code", "program", "implement", "debug"],
            "preferred_skill": "coding-agent",
            "confidence": 0.85
        },
        "trading": {
            "keywords": ["trade", "buy", "sell", "position", "交易"],
            "preferred_skill": "okx-bot",
            "confidence": 0.9
        }
    }
    
    # ========== 系统维护规则 ==========
    
    MAINTENANCE_RULES = {
        "memory_cleanup": {
            "condition": "memory_size > 150KB",
            "action": "cleanup_memory",
            "priority": 1
        },
        "docker_health": {
            "condition": "container_status != 'Up'",
            "action": "restart_container",
            "priority": 2
        },
        "tunnel_health": {
            "condition": "health_check != 200",
            "action": "restart_tunnel",
            "priority": 2
        }
    }
    
    def decide(self, context: str, options: List[str] = None) -> Dict[str, Any]:
        """根据上下文做出决策建议"""
        
        context_lower = context.lower()
        
        # 1. 交易决策
        for rule_name, rule in self.TRADING_RULES.items():
            if any(kw in context_lower for kw in [rule_name.replace("_", " ")]):
                return {
                    "decision": rule["action"],
                    "confidence": rule["confidence"],
                    "rule": rule_name,
                    "reasoning": f"基于交易规则: {rule_name}"
                }
        
        # 2. 技能选择
        for rule_name, rule in self.SKILL_SELECTION_RULES.items():
            if any(kw in context_lower for kw in rule["keywords"]):
                return {
                    "decision": rule["preferred_skill"],
                    "confidence": rule["confidence"],
                    "rule": rule_name,
                    "reasoning": f"基于技能选择规则: {rule_name}"
                }
        
        # 3. 系统维护
        for rule_name, rule in self.MAINTENANCE_RULES.items():
            if rule_name in context_lower:
                return {
                    "decision": rule["action"],
                    "priority": rule["priority"],
                    "rule": rule_name,
                    "reasoning": f"基于维护规则: {rule_name}"
                }
        
        # 默认决策
        return {
            "decision": "default",
            "confidence": 0.5,
            "reasoning": "无匹配规则，使用默认决策"
        }
    
    def record_decision(self, context: str, decision: str, result: str, 
                        metadata: Dict = None) -> None:
        """记录决策结果，用于学习"""
        record = {
            "timestamp": datetime.now().isoformat(),
            "context": context,
            "decision": decision,
            "result": result,
            "metadata": metadata or {}
        }
        
        self.decisions.append(record)
        
        # 只保留最近 1000 条
        if len(self.decisions) > 1000:
            self.decisions = self.decisions[-1000:]
        
        self._save_json(self.decisions_file, self.decisions)
    
    def get_success_rate(self, decision_type: str = None) -> Dict[str, float]:
        """计算决策成功率"""
        if not self.decisions:
            return {"total": 0, "success": 0, "rate": 0}
        
        filtered = self.decisions
        if decision_type:
            filtered = [d for d in filtered if decision_type in d.get("decision", "")]
        
        total = len(filtered)
        if total == 0:
            return {"total": 0, "success": 0, "rate": 0}
        
        success = len([d for d in filtered if d.get("result") == "success"])
        
        return {
            "total": total,
            "success": success,
            "rate": success / total if total > 0 else 0
        }
    
    def suggest_improvement(self) -> List[str]:
        """基于历史决策建议改进"""
        suggestions = []
        
        # 检查成功率低的决策类型
        for rule_name in list(self.TRADING_RULES.keys()):
            rate = self.get_success_rate(rule_name)
            if rate["total"] > 5 and rate["rate"] < 0.5:
                suggestions.append(
                    f"交易规则 '{rule_name}' 成功率仅 {rate['rate']:.1%}，建议调整参数"
                )
        
        return suggestions
    
    def add_rule(self, rule_type: str, rule_name: str, rule_config: Dict) -> None:
        """添加新规则"""
        if rule_type == "trading":
            self.TRADING_RULES[rule_name] = rule_config
        elif rule_type == "skill":
            self.SKILL_SELECTION_RULES[rule_name] = rule_config
        elif rule_type == "maintenance":
            self.MAINTENANCE_RULES[rule_name] = rule_config
        
        # 保存到文件
        self.rules[rule_type] = getattr(self, f"{rule_type.upper()}_RULES")
        self._save_json(self.rules_file, self.rules)


if __name__ == "__main__":
    engine = DecisionEngine()
    
    # 测试决策
    result = engine.decide("RSI is 75, overbought condition")
    print("决策结果:", result)
    
    # 记录决策
    engine.record_decision(
        context="BTC price dropped, oversold signal",
        decision="BUY_DIP",
        result="success"
    )
    
    # 查看成功率
    print("成功率:", engine.get_success_rate())