# 4-4: frontend-design — フロントエンド設計支援スキル（Anthropic 公式）

> **学習時間**: 15分 | **難易度**: ⭐⭐

## Copilot だけで頼むと

```
あなた: 商品検索機能を作って。キーワード入力 → リアルタイム候補 → 結果一覧。
        React + TypeScript。

Copilot: わかりました。SearchComponent.tsx に実装します：

export const SearchComponent = () => {
  const [query, setQuery] = useState('')
  const [suggestions, setSuggestions] = useState([])
  const [results, setResults] = useState([])
  const [loading, setLoading] = useState(false)
  const [page, setCurrentPage] = useState(1)
  // ...（300行へ続く）
```

動く。でも誰も触りたくないコードが完成した。

## @frontend-design を加えると

```
あなた: @frontend-design
要件: 商品検索機能。キーワード入力→候補表示→結果一覧。
技術スタック: React + TypeScript

Copilot: アーキテクチャを設計します。

コンポーネント構成:
  SearchContainer（状態管理）
    ├── SearchForm（入力UI）
    ├── SuggestionList（候補表示）
    └── SearchResults（結果一覧）

状態管理:
  Zustand: searchStore（query, results, loading）
  React Query: useSearchSuggestions / useSearchResults

データフロー:
  入力 → debounce(300ms) → API → 候補表示
      → 確定 → searchStore → 結果表示
```

コードの前に設計図が出てくる。

## frontend-design とは

Anthropic 公式提供のフロントエンド設計支援スキルです。コンポーネント分割・状態管理・データフロー・レンダリング最適化の4観点から、要件に合ったアーキテクチャ設計案を提案します。

| 項目 | 内容 |
|------|------|
| **提供元** | Anthropic（公式） |
| **動作環境** | GitHub Copilot（VS Code チャット / エージェントモード） |
| **呼び出し方** | `@frontend-design` |
| **スキル種別** | アーキテクチャ設計支援 |
| **設計観点** | コンポーネント分割 / 状態管理 / データフロー / レンダリング最適化 |

> Copilot にプリインストール済みのため、Skill Creator で作成する必要はありません。

## 同じ依頼で何が変わるのか

| 観点 | Copilot 単体 | @frontend-design あり |
|------|-------------|----------------------|
| **コンポーネント** | 1ファイルに全機能 | Container/Presentational に分割 |
| **状態管理** | useState を羅列 | Zustand + React Query に最適化 |
| **データフロー** | 暗黙的・双方向 | 単方向フローを明示 |
| **最初の出力** | コード | 設計図 |
| **保守性** | 触るのが怖い | 誰でも変更できる |

## 4つの設計観点

必要なときに参照してください。最初から全部覚える必要はありません。

| 観点 | 説明 | 出力例 |
|------|------|--------|
| **コンポーネント分割** | 関心の分離に基づいた適切なコンポーネント構成 | Container/Presentational パターン、責務の明確化 |
| **状態管理戦略** | プロジェクト規模に適した状態管理の選定と設計 | Zustand + React Query、Store 設計、アクション定義 |
| **データフロー設計** | 単方向データフローを基本としたデータの流れの設計 | ユーザー入力 → Container → Custom Hook → API → Store → 再レンダリング |
| **レンダリング最適化** | パフォーマンスを考慮したレンダリング戦略 | React.memo、仮想スクロール、入力デバウンス |

## 入力パラメータ

| パラメータ | 型 | 必須 | 説明 |
|-----------|------|------|------|
| `requirements` | string | ✅ | 機能要件の説明 |
| `tech_stack` | string | ✅ | 技術スタック（React, Vue, TypeScript 等） |
| `current_architecture` | string | ❌ | 現在のアーキテクチャ説明 |
| `constraints` | string[] | ❌ | 制約条件（パフォーマンス目標、バンドルサイズ等） |
| `design_focus` | string | ❌ | 設計フォーカス（components / state / data-flow / rendering / all） |
| `include_diagram` | boolean | ❌ | コンポーネント図を含めるか（デフォルト: false） |

## 出力スキーマ

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

## 使い方

### 1. 呼び出し方

VS Code の Copilot チャット（エージェントモード）で以下のように入力するだけで利用できます：

```
@frontend-design 
要件: 商品検索機能。ユーザーがキーワードを入力すると、
リアルタイムで候補表示、確定後に検索結果一覧を表示。
フィルター（カテゴリ、価格帯）とページネーション付き。
技術スタック: React + TypeScript + Tailwind CSS
```

### 2. 設計フォーカスの絞り込み

状況に応じて設計フォーカスを変更できます：

```
# 状態管理だけ知りたい場合
@frontend-design design_focus=state
要件: ...

# コンポーネント構成だけ知りたい場合
@frontend-design design_focus=components
要件: ...
```

## 設計の意図

### なぜコードより先にアーキテクチャを出力させるのか

通常のコード生成（要件→即コード）では、コンポーネントの責任範囲・状態の持ち場・データの流れが暗黙のままコードに埋め込まれる。一度コードが存在すると、設計の見直しはリファクタリングコストになる。アーキテクチャ（システムの構成要素と要素間の関係を定義した設計図）を先に出力させることで、コードを書く前に設計の問題を発見できる。

### なぜ観点を4つにするのか

コンポーネント分割・状態管理・データフロー・レンダリング最適化の4観点（UI の分割方法・データの置き場所・データの流れ・描画パフォーマンスの4つの設計軸）は、フロントエンドアーキテクチャの相互依存する4領域に対応している。コンポーネント構成を決めると状態の持ち場が絞られ、状態を決めるとデータフローが決まる順序関係があるため、この 4 つをセットで設計する。

**代替案との比較**:
- 観点をユーザーに選ばせる: 自由度が上がるが、相互依存を見落としやすい
- 2 観点に絞る（分割・状態のみ）: 素早く設計できるがレンダリング問題が後で表面化する

## この設計を変えるとき

- **小規模プロジェクトで観点を絞るとき**: ページ数が 3 以下の小規模サイトでは「コンポーネント分割のみ」に絞ってよい。状態管理とデータフローが自明なため設計コストが見合わない。
- **フレームワークが設計を規定するとき**: Next.js の App Router・Remix など、フレームワークがルーティングとデータフェッチを規定している場合、データフロー観点の設計はフレームワークの規約に委ねて省略してよい。

## 次のステップ

→ [4-5: ui-ux-pro-max — UI/UX最適化スキル](05-ui-ux-pro-max.md) で、設計したUIの品質を監査する方法を学ぶ
→ [5-7: 問題 × スキル解決マッピング](../05-skills-in-practice/07-problem-skill-mapping.md) で、全スキルの関係性を整理する
