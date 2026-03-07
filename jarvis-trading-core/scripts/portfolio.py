#!/usr/bin/env python3
"""
Jarvis Trading Core - Portfolio Management
投资组合管理：跨交易所资产汇总
"""

import os
import json
from datetime import datetime
from typing import Dict, List, Any

class Portfolio:
    """投资组合管理"""
    
    def __init__(self, skill_dir: str = None):
        self.skill_dir = skill_dir or os.path.expanduser(
            "~/.openclaw/workspace/skills/jarvis-trading-core"
        )
        self.storage_dir = os.path.join(self.skill_dir, "storage")
        self.config_dir = os.path.join(self.skill_dir, "config")
        
        os.makedirs(self.storage_dir, exist_ok=True)
        
        self.positions_file = os.path.join(self.storage_dir, "positions.json")
        self.pnl_file = os.path.join(self.storage_dir, "pnl.json")
        
        self.positions = self._load_json(self.positions_file, {})
        self.pnl = self._load_json(self.pnl_file, [])
    
    def _load_json(self, filepath: str, default: Any) -> Any:
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r') as f:
                    return json.load(f)
            except:
                pass
        return default
    
    def _save_json(self, filepath: str, data: Any) -> None:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def get_portfolio(self) -> Dict[str, Any]:
        """获取投资组合总览"""
        
        # 加载配置
        with open(os.path.join(self.config_dir, "exchanges.json")) as f:
            config = json.load(f)
        
        portfolio = {
            "timestamp": datetime.now().isoformat(),
            "total_value_usd": 0,
            "by_exchange": {},
            "positions": self.positions
        }
        
        for exchange, cfg in config.get("exchanges", {}).items():
            if cfg.get("enabled"):
                # 这里应该调用各个交易所 API 获取余额
                # 暂时返回模拟数据
                portfolio["by_exchange"][exchange] = {
                    "balance_usd": 0,
                    "positions": []
                }
        
        return portfolio
    
    def add_position(self, exchange: str, symbol: str, side: str, 
                     amount: float, price: float, leverage: int = 1) -> None:
        """添加仓位"""
        
        position_id = f"{exchange}:{symbol}:{side}"
        
        self.positions[position_id] = {
            "exchange": exchange,
            "symbol": symbol,
            "side": side,
            "amount": amount,
            "entry_price": price,
            "leverage": leverage,
            "value_usd": amount * price,
            "opened_at": datetime.now().isoformat()
        }
        
        self._save_json(self.positions_file, self.positions)
    
    def close_position(self, position_id: str, exit_price: float) -> Dict[str, Any]:
        """平仓并记录 PnL"""
        
        if position_id not in self.positions:
            return {"error": "Position not found"}
        
        pos = self.positions[position_id]
        
        # 计算盈亏
        if pos["side"] == "long":
            pnl_pct = (exit_price - pos["entry_price"]) / pos["entry_price"] * 100
        else:
            pnl_pct = (pos["entry_price"] - exit_price) / pos["entry_price"] * 100
        
        pnl_pct *= pos["leverage"]
        
        pnl_record = {
            "position_id": position_id,
            "symbol": pos["symbol"],
            "side": pos["side"],
            "entry_price": pos["entry_price"],
            "exit_price": exit_price,
            "pnl_pct": round(pnl_pct, 2),
            "pnl_usd": round(pos["value_usd"] * pnl_pct / 100, 2),
            "closed_at": datetime.now().isoformat()
        }
        
        self.pnl.append(pnl_record)
        self._save_json(self.pnl_file, self.pnl)
        
        del self.positions[position_id]
        self._save_json(self.positions_file, self.positions)
        
        return pnl_record
    
    def get_pnl(self, period: str = "24h") -> Dict[str, Any]:
        """获取 PnL 统计"""
        
        # 简化：返回所有记录
        total_pnl = sum(p.get("pnl_usd", 0) for p in self.pnl)
        win_count = len([p for p in self.pnl if p.get("pnl_usd", 0) > 0])
        loss_count = len([p for p in self.pnl if p.get("pnl_usd", 0) < 0])
        
        return {
            "total_pnl": total_pnl,
            "win_rate": win_count / len(self.pnl) if self.pnl else 0,
            "total_trades": len(self.pnl),
            "wins": win_count,
            "losses": loss_count
        }


if __name__ == "__main__":
    portfolio = Portfolio()
    
    # 测试
    print("📊 Jarvis Trading Core - Portfolio")
    print("=" * 40)
    
    # 获取组合
    p = portfolio.get_portfolio()
    print(f"时间: {p['timestamp']}")
    print(f"交易所: {list(p['by_exchange'].keys())}")
    
    # 添加测试仓位
    portfolio.add_position("binance", "BTC/USDT", "long", 0.01, 50000, 5)
    
    # 获取 PnL
    stats = portfolio.get_pnl()
    print(f"\nPnL 统计: {stats}")