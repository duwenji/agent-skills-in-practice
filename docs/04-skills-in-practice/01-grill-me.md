# 4-1: grill-me — コードレビュースキル

> **学習時間**: 25分 | **難易度**: ⭐⭐⭐ | **カテゴリ**: 品質検証

## 概要

**grill-me** は、コードの品質を「可読性」「パフォーマンス」「セキュリティ」「保守性」の4軸で徹底レビューするスキルです。PR レビュー前のセルフチェックや、チームのコードレビュー基準の統一に活用できます。

フロントエンド（React/TypeScript）に最適化されていますが、汎用的にも使用可能です。

## 学習目標

- Skill Creator を使ってコードレビュースキルを生成できる
- 4軸のレビュー観点を理解し、カスタマイズできる
- 出力スキーマを解析し、必要な情報を抽出できる

## 利用シーン

| シーン | 説明 |
|-------|------|
| PR レビュー前のセルフチェック | 自分のコードを事前にレビューして品質を高める |
| コード品質の統一基準 | チーム全体で同じ基準でコードレビューを実施 |
| 教育ツール | ジュニア開発者にコードレビューの観点を教える |
| レガシーコードの品質評価 | 既存コードの品質を数値化して改善計画を立てる |

## SKILL.md 完全定義

`samples/grill-me/SKILL.md` に完全な定義があります。以下は主要部分の抜粋です：

```yaml
---
id: grill-me
name: コードレビュー（grill-me）
description: コードの品質を「可読性」「パフォーマンス」「セキュリティ」「保守性」の4軸で徹底レビューします
tags:
  - code-review
  - quality
  - frontend
  - best-practices
---
```

### 入力パラメータ

| パラメータ | 型 | 必須 | デフォルト | 説明 |
|-----------|------|------|-----------|------|
| `code` | string | ✅ | — | レビュー対象のコード |
| `language` | string | ✅ | — | プログラミング言語 |
| `framework` | string | ❌ | — | フレームワーク |
| `focus_areas` | string[] | ❌ | 全4観点 | フォーカスする観点 |
| `max_issues` | number | ❌ | 10 | 最大報告数 |
| `include_fixes` | boolean | ❌ | true | 修正案を含めるか |

### 出力スキーマ

```json
{
  "summary": {
    "total_issues": 5,
    "critical": 1,
    "major": 2,
    "minor": 2,
    "overall_score": 72
  },
  "categories": {
    "readability": { "score": 80, "issues": [...] },
    "performance": { "score": 65, "issues": [...] },
    "security": { "score": 90, "issues": [...] },
    "maintainability": { "score": 55, "issues": [...] }
  },
  "issues": [
    {
      "id": "R1",
      "category": "readability",
      "severity": "major",
      "line": 42,
      "message": "関数が長すぎます（120行）",
      "suggestion": "handleSubmit を3つの関数に分割"
    }
  ],
  "positive_feedback": ["エラーハンドリングが適切です"]
}
```

## 実践ハンズオン

### ステップ1: Skill Creator でスキルを生成

GitHub Copilot Editor で以下のプロンプトを入力します：

```
@copilot grill-me スキルを作成して。
コードレビューを「可読性」「パフォーマンス」「セキュリティ」「保守性」の4軸で行い、
優先度付きの改善案を提示するスキル。
出力はJSON形式で、全体スコアとカテゴリ別スコアを含めて。
```

### ステップ2: 生成結果を確認

`.github/skills/grill-me/SKILL.md` に生成されたファイルを確認します。必要に応じて以下のカスタマイズを行います：

- レビュー観点の追加/削除
- 出力形式の調整
- デフォルト値の変更

### ステップ3: テスト実行

以下のコードでテスト実行します：

```
@grill-me 以下のReactコンポーネントをレビューして：

function UserList() {
  const [users, setUsers] = useState([]);
  useEffect(() => {
    fetch('/api/users').then(r => r.json()).then(setUsers);
  });
  return <ul>{users.map(u => <li>{u.name}</li>)}</ul>;
}
```

### 期待される結果

- **可読性**: コンポーネント名は適切、JSX はシンプル
- **パフォーマンス**: `useEffect` に依存配列がない → 無限ループの可能性を指摘
- **セキュリティ**: `u.name` のXSS対策がない → `dangerouslySetInnerHTML` の確認を促す
- **保守性**: ローディング状態やエラー状態のハンドリングがない

## カスタマイズ例

### レビュー観点の追加

フロントエンド特化の観点を追加する場合：

```
@copilot grill-me に「アクセシビリティ」と「テスト容易性」の
2つの観点を追加して。各観点の評価基準も定義して。
```

### 出力形式の変更

簡略化した出力が必要な場合：

```
@copilot grill-me の出力を、全体スコアとクリティカルな問題のみに
絞った簡略版に変更して。
```

## テストケース

| # | テスト内容 | 入力 | 期待結果 |
|---|-----------|------|---------|
| 1 | 空コード | code="" | エラーメッセージを返す |
| 2 | 適切なReactコンポーネント | 上記ハンズオンコード | 4軸のレビュー結果 + スコア |
| 3 | セキュリティフォーカス | focus_areas=["security"] | セキュリティ観点のみ |
| 4 | 修正案なし | include_fixes=false | 問題点のみ、修正案なし |
| 5 | 長大なコード | 500行以上のコード | 最大10件に絞った結果 |

## 次のステップ

- [triage: Issue分析スキル](02-triage-issue-analysis.md) に進む
- [improve: コード改善スキル](03-improve.md) で grill-me の結果を基に改善を自動化
- SKILL.md を `.github/skills/grill-me/` に配置して実際のプロジェクトで使用
