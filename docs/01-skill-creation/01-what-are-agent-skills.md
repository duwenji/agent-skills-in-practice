# 1-1: Agent Skills とは

> **学習時間**: 15分 | **難易度**: ⭐⭐

## 概要

**Agent Skills** は、AI エージェント（Claude Code、GitHub Copilot など）に特定のタスクを実行させるための指示書です。SKILL.md というファイルに手順やルールを記述し、エージェントが自動的に読み込んで実行します。

Agent Skills は **Agent Skills オープンスタンダード**（[agentskills.io](https://agentskills.io)）に基づく共通フォーマットで、複数の AI ツール間でスキルを共有できます。

## スキルを作成する2つのアプローチ

### アプローチ1: skill-creator スキルによる対話生成（Claude Code）

Claude Code には **skill-creator** というバンドルスキルが標準搭載されています（[anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/skill-creator)）。これはスキル作成のための本格的なフレームワークで、以下のプロセスを自動化します：

```mermaid
flowchart LR
    U[ユーザー] -->|「コードレビュースキルを作って」| CC[Claude Code]
    CC -->|skill-creator 対話生成| SKILL[SKILL.md 生成<br>.claude/skills/code-review/]
    SKILL -->|手動コピー| GH[SKILL.md 配置<br>.github/skills/code-review/]
    GH -->|自動読み込み| COPILOT[GitHub Copilot<br>VS Code で実行可能]
    
    style CC fill:#6B5B95,color:#fff,stroke:#333
    style COPILOT fill:#2DA44E,color:#fff,stroke:#333
```

**使い方**:
```bash
# Claude Code を起動
claude

# セッション内で skill-creator を呼び出す
/skill-creator

# または自然言語で依頼
コードレビュースキルを作成して
```

skill-creator スキルは以下のような対話を開始します：

```
Claude: どんなスキルを作りましょうか？
以下の点を教えてください：
1. このスキルに何をさせたいですか？
2. どのようなタイミングで発動すべきですか？
3. 出力形式の希望はありますか？
4. テストケースは必要ですか？
```

#### skill-creator の内部プロセス

skill-creator は単なる SKILL.md 生成ツールではなく、**スキル開発のライフサイクル全体**をカバーします：

| フェーズ | 内容 |
|---------|------|
| **1. 意図のヒアリング** | ユーザーの要件を対話で引き出す |
| **2. SKILL.md 作成** | ベストプラクティスに従った SKILL.md を生成 |
| **3. テストケース作成** | 2-3個の現実的なテストプロンプトを生成 |
| **4. 並列実行** | with-skill / baseline の両方を同時実行 |
| **5. 評価** | 定量的アサーション + 定性的レビュー |
| **6. 反復改善** | フィードバックに基づいてスキルを改善 |
| **7. Description最適化** | トリガー精度を自動最適化 |
| **8. パッケージング** | `.skill` ファイルとして出力 |

> **補足**: skill-creator は Claude Code 専用のツールですが、**生成された SKILL.md は Agent Skills オープンスタンダードに準拠しているため、そのまま GitHub Copilot でも使用できます**。詳細は [1-2: skill-creator で最初のスキルを作る](02-skill-creator-hands-on.md) で学びます。

### アプローチ2: 手書き SKILL.md

テキストエディタで直接 SKILL.md を作成する方法です。両プラットフォーム（Claude Code / GitHub Copilot）で共通のフォーマットです。

```bash
# スキルディレクトリを作成
mkdir -p .claude/skills/my-skill/

# SKILL.md を作成
touch .claude/skills/my-skill/SKILL.md
```

## 2つのアプローチの比較

| 観点 | skill-creator（対話生成） | 手書き SKILL.md |
|------|--------------------------|----------------|
| 作成方法 | Claude Code に対話で指示 | テキストエディタで直接記述 |
| 学習曲線 | ほぼゼロ | YAML/Markdown の知識が必要 |
| テスト自動化 | 自動生成・並列実行 | 手動テスト |
| 評価・ベンチマーク | 内蔵（定量的+定性的） | なし |
| 反復改善 | 構造化されたループ | 手動 |
| Description最適化 | 自動（トリガー精度向上） | 手動調整 |
| 対応プラットフォーム | Claude Code のみ | Claude Code + GitHub Copilot |
| 適した用途 | 本格的なスキル開発 | シンプルなスキル、クロスプラットフォーム |

## SKILL.md の基本構造

SKILL.md は YAML フロントマターと Markdown 本文の2部構成です：

```markdown
---
name: my-skill
description: スキルの説明（エージェントが自動読み込みの判断に使用）
---

# スキル名

## 概要
このスキルが何をするかの説明。

## 手順
1. ステップ1
2. ステップ2
3. ステップ3

## 注意事項
- 注意点1
- 注意点2
```

### フロントマターの役割

`name` と `description` フィールドは特に重要です：

- **`name`**: スキルの識別子。ディレクトリ名と一致させる
- **`description`**: エージェントが「今の会話に関連するスキルかどうか」を判断するための説明文。具体的かつ検索性の高い記述が推奨される

### スキルのディレクトリ構造

```
my-skill/
├── SKILL.md           # メインの指示（必須）
├── scripts/           # 実行可能コード（任意）
├── references/        # 参照ドキュメント（任意）
└── assets/            # 出力用テンプレート等（任意）
```

## スキルの配置場所

| 種類 | Claude Code | GitHub Copilot | 適用範囲 |
|------|-------------|----------------|---------|
| 個人用 | `~/.claude/skills/<name>/SKILL.md` | `~/.copilot/skills/<name>/SKILL.md` | 全プロジェクト |
| プロジェクト用 | `.claude/skills/<name>/SKILL.md` | `.github/skills/<name>/SKILL.md` | そのプロジェクトのみ |
| プラグイン | `<plugin>/skills/<name>/SKILL.md` | なし | プラグイン有効時 |

## スキルが使われるタイミング

スキルは以下の2つの方法で使われます：

1. **自動読み込み**: 会話の内容がスキルの `description` にマッチした場合、エージェントが自動的にスキルを読み込む
2. **明示的な呼び出し**: `/スキル名` で直接スキルを実行

## 次のステップ

→ [1-2: skill-creator で最初のスキルを作る](02-skill-creator-hands-on.md)
