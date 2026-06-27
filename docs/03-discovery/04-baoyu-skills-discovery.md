# baoyu-skills で学ぶ実践的スキル発見

> **学習時間**: 15分 | **難易度**: ⭐⭐

## 概要

ここまで Find Skills や skill.sh の使い方を学びました。このセクションでは、**実際に GitHub 上で公開されている人気スキルリポジトリ**を題材に、スキル発見の実践練習を行います。

題材とするのは **JimLiu/baoyu-skills**（21,000+ Stars）です。このリポジトリは21のスキルを3カテゴリで提供しており、スキル発見・評価・選択の良い教材となります。

## baoyu-skills とは

**baoyu-skills** は、Jim Liu 氏が開発した AI エージェント（Claude Code, Codex 等）向けのスキル集です。

| 項目 | 内容 |
|------|------|
| **リポジトリ** | [github.com/JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) |
| **スター数** | 21,000+ |
| **スキル数** | 21 |
| **言語** | TypeScript（Bun ランタイム） |
| **ライセンス** | MIT-0 |
| **インストール** | `npx skills add jimliu/baoyu-skills` |

### 3つのカテゴリ

baoyu-skills は以下の3カテゴリで構成されています：

| カテゴリ | 説明 | スキル数 |
|---------|------|---------|
| **Content Skills** | コンテンツ生成・公開（画像、スライド、漫画、図表、SNS投稿） | 7 |
| **AI Generation Skills** | AI 生成バックエンド（画像生成、Web経由生成） | 3 |
| **Utility Skills** | コンテンツ処理（変換、圧縮、翻訳、公開） | 11+ |

## 実践: baoyu-skills を探索する

### ステップ1: リポジトリを調査する

まずはリポジトリの全体像を把握しましょう。GitHub 上で以下の情報を確認します：

1. **README.md** — リポジトリの説明、インストール方法、全スキル一覧
2. **スキル構成** — `skills/` ディレクトリに各スキルが配置されている
3. **スキル定義** — 各スキルフォルダ内の `SKILL.md` がスキルの実体

```bash
# GitHub CLI でリポジトリ情報を確認
gh repo view JimLiu/baoyu-skills

# スキル一覧を取得
gh api repos/JimLiu/baoyu-skills/contents/skills --jq '.[].name'
```

### ステップ2: スキルを評価する

スキルを選ぶ際の評価基準を、baoyu-skills を例に確認します：

| 評価基準 | baoyu-skills での確認ポイント |
|---------|---------------------------|
| **目的の一致** | 自分のユースケースに合うカテゴリがあるか |
| **品質** | 各スキルの説明が明確で、使用例が充実しているか |
| **メンテナンス** | 最終更新日が新しいか、CHANGELOG が整備されているか |
| **人気** | 21,000+ Stars は信頼性の指標 |
| **互換性** | Claude Code / Codex / Cursor など複数エージェント対応 |

### ステップ3: スキルをインストールする

baoyu-skills は複数の方法でインストールできます：

```bash
# 方法1: npx skills add（推奨）
npx skills add jimliu/baoyu-skills

# 方法2: Claude Code プラグインとして
# Claude Code セッション内で以下を実行
/plugin marketplace add JimLiu/baoyu-skills
/plugin install baoyu-skills@baoyu-skills

# 方法3: エージェントに直接依頼
# 「Please install Skills from github.com/JimLiu/baoyu-skills」
```

### ステップ4: スキルを選定する

21ものスキルがある場合、**全てをインストールする必要はありません**。必要なスキルだけを選びましょう。

**ユースケース別おすすめスキル**:

| 目的 | おすすめスキル |
|------|--------------|
| 技術記事に図解を入れたい | baoyu-diagram, baoyu-infographic |
| ブログのカバー画像を作りたい | baoyu-cover-image |
| プレゼン資料を作りたい | baoyu-slide-deck |
| 知識を漫画で伝えたい | baoyu-comic |
| SNS 投稿用画像を作りたい | baoyu-xhs-images |
| 記事を翻訳したい | baoyu-translate |
| Markdown を HTML に変換したい | baoyu-markdown-to-html |

## baoyu-skills の設計パターン

baoyu-skills の各スキルは、以下の共通パターンで設計されています。これはスキル開発の参考にもなります：

```
skills/baoyu-<name>/
├── SKILL.md          # スキル定義（YAML front matter + 説明）
├── scripts/          # 実行スクリプト（TypeScript / Bun）
├── references/       # 参考資料
└── prompts/          # プロンプトテンプレート
```

### SKILL.md の構造例

baoyu-skills の SKILL.md は以下のような frontmatter 構造です：

```yaml
---
name: baoyu-diagram
description: Generates publication-ready SVG diagrams from source material. Use when user asks to create diagrams, flowcharts, architecture diagrams, or visual explanations.
version: 1.0.0
metadata:
  openclaw:
    homepage: https://github.com/JimLiu/baoyu-skills#baoyu-diagram
    requires:
      anyBins:
        - bun
        - npx
---
```

**各フィールドのルール**:
- `name`: 64文字以内、小文字英数字とハイフンのみ、`baoyu-` プレフィックス必須
- `description`: 1024文字以内、三人称で記述（"Generates..." / "Use when..."）
- `version`: semver 形式
- `metadata.openclaw.requires.anyBins`: スクリプト実行に必要なランタイム

## 学びのポイント

baoyu-skills を題材にすることで、以下のスキル発見の実践が身につきます：

1. **README の読み解き方** — リポジトリの説明から必要なスキルを見極める
2. **スキルの評価基準** — Stars 数だけでなく、メンテナンス状況や品質も確認する
3. **部分的な導入** — 全てをインストールせず、必要なスキルだけを選ぶ判断力
4. **設計パターンの学習** — 優れたスキルリポジトリから設計パターンを学ぶ

## 次のステップ

→ [Part 4: 概念フレームワークと課題認識](../04-frameworks/01-superpowers-overview.md)

---

> **💡 参考リンク**: [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | [npx skills](https://www.npmjs.com/package/skills)
