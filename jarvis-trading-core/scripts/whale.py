#!/usr/bin/env python3
"""
Jarvis Trading Core - Whale Monitoring
鲸鱼追踪：大户钱包监控
"""

import os
import json
from datetime import datetime
from typing import Dict, List, Any, Optional

class WhaleMonitor:
    """鲸鱼监控"""
    
    def __init__(self, skill_dir: str = None):
        self.skill_dir = skill_dir or os.path.expanduser(
            "~/.openclaw/workspace/skills/jarvis-trading-core"
        )
        self.config_dir = os.path.join(self.skill_dir, "config")
        self.storage_dir = os.path.join(self.skill_dir, "storage")
        
        # 加载配置
        with open(os.path.join(self.config_dir, "whale_watch.json")) as f:
            self.config = json.load(f)
        
        os.makedirs(self.storage_dir, exist_ok=True)
        
        self.history_file = os.path.join(self.storage_dir, "whale_history.json")
        self.history = self._load_history()
    
    def _load_history(self) -> List[Dict]:
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        return []
    
    def _save_history(self) -> None:
        with open(self.history_file, 'w') as f:
            json.dump(self.history, f, indent=2, ensure_ascii=False)
    
    def get_whales(self) -> List[Dict]:
        """获取监控的鲸鱼列表"""
        return self.config.get("whales", [])
    
    def add_whale(self, address: str, name: str = None, whale_type: str = "unknown") -> None:
        """添加监控鲸鱼"""
        
        whale = {
            "address": address,
            "name": name or address[:6] + "...",
            "type": whale_type,
            "alerts": ["large_buy", "large_sell"]
        }
        
        self.config["whales"].append(whale)
        
        # 保存配置
        with open(os.path.join(self.config_dir, "whale_watch.json"), 'w') as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)
    
    def record_activity(self, address: str, amount: float, token: str, 
                       tx_type: str, tx_hash: str = None) -> None:
        """记录鲸鱼活动"""
        
        # 查找鲸鱼信息
        whale_info = None
        for w in self.config.get("whales", []):
            if address.lower() in w.get("address", "").lower():
                whale_info = w
                break
        
        activity = {
            "timestamp": datetime.now().isoformat(),
            "address": address,
            "whale_name": whale_info.get("name") if whale_info else "Unknown",
            "whale_type": whale_info.get("type") if whale_info else "unknown",
            "amount": amount,
            "token": token,
            "tx_type": tx_type,  # "transfer_in" or "transfer_out"
            "tx_hash": tx_hash,
            "value_usd": self._estimate_value(amount, token)
        }
        
        self.history.append(activity)
        self._save_history()
        
        # 检查是否触发警报
        self._check_alerts(activity)
        
        return activity
    
    def _estimate_value(self, amount: float, token: str) -> float:
        """粗略估算 USD 值"""
        # 简化：应该调用价格 API
        prices = {"ETH": 2500, "BTC": 65000, "USDC": 1, "USDT": 1}
        return amount * prices.get(token.upper(), 0)
    
    def _check_alerts(self, activity: Dict) -> Optional[Dict]:
        """检查是否触发警报"""
        
        thresholds = self.config.get("alert_thresholds", {})
        
        alert = None
        
        if activity["token"].upper() == "ETH" and activity["amount"] > thresholds.get("eth_transfer", 100):
            alert = {
                "type": "large_transfer",
                "severity": "high",
                "message": f"🐋 {activity['whale_name']} transferred {activity['amount']} ETH"
            }
        elif activity["token"].upper() == "BTC" and activity["amount"] > thresholds.get("btc_transfer", 10):
            alert = {
                "type": "large_transfer",
                "severity": "high",
                "message": f"🐋 {activity['whale_name']} transferred {activity['amount']} BTC"
            }
        
        return alert
    
    def get_recent_activity(self, limit: int = 10) -> List[Dict]:
        """获取最近活动"""
        return self.history[-limit:]
    
    def get_whale_summary(self) -> Dict[str, Any]:
        """获取鲸鱼活动摘要"""
        
        if not self.history:
            return {"total_activities": 0, "whales": {}}
        
        # 按鲸鱼分组
        whale_stats = {}
        
        for activity in self.history:
            name = activity.get("whale_name", "Unknown")
            if name not in whale_stats:
                whale_stats[name] = {
                    "activities": 0,
                    "total_value": 0,
                    "tokens": set()
                }
            
            whale_stats[name]["activities"] += 1
            whale_stats[name]["total_value"] += activity.get("value_usd", 0)
            whale_stats[name]["tokens"].add(activity["token"])
        
        # 转换 set 为 list
        for name in whale_stats:
            whale_stats[name]["tokens"] = list(whale_stats[name]["tokens"])
        
        return {
            "total_activities": len(self.history),
            "whales": whale_stats,
            "recent": self.get_recent_activity(5)
        }


if __name__ == "__main__":
    monitor = WhaleMonitor()
    
    # 测试
    print("🐋 Jarvis Trading Core - Whale Monitor")
    print("=" * 40)
    
    # 获取鲸鱼列表
    whales = monitor.get_whales()
    print(f"监控中: {len(whales)} 只鲸鱼")
    for w in whales:
        print(f"  - {w['name']}: {w['address'][:10]}...")
    
    # 记录模拟活动
    monitor.record_activity(
        address="0x8acc...d4a2",
        amount=150,
        token="ETH",
        tx_type="transfer_in"
    )
    
    # 获取摘要
    summary = monitor.get_whale_summary()
    print(f"\n总活动: {summary['total_activities']}")