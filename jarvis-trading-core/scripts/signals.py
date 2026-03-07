#!/usr/bin/env python3
"""
Jarvis Trading Core - Signal Detection
信号检测：RSI, MACD, 布林带
"""

import os
import json
from datetime import datetime
from typing import Dict, List, Any, Optional

class SignalDetector:
    """技术信号检测器"""
    
    def __init__(self, skill_dir: str = None):
        self.skill_dir = skill_dir or os.path.expanduser(
            "~/.openclaw/workspace/skills/jarvis-trading-core"
        )
        self.config_dir = os.path.join(self.skill_dir, "config")
        self.storage_dir = os.path.join(self.skill_dir, "storage")
        
        # 加载信号配置
        with open(os.path.join(self.config_dir, "signals.json")) as f:
            self.config = json.load(f)
        
        self.signals_file = os.path.join(self.storage_dir, "signals.json")
        self.signals = self._load_signals()
    
    def _load_signals(self) -> List[Dict]:
        if os.path.exists(self.signals_file):
            try:
                with open(self.signals_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        return []
    
    def _save_signals(self) -> None:
        with open(self.signals_file, 'w') as f:
            json.dump(self.signals, f, indent=2, ensure_ascii=False)
    
    def calculate_rsi(self, prices: List[float], period: int = 14) -> float:
        """计算 RSI"""
        if len(prices) < period + 1:
            return 50.0
        
        gains = []
        losses = []
        
        for i in range(1, len(prices)):
            change = prices[i] - prices[i-1]
            if change > 0:
                gains.append(change)
                losses.append(0)
            else:
                gains.append(0)
                losses.append(abs(change))
        
        avg_gain = sum(gains[-period:]) / period
        avg_loss = sum(losses[-period:]) / period
        
        if avg_loss == 0:
            return 100
        
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        
        return round(rsi, 2)
    
    def calculate_macd(self, prices: List[float]) -> Dict[str, float]:
        """计算 MACD"""
        if len(prices) < 26:
            return {"macd": 0, "signal": 0, "histogram": 0}
        
        # 简化 EMA 计算
        def ema(data, period):
            multiplier = 2 / (period + 1)
            ema_val = data[0]
            for price in data[1:]:
                ema_val = (price - ema_val) * multiplier + ema_val
            return ema_val
        
        ema_12 = ema(prices, 12)
        ema_26 = ema(prices, 26)
        
        macd_line = ema_12 - ema_26
        signal_line = macd_line  # 简化
        histogram = macd_line - signal_line
        
        return {
            "macd": round(macd_line, 2),
            "signal": round(signal_line, 2),
            "histogram": round(histogram, 2)
        }
    
    def calculate_bollinger(self, prices: List[float], period: int = 20, std_mult: int = 2) -> Dict[str, float]:
        """计算布林带"""
        if len(prices) < period:
            return {"upper": 0, "middle": 0, "lower": 0}
        
        recent = prices[-period:]
        sma = sum(recent) / period
        
        variance = sum((p - sma) ** 2 for p in recent) / period
        std = variance ** 0.5
        
        return {
            "upper": round(sma + std_mult * std, 2),
            "middle": round(sma, 2),
            "lower": round(sma - std_mult * std, 2)
        }
    
    def analyze(self, symbol: str, prices: List[float]) -> Dict[str, Any]:
        """分析价格并生成信号"""
        
        if len(prices) < 30:
            return {"error": "Insufficient data"}
        
        # 计算指标
        rsi = self.calculate_rsi(prices)
        macd = self.calculate_macd(prices)
        bb = self.calculate_bollinger(prices)
        
        current_price = prices[-1]
        
        # 生成信号
        signals = []
        
        # RSI 信号
        if rsi < 30:
            signals.append({
                "indicator": "RSI",
                "signal": "BUY",
                "reason": f"RSI oversold ({rsi})",
                "confidence": 0.75
            })
        elif rsi > 70:
            signals.append({
                "indicator": "RSI", 
                "signal": "SELL",
                "reason": f"RSI overbought ({rsi})",
                "confidence": 0.75
            })
        
        # MACD 信号
        if macd["histogram"] > 0 and macd["histogram"] < 0:
            signals.append({
                "indicator": "MACD",
                "signal": "BUY",
                "reason": "Golden cross",
                "confidence": 0.70
            })
        elif macd["histogram"] < 0 and macd["histogram"] > 0:
            signals.append({
                "indicator": "MACD",
                "signal": "SELL",
                "reason": "Death cross",
                "confidence": 0.70
            })
        
        # 布林带信号
        if current_price < bb["lower"]:
            signals.append({
                "indicator": "Bollinger",
                "signal": "BUY",
                "reason": "Price below lower band",
                "confidence": 0.65
            })
        elif current_price > bb["upper"]:
            signals.append({
                "indicator": "Bollinger",
                "signal": "SELL", 
                "reason": "Price above upper band",
                "confidence": 0.65
            })
        
        # 保存信号
        signal_record = {
            "symbol": symbol,
            "timestamp": datetime.now().isoformat(),
            "price": current_price,
            "indicators": {"rsi": rsi, "macd": macd, "bollinger": bb},
            "signals": signals
        }
        
        self.signals.append(signal_record)
        self._save_signals()
        
        return signal_record
    
    def get_signal_history(self, limit: int = 10) -> List[Dict]:
        """获取信号历史"""
        return self.signals[-limit:]


if __name__ == "__main__":
    detector = SignalDetector()
    
    # 模拟价格数据
    import random
    prices = [50000 + random.randint(-1000, 1000) for _ in range(50)]
    
    result = detector.analyze("BTC", prices)
    print("📊 Signal Analysis:")
    print(json.dumps(result, indent=2))