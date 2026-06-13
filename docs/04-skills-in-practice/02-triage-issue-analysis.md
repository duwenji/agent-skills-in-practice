# 4-2: triage — Issue分析スキル

> **学習時間**: 25分 | **難易度**: ⭐⭐⭐ | **カテゴリ**: 優先順位付け

## 概要

**triage** は、GitHub Issue の内容を解析し、優先度（P0〜P3）の判定、カテゴリ分類、影響範囲の特定、対応推奨事項を自動生成するスキルです。プロジェクト管理の効率化とトリアージの標準化を実現します。

## 学習目標

- Skill Creator を使って Issue 分析スキルを生成できる
- 優先度判定ロジックを理解し、カスタマイズできる
- 出力結果をプロジェクト管理に活用できる

## 利用シーン

| シーン | 説明 |
|-------|------|
| 新規 Issue の自動トリアージ | 作成された Issue を自動的に分類・優先度付け |
| バックログ整理 | 既存 Issue の優先度を再評価して整理 |
| スプリント計画 | スプリント前に Issue を分析して計画を最適化 |
| プロジェクト健全性チェック | Issue の傾向を分析してプロジェクトの健全性を評価 |

## SKILL.md 完全定義

`samples/triage/SKILL.md` に完全な定義があります。

### 入力パラメータ

| パラメータ | 型 | 必須 | デフォルト | 説明 |
|-----------|------|------|-----------|------|
| `issue_title` | string | ✅ | — | Issue のタイトル |
| `issue_body` | string | ✅ | — | Issue の本文（Markdown形式） |
| `labels` | string[] | ❌ | — | 既存のラベル一覧 |
| `project_context` | string | ❌ | — | プロジェクトのコンテキスト情報 |
| `include_recommendation` | boolean | ❌ | true | 対応推奨事項を含めるか |

### 出力スキーマ

```json
{
  "priority": {
    "level": "P1",
    "rationale": "ユーザー認証に関する問題で、ログイン不能の可能性があるため"
  },
  "category": {
    "primary": "bug",
    "secondary": ["authentication", "security"],
    "confidence": 0.92
  },
  "impact": {
    "scope": "全ユーザー",
    "severity": "high",
    "urgency": "high"
  },
  "effort_estimate": {
    "level": "medium",
    "story_points": 5,
    "rationale": "認証フローの修正が必要"
  },
  "recommendation": {
    "action": "即時対応推奨",
    "suggested_assignee": "frontend-team",
    "suggested_sprint": "current",
    "next_steps": [
      "影響範囲の特定",
      "修正案の作成",
      "コードレビュー"
    ]
  }
}
```

## 実践ハンズオン

### ステップ1: Skill Creator でスキルを生成

```
@copilot triage スキルを作成して。
GitHub Issue を分析して優先度（P0〜P3）とカテゴリを自動判定し、
影響範囲と対応推奨事項を提示するスキル。
```

### ステップ2: テスト実行

以下の Issue 内容でテスト：

```
@triage 
タイトル: 「ログインページで500エラーが発生する」
本文: 本番環境でログインページにアクセスすると
Internal Server Error が発生します。
エラーログには「TypeError: Cannot read properties of null」と記録されています。
再現率は100%で、全ユーザーに影響します。
```

### 期待される結果

- **優先度**: P0（クリティカル）
- **カテゴリ**: bug / authentication
- **影響範囲**: 全ユーザー、高 severity
- **推奨**: 即時対応、ホットフィックス推奨

## 優先度判定基準のカスタマイズ

プロジェクトに合わせて優先度判定ロジックをカスタマイズできます：

```
@copilot triage の優先度判定基準を以下のように変更して：
- P0: セキュリティ脆弱性または全ユーザーに影響する障害
- P1: 主要機能の障害または多数ユーザーに影響
- P2: マイナー機能の障害または一部ユーザーに影響
- P3: 機能リクエスト、改善提案、ドキュメント更新
```

## テストケース

| # | テスト内容 | 期待結果 |
|---|-----------|---------|
| 1 | 空の Issue | エラーメッセージを返す |
| 2 | 重大なバグ報告（P0相当） | P0判定 + 即時対応推奨 |
| 3 | 機能リクエスト（P3相当） | P3判定 + 次スプリント以降 |
| 4 | ラベル情報あり | 既存ラベルを考慮した分類 |
| 5 | 質問/議論系 Issue | 該当カテゴリ + 低優先度 |

## 次のステップ

- [improve: コード改善スキル](03-improve.md) でトリアージ結果を基に改善
- [Part 5-1: パイプライン連携](../06-advanced/01-pipeline-integration.md) で triage → assign の自動化
