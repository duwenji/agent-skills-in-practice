# 4-4: frontend-design — フロントエンド設計支援スキル

> **学習時間**: 25分 | **難易度**: ⭐⭐⭐ | **カテゴリ**: アーキテクチャ

## 概要

**frontend-design** は、フロントエンドアプリケーションのアーキテクチャ設計を支援するスキルです。コンポーネント分割、状態管理戦略、データフロー設計、レンダリング最適化の観点から、要件に最適な設計案を提案します。

## 学習目標

- Skill Creator を使って設計支援スキルを生成できる
- コンポーネント設計のベストプラクティスを理解する
- 状態管理戦略を要件に合わせて選択できる

## 利用シーン

| シーン | 説明 |
|-------|------|
| 新規機能のアーキテクチャ設計 | 要件から最適なコンポーネント構成を導出 |
| 既存コンポーネントのリファクタリング | 肥大化したコンポーネントの分割計画 |
| 状態管理ライブラリの選定 | プロジェクト規模に適した状態管理戦略の提案 |
| パフォーマンス改善の設計見直し | レンダリング最適化のための設計変更 |

## SKILL.md 完全定義

`samples/frontend-design/SKILL.md` に完全な定義があります。

### 入力パラメータ

| パラメータ | 型 | 必須 | デフォルト | 説明 |
|-----------|------|------|-----------|------|
| `requirements` | string | ✅ | — | 機能要件の説明 |
| `tech_stack` | string | ✅ | — | 技術スタック |
| `current_architecture` | string | ❌ | — | 現在のアーキテクチャ説明 |
| `constraints` | string[] | ❌ | — | 制約条件 |
| `design_focus` | string | ❌ | "all" | 設計フォーカス |
| `include_diagram` | boolean | ❌ | false | コンポーネント図を含めるか |

### 出力スキーマ

```json
{
  "architecture_overview": {
    "pattern": "Container/Presentational + Custom Hooks",
    "rationale": "関心の分離とテスト容易性を両立するため"
  },
  "component_tree": {
    "root": "App",
    "children": [
      {
        "name": "SearchContainer",
        "type": "container",
        "children": ["SearchForm", "SearchResults", "SearchPagination"],
        "responsibility": "検索状態の管理と子コンポーネントへのデータ受け渡し"
      }
    ]
  },
  "state_management": {
    "strategy": "Zustand + React Query",
    "stores": [
      {
        "name": "searchStore",
        "state": ["query", "filters", "results", "loading", "error"],
        "actions": ["search", "setFilters", "clearResults"]
      }
    ],
    "server_state": {
      "tool": "React Query",
      "queries": ["searchResults", "suggestions"],
      "mutations": ["saveSearch", "deleteSearch"]
    }
  },
  "data_flow": {
    "direction": "unidirectional",
    "description": "ユーザー入力 → Container → Custom Hook → API → Store → 再レンダリング"
  },
  "optimization_recommendations": [
    {
      "area": "rendering",
      "suggestion": "SearchResults に React.memo + virtual scrolling を適用",
      "expected_impact": "リストレンダリングのパフォーマンスが約5倍向上"
    }
  ]
}
```

## 実践ハンズオン

### ステップ1: Skill Creator でスキルを生成

```
@copilot frontend-design スキルを作成して。
フロントエンドのアーキテクチャ設計を支援するスキル。
コンポーネント分割、状態管理、データフロー、レンダリング最適化の
観点から設計案を提案する。
```

### ステップ2: テスト実行

以下の要件でテスト：

```
@frontend-design 
要件: 商品検索機能。ユーザーがキーワードを入力すると、
リアルタイムで候補表示、確定後に検索結果一覧を表示。
フィルター（カテゴリ、価格帯）とページネーション付き。
技術スタック: React + TypeScript + Tailwind CSS
```

### 期待される結果

- **アーキテクチャ**: Container/Presentational パターン
- **コンポーネント分割**: SearchContainer, SearchForm, SearchSuggestions, SearchResults, SearchPagination, FilterPanel
- **状態管理**: React Query（サーバー状態）+ Zustand（UI状態）
- **最適化**: 検索結果の仮想スクロール、入力のデバウンス

## 設計フォーカスの使い分け

状況に応じて設計フォーカスを変更することで、必要な情報に絞った設計案を得られます：

```
# 状態管理だけ知りたい場合
@frontend-design design_focus=state
要件: ...

# コンポーネント構成だけ知りたい場合
@frontend-design design_focus=components
要件: ...
```

## テストケース

| # | テスト内容 | 期待結果 |
|---|-----------|---------|
| 1 | 空の要件 | エラーメッセージを返す |
| 2 | シンプルなフォーム要件 | 適切なコンポーネント分割案 |
| 3 | 複雑な状態管理が必要な要件 | 状態管理戦略を含む設計案 |
| 4 | パフォーマンス制約あり | 制約を考慮した最適化提案 |
| 5 | design_focus=components のみ | コンポーネント設計のみ |

## 次のステップ

- [ui-ux-pro-max: UI/UX最適化スキル](05-ui-ux-pro-max.md) で設計したUIの品質を監査
- [Part 5-1: パイプライン連携](../06-advanced/01-pipeline-integration.md) で frontend-design → ui-ux-pro-max の連携
