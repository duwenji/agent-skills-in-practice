# Agent Skills in Practice — スキルを作り、見つけ、活用する

Agent Skills オープンスタンダード（`agentskills.io`）に基づき、**Claude Code の `/skill-creator`** と **GitHub Copilot の Agent Skills** の両方で使えるスキル開発を学ぶチュートリアルです。

> 💡 ブラウザで https://duwenji.github.io/spa-quiz-app/ を開くと、関連トピックをクイズ形式で復習できます。

---

## 🎯 このチュートリアルの特徴

| 観点 | 内容 |
|------|------|
| **フォーカス** | Agent Skills オープンスタンダードの実践 |
| **スキル生成** | Claude Code `/skill-creator`（対話生成）+ 手書き |
| **実行環境** | Claude Code（`.claude/skills/`）& GitHub Copilot（`.github/skills/`） |
| **サンプルスキル** | **フロントエンド特化**（grill-me, frontend-design 等）+ **コンテンツ生成**（baoyu-skills） |
| **問題認識** | **AIコード生成3課題** からスタート |
| **概念フレームワーク** | **Superpowers（OSSプラグイン）/ GStack / baoyu-skills** を解説 |

---

## 📚 5層構造

```
発見層  ── Find Skills / gh skill / skill.sh / baoyu-skills 発見
作成層  ── Claude Code /skill-creator + 手書き SKILL.md
概念層  ── Superpowers（OSSプラグイン）/ GStack / baoyu-skills アーキテクチャ
実践層  ── grill-me / triage / improve / frontend-design / ui-ux-pro-max / baoyu-*
応用層  ── コンテンツ生成パイプライン / 画像生成バックエンド / カスタムスキル開発
```

---

## 📖 学習の流れ

### Part 1: 概要と環境準備（20分）⭐
| # | セクション | 内容 |
|---|-----------|------|
| 1-1 | Agent Skills エコシステムの全体像 | 本教材の目的、4層構造の解説 |
| 1-2 | 環境セットアップ | Claude Code / GitHub Copilot 両方の準備 |

### Part 2: スキル作成入門（60分）
| # | セクション | 内容 |
|---|-----------|------|
| 2-1 | Agent Skills とは | オープンスタンダード、Claude Code と GitHub Copilot の比較 |
| 2-2 | skill-creator で最初のスキルを作る | ハンズオン：対話形式でスキル生成、テスト・評価・改善サイクル |
| 2-3 | SKILL.md の手書きとカスタマイズ | 生成後編集・最適化、両プラットフォーム対応 |
| 2-4 | スキル作成のベストプラクティス | 効果的なプロンプト設計、反復改善サイクル |

### Part 3: スキル発見と共有（60分）
| # | セクション | 内容 |
|---|-----------|------|
| 3-1 | Find Skills / gh skill でスキルを探す | GitHub.com 上のスキル発見機能、CLI検索 |
| 3-2 | skill.sh によるクロスプラットフォーム検索 | コマンドラインからスキルを検索・実行 |
| 3-3 | スキルの共有とチーム展開 | Personal Skills / Project Skills / submodule 戦略 |
| 3-4 | baoyu-skills で学ぶ実践的スキル発見 | 21,000+ Stars の人気リポジトリを題材にスキル発見を実践 |

### Part 4: 概念フレームワークと課題認識（80分）
| # | セクション | 内容 |
|---|-----------|------|
| 4-1 | Superpowers: コーディングエージェントの開発方法論 | Superpowers（obra/superpowers）の解説、スキルによる開発プロセス自動化 |
| 4-2 | GStack: Generative AI Stack 全体像 | 生成AIスタックにおけるスキルの位置づけ |
| 4-3 | AIコード生成の3つの課題 | AIコード生成の問題分析（理解のずれ / 実行失敗 / 構造の問題） |
| 4-4 | 問題 × スキル解決マッピング | 各問題をどのスキルで解決するか（一覧表） |
| 4-5 | baoyu-skills のアーキテクチャ分析 | 3大フレームワーク比較、自己完結型設計、5Dスタイル体系 |

### Part 5: 実践スキル実装編（180分）⭐ メイン
| # | スキル | 種類 | 学習ポイント |
|---|-------|------|------------|
| 5-1 | **grill-me**（コードレビュー） | 品質検証 | コード分析、レビュー観点の自動化、SKILL.md実装 |
| 5-2 | **triage**（Issue分析） | 優先順位付け | Issue解析、ラベル分類、優先度判定ロジック |
| 5-3 | **improve**（コード改善） | リファクタリング | 改善提案、パフォーマンス最適化、リファクタリング支援 |
| 5-4 | **frontend-design**（設計支援） | アーキテクチャ | コンポーネント設計、状態管理設計、レンダリング最適化 |
| 5-5 | **ui-ux-pro-max**（UI/UX最適化） | デザイン改善 | アクセシビリティ、レスポンシブデザイン、ユーザビリティ監査 |
| 5-6 | **baoyu-diagram**（SVG図形生成） | コンテンツ生成 | SVG直書き、5図タイプ、ダークモード対応 |
| 5-7 | **baoyu-infographic**（インフォグラフィック） | コンテンツ生成 | 21レイアウト×17スタイル、自動推薦ロジック |
| 5-8 | **baoyu-comic**（知識マンガ生成） | コンテンツ生成 | 5アート×7トーン、ストーリーボード、順次生成 |

### Part 6: コンテンツ生成スキル実践（90分）🆕
| # | セクション | 内容 |
|---|-----------|------|
| 6-1 | baoyu-skills エコシステム入門 | 全体像、インストール、3カテゴリ（Content / AI Gen / Utility） |
| 6-2 | コンテンツ生成スキルを使いこなす | カバー画像→図解→インフォグラフィック→スライドの連携 |
| 6-3 | AI画像生成バックエンドの選択 | baoyu-image-gen / Gemini Web / Codex CLI の比較と選択 |
| 6-4 | 実プロジェクトでのスキル連携 | パイプライン構築、CI/CD統合、バッチ処理、並列実行 |
| 6-5 | カスタムスキル開発（baoyu流） | 自己完結型スキル、スタイル体系、バックエンド抽象化 |

### Part 7: 発展・応用（65分）
| # | セクション | 内容 |
|---|-----------|------|
| 7-1 | 複数スキルの連携パイプライン | grill-me → improve → frontend-design の連携 |
| 7-2 | 実プロジェクトへの組み込み | CI/CD パイプラインへの統合、品質ゲート |
| 7-3 | スキル評価と改善サイクル | 品質評価フレームワーク導入 |
| 7-4 | skill-creator 徹底解説 | 対話生成の仕組み、内部プロセス、クロスプラットフォーム活用ノウハウ |

---

## ⏱ 学習時間目安

| Part | セクション数 | 学習時間 | 難易度 |
|------|------------|---------|-------|
| Part 1 | 2 | 20分 | ⭐ |
| Part 2 | 4 | 60分 | ⭐⭐ |
| Part 3 | 4 | 60分 | ⭐⭐ |
| Part 4 | 5 | 80分 | ⭐⭐ |
| Part 5 | 8 | 180分 | ⭐⭐⭐ |
| Part 6 | 5 | 90分 | ⭐⭐⭐ |
| Part 7 | 4 | 65分 | ⭐⭐⭐ |
| **合計** | **32** | **8時間35分** | |


---

## 🚀 クイックスタート（5分）

### 1. Claude Code でスキルを生成する
```bash
# Claude Code を起動し、以下を実行
claude

# セッション内で /skill-creator を実行
/skill-creator
```

### 2. GitHub Copilot でスキルを使う
`.github/skills/` ディレクトリに SKILL.md を配置します：
```bash
mkdir -p .github/skills/grill-me/
# SKILL.md を配置
```

### 3. 実践スキルを試す
`docs/05-skills-in-practice/` から使いたいスキルを選び、SKILL.md をコピーして配置します。

---

## 📁 ファイル構成

```
agent-skills-in-practice/
├── README.md
├── CHANGELOG.md
├── MASTER-INDEX.md
├── QUICK-REFERENCE.md
├── ROADMAP.md
├── CONTRIBUTING.md
├── LICENSE
├── docs/
│   ├── 00-COVER.md
│   ├── 01-fundamentals/          # Part 1
│   ├── 02-skill-creation/        # Part 2
│   ├── 03-discovery/             # Part 3
│   ├── 04-frameworks/            # Part 4
│   ├── 05-skills-in-practice/    # Part 5 ⭐
│   ├── 06-content-creation/     # Part 6 🆕 baoyu-skills
│   └── 07-advanced/             # Part 7
├── samples/                      # 実装サンプル（SKILL.md）
├── assets/                       # 図表類
│   └── diagrams/
└── ebook-output/                 # 電子書籍出力
```

---

## 🎓 学習後、あなたができること

✓ Claude Code の `/skill-creator` で対話的にスキルを作成できる  
✓ GitHub Copilot の `.github/skills/` にスキルを配置できる  
✓ フロントエンド開発に特化した実践スキルを使いこなせる  
✓ スキルをチームで共有・管理できる  
✓ 複数スキルを連携させたパイプラインを構築できる  
✓ Superpowers（obra/superpowers）の設計思想を理解し、スキル開発に応用できる

---

## 🔗 関連リソース

### 公式ドキュメント

| プロダクト | 提供元 | スキル配置場所 | スキル生成方法 |
|-----------|--------|--------------|--------------|
| **Claude Code** | Anthropic | `.claude/skills/<name>/SKILL.md` | `/skill-creator`（対話生成）/ 手書き |
| **GitHub Copilot** | GitHub (Microsoft) | `.github/skills/<name>/SKILL.md` | 手書き / `gh skill` でインストール |

### 共通基盤

- [Agent Skills オープンスタンダード](https://agentskills.io)
- [agentskills/agentskills (GitHub)](https://github.com/agentskills/agentskills)
- [anthropics/skills - skill-creator (GitHub)](https://github.com/anthropics/skills/tree/main/skills/skill-creator)

### 公式ドキュメント

- [Claude Code Skills ドキュメント](https://code.claude.com/docs/en/skills)
- [GitHub Copilot Agent Skills ドキュメント](https://docs.github.com/en/copilot/using-github-copilot/creating-and-editing-skills)

---

## 🤝 貢献・フィードバック

改善提案、誤字修正、新しいスキル提案は Issue/PR でお気軽にお寄せください。

## 📄 ライセンス

MIT License - 自由に使用、改変、配布できます。

---

**最終更新**: 2026年6月13日  
**バージョン**: 0.2.0 🚧 全面改訂中

👉 [Part 1: エコシステム概要を読む →](docs/01-fundamentals/01-ecosystem-overview.md)
