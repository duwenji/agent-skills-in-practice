# 5-1: baoyu-skills エコシステム入門

> **学習時間**: 15分 | **難易度**: ⭐⭐

## 概要

この Part 6 では、**JimLiu/baoyu-skills** を題材に、コンテンツ生成に特化したスキルセットの実践的な活用方法を学びます。これまでの Part 1〜5 で学んだスキル開発の知識を、実際のプロダクション品質のスキルセットを通じて応用します。

baoyu-skills は21,000+ Stars を集める人気リポジトリで、**コンテンツ生成**という特定ドメインに特化した20+のスキルを提供しています。

## baoyu-skills の全体像

### 3つのカテゴリ

baoyu-skills は以下の3カテゴリで構成されています：

```
baoyu-skills（21スキル）
├── Content Skills（7スキル）
│   ├── baoyu-cover-image     — 記事カバー画像生成
│   ├── baoyu-infographic     — インフォグラフィック生成
│   ├── baoyu-diagram         — SVG図形生成
│   ├── baoyu-slide-deck      — スライドデッキ生成
│   ├── baoyu-comic           — 知識マンガ生成
│   ├── baoyu-xhs-images      — SNS投稿画像生成
│   └── baoyu-article-illustrator — 記事挿絵生成
│
├── AI Generation Skills（3スキル）
│   ├── baoyu-image-gen       — 統合画像生成バックエンド
│   ├── baoyu-danger-gemini-web — Gemini Web 経由の画像生成
│   └── baoyu-danger-x-to-markdown — X(Twitter)投稿のMarkdown変換
│
└── Utility Skills（11スキル）
    ├── baoyu-translate       — 翻訳
    ├── baoyu-markdown-to-html — Markdown→HTML変換
    ├── baoyu-format-markdown — Markdown整形
    ├── baoyu-compress-image  — 画像圧縮
    ├── baoyu-url-to-markdown — URL→Markdown変換
    ├── baoyu-youtube-transcript — YouTube文字起こし
    ├── baoyu-wechat-summary  — WeChat記事要約
    ├── baoyu-post-to-x       — X(Twitter)投稿
    ├── baoyu-post-to-wechat  — WeChat投稿
    ├── baoyu-post-to-weibo   — Weibo投稿
    └── baoyu-electron-extract — Electronアプリ抽出
```

### インストール方法

```bash
# 推奨: npx skills add
npx skills add jimliu/baoyu-skills

# Claude Code プラグインとして
# Claude Code セッション内で:
/plugin marketplace add JimLiu/baoyu-skills
/plugin install baoyu-skills@baoyu-skills
```

> **💡 注意**: 21のスキル全てをインストールする必要はありません。必要なスキルだけを選んでインストールしましょう。

## コンテンツ生成のワークフロー

baoyu-skills を使った典型的なコンテンツ生成ワークフローは以下の通りです：

```
記事を書く
    ↓
baoyu-cover-image でカバー画像を生成
    ↓
baoyu-diagram で図解を生成
    ↓
baoyu-infographic でインフォグラフィックを生成
    ↓
baoyu-slide-deck でプレゼン資料を生成
    ↓
baoyu-translate で多言語化
    ↓
baoyu-markdown-to-html でHTML出力
```

## この Part の学習の流れ

| # | セクション | 内容 | 時間 |
|---|-----------|------|------|
| 6-1 | baoyu-skills エコシステム入門 | 全体像、インストール、3カテゴリ | 15分 |
| 6-2 | コンテンツ生成スキルを使いこなす | 主要スキルの実践的な使い方 | 20分 |
| 6-3 | AI画像生成バックエンドの選択 | 画像生成バックエンドの比較と使い分け | 15分 |
| 6-4 | 実プロジェクトでのスキル連携 | 図→インフォグラフィック→スライド→公開の自動化 | 20分 |
| 6-5 | カスタムスキル開発（baoyu流） | baoyuの設計パターンを真似た自前スキルの作り方 | 20分 |

## 前提知識

この Part を学習するには、以下の知識を前提とします：

- Part 1〜5 の内容を理解している
- Agent Skills の基本（SKILL.md の構造、スラッシュコマンド）を理解している
- Claude Code または Codex CLI が利用可能

## 次のステップ

→ [6-2: コンテンツ生成スキルを使いこなす](02-content-skills-in-action.md)
