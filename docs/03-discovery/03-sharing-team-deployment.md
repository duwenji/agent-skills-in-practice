# 3-3: スキルの共有とチーム展開

> **学習時間**: 15分 | **難易度**: ⭐⭐

## 概要

作成したスキルをチームで共有・展開する方法を学びます。Personal Skills、shared-copilot-skills、Git submodule の3つの戦略を状況に応じて使い分けることで、効率的なスキル管理が可能になります。

## 3つの共有戦略

| 戦略 | 適用範囲 | 難易度 | 推奨シーン |
|------|---------|--------|-----------|
| Personal Skills | 個人 | ⭐ | 個人利用、実験 |
| shared-copilot-skills | チーム | ⭐⭐ | チーム内共有 |
| Git submodule | 組織全体 | ⭐⭐⭐ | 組織全体での標準化 |

## 戦略1: Personal Skills

個人の開発環境でスキルを管理する最もシンプルな方法です。

### 設定方法

```bash
# Windows
mkdir -p %USERPROFILE%\.copilot\skills\
copy SKILL.md %USERPROFILE%\.copilot\skills\my-skill\

# macOS / Linux
mkdir -p ~/.copilot/skills/
cp SKILL.md ~/.copilot/skills/my-skill/
```

### メリット・デメリット

- ✅ 設定が最も簡単
- ✅ 個人の実験に最適
- ❌ チーム共有不可
- ❌ バックアップが必要

## 戦略2: shared-copilot-skills

チームで共有するスキルリポジトリを作成し、全メンバーが参照できるようにします。

### リポジトリ構成例

```
shared-copilot-skills/
├── README.md
├── skills/
│   ├── grill-me/
│   │   └── SKILL.md
│   ├── triage/
│   │   └── SKILL.md
│   └── improve/
│       └── SKILL.md
└── CONTRIBUTING.md
```

### セットアップ手順

1. 共有リポジトリを作成
2. スキルを `skills/` ディレクトリに配置
3. チームメンバーにリポジトリのアクセス権を付与
4. 各メンバーが Personal Skills として参照設定

### 運用ルール例

```markdown
## スキル追加フロー
1. Issue でスキル提案
2. チームレビュー
3. PR 作成
4. 承認後マージ
5. チームメンバーに通知

## バージョン管理
- スキルは Semantic Versioning に従う
- CHANGELOG に変更履歴を記載
- 破壊的変更はメジャーバージョンアップ
```

## 戦略3: Git submodule

組織全体でスキルを標準化する場合に有効です。

### セットアップ

```bash
# スキルリポジトリを submodule として追加
git submodule add https://github.com/org/shared-copilot-skills.git .github/skills/

# 特定のバージョンで固定
cd .github/skills/
git checkout v1.2.0
cd ../..

# 変更をコミット
git add .gitmodules .github/skills/
git commit -m "Add shared skills submodule (v1.2.0)"
```

### 更新手順

```bash
# 最新版に更新
git submodule update --remote .github/skills/

# 特定のバージョンに更新
cd .github/skills/
git fetch --tags
git checkout v2.0.0
cd ../..
git add .github/skills/
git commit -m "Update shared skills to v2.0.0"
```

## 戦略の選び方

```
個人で使いたい？
├── Yes → Personal Skills
└── No → チームで使いたい？
         ├── 小規模チーム（〜10人）→ shared-copilot-skills
         └── 大規模組織 → Git submodule
```

## 次のステップ

→ [Part 4: 概念フレームワーク](../04-frameworks/01-superpowers.md)
