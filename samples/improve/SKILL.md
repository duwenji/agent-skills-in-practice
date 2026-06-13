---
id: improve
name: コード改善（improve）
description: 既存コードを分析し、パフォーマンス最適化・リファクタリング・モダナイゼーションの改善提案を行います
tags:
  - refactoring
  - performance
  - optimization
  - modernization
---

# improve — コード改善スキル

## 概要

既存のコードを分析し、パフォーマンス最適化、リファクタリング、モダナイゼーションの観点から改善提案を行います。各提案には難易度と期待効果の評価が付与され、優先順位付けが可能です。

## 利用シーン

- レガシーコードのモダナイゼーション
- パフォーマンスボトルネックの特定と改善
- コードベース全体の品質向上計画
- 技術負債の返済計画策定

## 入力パラメータ

| パラメータ | 型 | 必須 | 説明 |
|-----------|------|------|------|
| `code` | string | ✅ | 改善対象のコード |
| `language` | string | ✅ | プログラミング言語 |
| `improvement_type` | string | ❌ | 改善タイプ（performance / refactoring / modernization / all） |
| `max_suggestions` | number | ❌ | 最大提案数（デフォルト: 5） |
| `include_code_examples` | boolean | ❌ | 改善後のコード例を含めるか（デフォルト: true） |
| `constraints` | string[] | ❌ | 制約条件（例: "IE11対応", "bundle size < 200KB"） |

## 出力スキーマ

```json
{
  "summary": {
    "total_suggestions": 5,
    "estimated_effort_hours": 8,
    "overall_improvement_potential": "high"
  },
  "suggestions": [
    {
      "id": "OPT-1",
      "type": "performance",
      "title": "メモ化による再レンダリング最適化",
      "difficulty": "easy",
      "impact": "high",
      "location": {
        "file": "src/components/UserList.tsx",
        "line": 15
      },
      "current_code": "const UserList = ({ users }) => { ... }",
      "improved_code": "const UserList = React.memo(({ users }) => { ... })",
      "rationale": "users が変更されていない場合の不要な再レンダリングを防止",
      "estimated_improvement": "レンダリング回数が約60%削減"
    }
  ],
  "quick_wins": ["OPT-1", "REF-2"],
  "long_term": ["MOD-3"]
}
```

## 実践ハンズオン

### ステップ1: Skill Creator で生成
Copilot Editor で以下を入力：
```
@copilot improve スキルを作成して。
既存コードを分析し、パフォーマンス最適化・リファクタリング・モダナイゼーションの
改善提案を行うスキル。各提案に難易度と効果の評価を付けて。
```

### ステップ2: テスト実行
以下のコードでテスト：
```
@improve 
言語: TypeScript/React

function SearchResults({ query, data }) {
  const [results, setResults] = useState([]);
  useEffect(() => {
    if (data) {
      const filtered = data.filter(item => 
        item.name.includes(query) || item.description.includes(query)
      );
      setResults(filtered);
    }
  }, [query, data]);
  return <div>{results.map(r => <SearchCard item={r} />)}</div>;
}
```

## テストケース

| # | テスト内容 | 期待結果 |
|---|-----------|---------|
| 1 | 空コードを入力 | エラーメッセージを返す |
| 2 | パフォーマンス問題を含むコード | メモ化や不要レンダリングの改善提案を返す |
| 3 | improvement_type=refactoring のみ | リファクタリング提案のみを返す |
| 4 | 制約条件あり（IE11対応） | 制約を考慮した提案を返す |
| 5 | 最適化済みのコード | 改善点なしの結果を返す |
