# 3-5: baoyu-skills のアーキテクチャ分析

> **学習時間**: 20分 | **難易度**: ⭐⭐

## 概要

ここまで Superpowers（Jesse Vincent）と gstack（Garry Tan）という2つの代表的なフレームワークを学びました。このセクションでは、**JimLiu/baoyu-skills** のアーキテクチャを分析し、21,000+ Stars を集めるスキル設計のベストプラクティスを学びます。

baoyu-skills は「コンテンツ生成」に特化したスキルセットであり、Superpowers（開発プロセス自動化プラグイン）や gstack（役割分担スキルセット）とは異なるアプローチを取っています。

## 3大フレームワークの比較

まず、このチュートリアルで扱う3つのアプローチを比較します：

| 観点 | Superpowers | gstack | baoyu-skills |
|------|------------|--------|-------------|
| **作者** | Jesse Vincent | Garry Tan | Jim Liu |
| **提供形態** | **Plugin**（Claude Plugin Marketplace） | **スキルセット**（git clone） | **スキルセット**（Pluginとしても配布可） |
| **目的** | 開発プロセス方法論 | 仮想的エンジニアリングチーム | コンテンツ生成 |
| **スキル数** | 15 | 31 | 21 |
| **起動方法** | 自動起動 | 明示的スラッシュコマンド | 明示的スラッシュコマンド |
| **特徴** | HARD-GATE, TDD強制 | 役割分担, 実ブラウザQA | 5Dスタイル体系, SVG直書き |
| **主なユーザー** | 開発者全般 | スタートアップ創業者 | コンテンツクリエイター |
| **Stars** | 10,000+ | 109,000+ | 21,000+ |

## baoyu-skills のアーキテクチャ

### 全体構成

baoyu-skills は以下の3層アーキテクチャで設計されています：

```
┌──────────────────────────────────────────────┐
│              プラグイン層                      │
│  .claude-plugin/marketplace.json              │
│  全スキルを1つのプラグインとして公開             │
├──────────────────────────────────────────────┤
│              スキル層                          │
│  skills/baoyu-<name>/SKILL.md                 │
│  21の独立したスキル（自己完結型）               │
├──────────────────────────────────────────────┤
│              実行層                            │
│  scripts/main.ts（TypeScript / Bun）          │
│  各スキルの実行ロジック                         │
└──────────────────────────────────────────────┘
```

### スキルの自己完結性（Self-Containment）

baoyu-skills の最も重要な設計原則は **Skill Self-Containment**（スキルの自己完結性）です。

各スキルは独立して配布・実行できるように設計されており、以下のルールに従います：

| ルール | 内容 |
|-------|------|
| **外部参照禁止** | SKILL.md からリポジトリ外のファイルを参照しない |
| **インライン化** | 共有ルール（画像生成、ユーザー入力など）は各スキルに直接記述 |
| **独立実行** | スキルフォルダを他のプロジェクトにコピーしても動作する |
| **500行制限** | SKILL.md 本文は500行以内に抑え、詳細は `references/` に分割 |

```
✅ 良い例: SKILL.md 内に画像生成バックエンドの選択ルールを直接記述
❌ 悪い例: SKILL.md から ../../docs/image-generation-tools.md を参照
```

### インライン化ルール（必須セクションの自己完結）

baoyu-skills では、以下の2つのセクションは **SKILL.md に直接インライン記述**することが必須です（外部ファイル参照禁止）：

| 必須セクション | 内容 | 配置場所 |
|---------------|------|---------|
| **User Input Tools** | ユーザー入力受付時のツール選択ルール（AskUserQuestion 優先、フォールバック、バッチング） | SKILL.md 冒頭（intro直後） |
| **Image Generation Tools** | 画像生成時のバックエンド選択ルール（利用可能なツールの検出、プロンプトファイル保存の義務） | User Input Tools の直後 |

これにより、スキルフォルダごと他のプロジェクトにコピーしても、一切の外部参照なしで完全に動作します。

### Progressive Disclosure（段階的開示）

SKILL.md を500行以内に保つため、baoyu-skills は **Progressive Disclosure** パターンを採用しています。詳細な定義（スタイル一覧、プロバイダー設定など）は `references/` フォルダに分割し、必要なときだけ読み込む構造です。これにより LLM のコンテキストウィンドウを節約しながら、必要な情報へアクセスできます。

### EXTEND.md プリファレンスシステム

baoyu-skills のもう一つの重要な設計パターンが **EXTEND.md** によるユーザー設定管理です。各スキルは3段階の優先順位（プロジェクト → XDG → ユーザーホーム）で設定ファイルを探索します。初回実行時に EXTEND.md が存在しない場合、スキルはブロッキング状態となり、対話形式で設定を収集してから処理を開始します。

> 実装の詳細は [Part 5-5: カスタムスキル開発](../05-content-creation/05-custom-skill-development.md) を参照してください。

### 5D スタイル体系

baoyu-skills のコンテンツ生成スキルは、**5次元のスタイル体系**を持っています。これは特に baoyu-cover-image で顕著です：

| 次元 | 説明 | 選択肢 |
|------|------|--------|
| **Type**（タイプ） | ビジュアルの種類 | hero, conceptual, typography, metaphor, scene, minimal |
| **Palette**（パレット） | 配色 | warm, elegant, cool, dark, earth, vivid, pastel, mono, retro, duotone, macaron |
| **Rendering**（レンダリング） | 描画スタイル | flat-vector, hand-drawn, painterly, digital, pixel, chalk, screen-print |
| **Text**（テキスト） | テキスト量 | none, title-only, title-subtitle, text-rich |
| **Mood**（ムード） | 雰囲気 | subtle, balanced, bold |

この5D体系により、77通りの組み合わせ（11パレット × 7レンダリング）から最適なスタイルを選択できます。

### スキル間の設計パターン比較

baoyu-skills 内の各スキルは、共通の設計パターンを持ちながらも、独自の拡張を加えています：

| スキル | スタイル体系 | レイアウト体系 | 出力形式 |
|--------|------------|--------------|---------|
| baoyu-cover-image | 5D（Type×Palette×Rendering×Text×Mood） | アスペクト比指定 | PNG |
| baoyu-infographic | 21レイアウト × 17スタイル | 情報構造ベース | PNG |
| baoyu-slide-deck | 4D（Texture×Mood×Typography×Density） | スライド数指定 | PPTX + PDF |
| baoyu-comic | 5アート × 7トーン | パネルレイアウト | 画像シーケンス |
| baoyu-diagram | デザインシステム統一 | 5図タイプ | SVG（ダークモード対応） |
| baoyu-xhs-images | 12スタイル × 6レイアウト | 情報密度ベース | 画像カード |

## クロスプラットフォーム対応

baoyu-skills は複数の AI エージェントで動作するよう設計されています：

| エージェント | 対応方法 |
|------------|---------|
| **Claude Code** | `.claude-plugin/marketplace.json` 経由のプラグイン |
| **OpenAI Codex CLI** | `npx skills add` でインストール |
| **Cursor** | スキルフォルダを直接配置 |
| **Claude Desktop** | ファイルベースのスキル読み込み |

## 画像生成バックエンドの抽象化

baoyu-skills の特筆すべき設計として、**画像生成バックエンドの抽象化**があります。コンテンツ生成スキルは実際の画像生成をバックエンドスキルに委譲します：

```
コンテンツスキル（例: baoyu-cover-image）
    ↓ 画像生成を依頼
画像生成バックエンド（複数選択可能）
    ├── baoyu-image-gen（OpenAI / Azure / Google / OpenRouter 等）
    ├── baoyu-danger-gemini-web（Gemini Web 経由）
    └── codex-imagegen（Codex CLI の画像生成機能）
```

各コンテンツスキルは「どのバックエンドを使うか」を気にせず、統一されたインターフェースで画像生成を依頼できます。バックエンドの選択は実行時に決定されます：

| 状況 | 動作 |
|------|------|
| バックエンドが1つだけ利用可能 | 自動的にそれを使用 |
| 複数のバックエンドが利用可能 | ユーザーに選択を確認 |
| バックエンドが利用不可 | ユーザーに設定方法を案内 |

## baoyu-skills から学ぶ設計の教訓

### 1. ドメイン特化の重要性

Superpowers（プラグイン）や gstack（スキルセット）が「開発プロセス全体」をカバーするのに対し、baoyu-skills は「コンテンツ生成」という特定ドメインに特化しています。これにより：

- 各スキルの役割が明確で、ユーザーが選びやすい
- スタイル体系などドメイン固有の設計を深堀りできる
- 競合するスキルが少なく、差別化しやすい

### 2. スタイル体系の設計

baoyu-skills の最大の強みは、**体系化されたスタイル設計**です。単なる「画像を生成する」ではなく：

- 次元分解（Type, Palette, Rendering など）
- 組み合わせ可能性（77通りの組み合わせ）
- 視覚的なプレビュー（スクリーンショット一覧）

これにより、ユーザーは直感的にスタイルを選択できます。

### 3. 自己完結型スキル

各スキルが独立して動作する設計は、以下のメリットをもたらします：

- 必要なスキルだけをインストールできる
- スキル単位でバージョン管理できる
- 他のプロジェクトに移植しやすい
- テストが容易

### 4. 実行スクリプトの分離

SKILL.md（定義）と scripts/main.ts（実行）を分離することで：

- スキルの説明と実装が明確に分離される
- 複雑なロジックをスクリプトに委譲できる
- テストが書きやすい

## 次のステップ

→ [3-9: 問題 × スキル解決マッピング](09-problem-skill-mapping.md)

---

> **💡 参考リンク**: [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | [CLAUDE.md](https://github.com/JimLiu/baoyu-skills/blob/main/CLAUDE.md)
