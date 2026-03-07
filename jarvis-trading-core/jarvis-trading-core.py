#!/usr/bin/env python3
"""
Jarvis Trading Core - Main Entry
主入口脚本
"""

import sys
import os

# 添加脚本目录到路径
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)

from scripts.portfolio import Portfolio
from scripts.signals import SignalDetector
from scripts.whale import WhaleMonitor

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Jarvis Trading Core")
    parser.add_argument("command", choices=["portfolio", "signal", "whale", "help"])
    parser.add_argument("--symbol", help="Trading symbol")
    parser.add_argument("--prices", help="Comma-separated prices")
    parser.add_argument("--action", help="Action to perform")
    
    args = parser.parse_args()
    
    if args.command == "portfolio":
        p = Portfolio()
        print(p.get_portfolio())
    
    elif args.command == "signal":
        if args.prices:
            prices = [float(p) for p in args.prices.split(",")]
            detector = SignalDetector()
            result = detector.analyze(args.symbol or "UNKNOWN", prices)
            print(result)
        else:
            detector = SignalDetector()
            print(detector.get_signal_history())
    
    elif args.command == "whale":
        w = WhaleMonitor()
        print(w.get_whale_summary())
    
    else:
        print("""
Jarvis Trading Core Commands:
  portfolio              - Show portfolio
  signal --symbol BTC --prices 50000,51000,...  - Analyze signals
  whale                  - Show whale activity
""")

if __name__ == "__main__":
    main()