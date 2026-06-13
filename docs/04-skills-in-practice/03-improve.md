# 4-3: improve — コード改善スキル

> **学習時間**: 25分 | **難易度**: ⭐⭐⭐ | **カテゴリ**: リファクタリング

## 概要

**improve** は、既存のコードを分析し、パフォーマンス最適化、リファクタリング、モダナイゼーションの観点から改善提案を行うスキルです。各提案には難易度と期待効果の評価が付与され、優先順位付けが可能です。

## 学習目標

- Skill Creator を使ってコード改善スキルを生成できる
- パフォーマンス最適化の提案を理解し、適用できる
- 制約条件を考慮した改善提案を引き出せる

## 利用シーン

| シーン | 説明 |
|-------|------|
| レガシーコードのモダナイゼーション | 古いコードを最新のベストプラクティスに更新 |
| パフォーマンスボトルネックの特定 | 処理が遅い箇所を特定し、改善案を提示 |
| 技術負債の返済計画 | コードベース全体の改善点を洗い出し、優先順位付け |
| コードレビューの補完 | レビューでは見つけにくいパフォーマンス問題を発見 |

## SKILL.md 完全定義

`samples/improve/SKILL.md` に完全な定義があります。

### 入力パラメータ

| パラメータ | 型 | 必須 | デフォルト | 説明 |
|-----------|------|------|-----------|------|
| `code` | string | ✅ | — | 改善対象のコード |
| `language` | string | ✅ | — | プログラミング言語 |
| `improvement_type` | string | ❌ | "all" | 改善タイプ（performance / refactoring / modernization / all） |
| `max_suggestions` | number | ❌ | 5 | 最大提案数 |
| `include_code_examples` | boolean | ❌ | true | 改善後のコード例を含めるか |
| `constraints` | string[] | ❌ | — | 制約条件 |

### 出力スキーマ

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
      "location": { "file": "src/components/UserList.tsx", "line": 15 },
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

### ステップ1: Skill Creator でスキルを生成

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

### 期待される結果

- **パフォーマンス**: `useMemo` でフィルタリング処理をメモ化、`React.memo` で `SearchCard` をラップ
- **リファクタリング**: フィルタリングロジックをカスタムフックに分離
- **クイックウィン**: `React.memo` の追加（難易度: easy, 効果: high）

## 制約条件を使った高度な活用

実際のプロジェクトでは様々な制約があります。制約を指定することで、現実的な改善提案を得られます：

```
@improve 
言語: JavaScript
制約条件: ["IE11対応", "bundle size < 200KB", "jQueryからの移行途中"]

[既存コード]
```

## テストケース

| # | テスト内容 | 期待結果 |
|---|-----------|---------|
| 1 | 空コード | エラーメッセージを返す |
| 2 | パフォーマンス問題を含むコード | メモ化や不要レンダリングの改善提案 |
| 3 | improvement_type=refactoring のみ | リファクタリング提案のみ |
| 4 | 制約条件あり（IE11対応） | 制約を考慮した提案 |
| 5 | 最適化済みのコード | 改善点なしの結果 |

## 次のステップ

- [frontend-design: 設計支援スキル](04-frontend-design.md) でアーキテクチャレベルからの改善
- [Part 5-1: パイプライン連携](../06-advanced/01-pipeline-integration.md) で grill-me → improve の連携
