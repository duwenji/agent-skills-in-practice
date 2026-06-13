---
id: triage
name: Issue分析（triage）
description: GitHub Issue の内容を分析し、優先度・カテゴリ・影響範囲を自動判定します
tags:
  - issue-analysis
  - triage
  - project-management
  - automation
---

# triage — Issue分析スキル

## 概要

GitHub Issue の内容を解析し、優先度（P0〜P3）の判定、カテゴリ分類、影響範囲の特定、対応推奨事項を自動生成します。プロジェクト管理の効率化とトリアージの標準化を実現します。

## 利用シーン

- 新規 Issue 作成時の自動トリアージ
- バックログ整理時の優先度再評価
- スプリント計画前の Issue 分析
- プロジェクト健全性の定期チェック

## 入力パラメータ

| パラメータ | 型 | 必須 | 説明 |
|-----------|------|------|------|
| `issue_title` | string | ✅ | Issue のタイトル |
| `issue_body` | string | ✅ | Issue の本文（Markdown形式） |
| `labels` | string[] | ❌ | 既存のラベル一覧 |
| `project_context` | string | ❌ | プロジェクトのコンテキスト情報 |
| `include_recommendation` | boolean | ❌ | 対応推奨事項を含めるか（デフォルト: true） |

## 出力スキーマ

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

### ステップ1: Skill Creator で生成
Copilot Editor で以下を入力：
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

## テストケース

| # | テスト内容 | 期待結果 |
|---|-----------|---------|
| 1 | 空の Issue を入力 | エラーメッセージを返す |
| 2 | 重大なバグ報告（P0相当） | P0判定 + 即時対応推奨を返す |
| 3 | 機能リクエスト（P3相当） | P3判定 + 次スプリント以降の推奨を返す |
| 4 | ラベル情報あり | 既存ラベルを考慮した分類を返す |
| 5 | 質問/議論系 Issue | 該当カテゴリ + 低優先度を返す |
