---
name: jarvis-onchain-core
description: >
  Jarvis 核心链上系统 - 多链聚合 + 智能合约交互 + NFT/代币管理。
  基于 onchainkit, erc-8004, endaoment, ens-primary-name, veil, clanker, qrcoin, base 精华重构。
  功能：钱包管理、跨链转账、DeFi、NFT、隐私交易、ENS。
---

# Jarvis OnChain Core

 Jarvis 自主研发的核心链上技能，整合多个 OnChain/DeFi 技能的最佳实践。

## 核心功能

- **多链支持**: Ethereum, Base, Arbitrum, Optimism, Polygon, Solana, Unichain
- **钱包管理**: 多钱包支持、硬件钱包集成
- **代币操作**: 部署 ERC20、Token 转账、Swap
- **DeFi**: 流动性、收益率、质押
- **NFT**: 铸造、交易、管理
- **ENS**: 域名注册、反向解析、设置主域名
- **隐私交易**: Veil Cash _shielded pool
- **预测市场**: Polymarket 集成

## 架构

```
jarvis-onchain-core/
├── SKILL.md
├── _meta.json
├── config/
│   ├── chains.json        # 链配置
│   ├── wallets.json       # 钱包配置
│   └── protocols.json     # 协议配置
├── scripts/
│   ├── wallet.py          # 钱包管理
│   ├── token.py           # 代币操作
│   ├── defi.py            # DeFi 操作
│   ├── nft.py             # NFT 管理
│   ├── ens.py             # ENS 管理
│   └── privacy.py         # 隐私交易
└── storage/
    ├── positions.json     # 链上仓位
    └── history.json       # 交易历史
```

## 使用方式

### 钱包

```bash
# 余额查询
balance --chain base

# 添加钱包
wallet add 0x...

# 多签设置
wallet multisig --threshold 2 --owners 0x...,0x...
```

### 代币

```bash
# 部署代币
token deploy --name "MyToken" --symbol "MTK" --supply 1000000

# 转账
token transfer --to 0x... --amount 100 --chain base

# Swap
token swap --from ETH --to USDC --amount 1
```

### DeFi

```bash
# 添加流动性
defi add --pool ETH-USDC --amount 1,1000

# 质押
defi stake --token ETH --amount 10
```

### NFT

```bash
# 铸造 NFT
nft mint --contract 0x... --to 0x...

# 转移
nft transfer --id 1 --to 0x...
```

### ENS

```bash
# 设置主域名
ens set-primary myname.eth

# 解析地址
ens resolve myname.eth
```

### 隐私

```bash
# 隐私存款
veil deposit --amount 10

# 隐私提款
veil withdraw --to 0x... --amount 10
```

## 已整合技能

| 原技能 | 整合功能 |
|--------|---------|
| onchainkit | 链上开发工具 |
| erc-8004 | AI Agent 注册 |
| endaoment | 慈善捐赠 |
| ens-primary-name | ENS 主域名 |
| veil | 隐私交易 |
| clanker | 代币部署 |
| qrcoin | QR 码拍卖 |
| base | Base 链支持 |

## 支持链

| 链 | 状态 | 功能 |
|-----|------|------|
| Ethereum | ✅ | 完整 |
| Base | ✅ | 完整 |
| Arbitrum | ✅ | 完整 |
| Optimism | ✅ | 完整 |
| Polygon | ✅ | 完整 |
| Solana | 🔄 | 基础 |
| Unichain | 🔄 | 基础 |

## 版本历史

- **2026-03-06 v1.0.0**: 初始版本，整合 8 个 OnChain/DeFi 技能的核心功能

## 下一步更新计划

- [ ] 添加更多链 (Solana 完整支持)
- [ ] 集成更多 DeFi 协议
- [ ] 完善 NFT 交易市场
- [ ] 添加合约部署模板