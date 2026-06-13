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

# grill-me — コードレビュースキル

## 概要

指定されたコードを4つの観点（可読性、パフォーマンス、セキュリティ、保守性）で分析し、改善点を優先度付きで提示します。フロントエンド（React/TypeScript）に最適化されていますが、汎用的にも使用可能です。

## 利用シーン

- PR レビュー前のセルフチェック
- コード品質の統一基準として
- チームのコードレビュー基準の教育ツールとして
- レガシーコードの品質評価

## 入力パラメータ

| パラメータ | 型 | 必須 | 説明 |
|-----------|------|------|------|
| `code` | string | ✅ | レビュー対象のコード |
| `language` | string | ✅ | プログラミング言語（TypeScript, JavaScript, Python 等） |
| `framework` | string | ❌ | フレームワーク（React, Vue, Angular 等） |
| `focus_areas` | string[] | ❌ | フォーカスする観点（デフォルト: 全4観点） |
| `max_issues` | number | ❌ | 最大報告数（デフォルト: 10） |
| `include_fixes` | boolean | ❌ | 修正案を含めるか（デフォルト: true） |

## 出力スキーマ

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
      "message": "関数が長すぎます（120行）。20行以下に分割を推奨",
      "suggestion": "handleSubmit を handleSubmitValidation, handleSubmitApiCall, handleSubmitRedirect に分割"
    }
  ],
  "positive_feedback": ["エラーハンドリングが適切です"]
}
```

## 実践ハンズオン

### ステップ1: Skill Creator で生成
Copilot Editor で以下を入力：
```
@copilot grill-me スキルを作成して。
コードレビューを「可読性」「パフォーマンス」「セキュリティ」「保守性」の4軸で行い、
優先度付きの改善案を提示するスキル。
出力はJSON形式で、全体スコアとカテゴリ別スコアを含めて。
```

### ステップ2: 生成された SKILL.md を確認
`.github/skills/grill-me/SKILL.md` に生成されたファイルを確認し、必要に応じて編集。

### ステップ3: テスト実行
以下のコードでテスト：
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

## テストケース

| # | テスト内容 | 期待結果 |
|---|-----------|---------|
| 1 | 空コードを入力 | エラーメッセージを返す |
| 2 | 適切なReactコンポーネント | 4軸のレビュー結果 + スコアを返す |
| 3 | focus_areas=["security"] のみ指定 | セキュリティ観点のみの結果を返す |
| 4 | include_fixes=false | 問題点のみ、修正案なしで返す |
| 5 | 長大なコード（500行以上） | 最大10件に絞った結果を返す |
