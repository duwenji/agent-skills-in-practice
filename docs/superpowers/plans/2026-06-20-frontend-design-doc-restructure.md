# frontend-design ドキュメント再構成 実装計画

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** `docs/03-frameworks/03-3a-frontend-design.md` を物語構造（Before/After フック → 説明 → リファレンス）に再構成し、「Copilot を使っているが雑なコードが出てくる」読者が冒頭で即座に価値を感じられるようにする。

**Architecture:** 既存ファイルを完全に書き直す。情報はゼロ削除で、冒頭に Before/After フック2セクションを追加、`## 詳細説明` を3つの独立 `##` セクションに分割昇格、`## 同じ依頼で何が変わるのか` を独立セクションとして追加する。

**Tech Stack:** Markdown のみ。コード変更なし。

## Global Constraints

- 対象ファイル: `docs/03-frameworks/03-3a-frontend-design.md` のみ
- 情報ゼロ削除: 入力パラメータ全行・出力スキーマ JSON・4観点テーブル・特徴テーブル・呼び出し例・design_focus 例・次のステップリンクは全て保持
- `## 同じ依頼で何が変わるのか` は独立した `##` セクションとして配置（他セクション内に入れ子にしない）

---

### Task 1: 03-3a-frontend-design.md を新構成で書き直す

**Files:**
- Modify: `docs/03-frameworks/03-3a-frontend-design.md`

**Interfaces:**
- Consumes: 設計仕様 `docs/superpowers/specs/2026-06-20-frontend-design-doc-restructure-design.md`
- Produces: 再構成済みの `docs/03-frameworks/03-3a-frontend-design.md`

- [ ] **Step 1: 現行ファイルを読んで内容を把握する**

```bash
cat docs/03-frameworks/03-3a-frontend-design.md
```

現行ファイルの構成を確認し、保持必須コンテンツを頭に入れる。

- [ ] **Step 2: 以下の完全な新ファイル内容でファイルを書き直す**

`docs/03-frameworks/03-3a-frontend-design.md` の全内容を以下に置き換える（コードブロック内のバッククォートはそのまま使用すること）：

---

```markdown
# 3-3a: frontend-design — フロントエンド設計支援スキル（Anthropic 公式）

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

## 次のステップ

→ [3-3b: ui-ux-pro-max — UI/UX最適化スキル](03-3b-ui-ux-pro-max.md) で、設計したUIの品質を監査する方法を学ぶ
→ [3-4: 問題 × スキル解決マッピング](04-problem-skill-mapping.md) で、全スキルの関係性を整理する
```

---

- [ ] **Step 3: 保持必須コンテンツの存在を確認する（10項目）**

以下を1つずつ確認する：

1. `@frontend-design` 呼び出し例コードブロック（`## 使い方` 内）が存在する
2. 特徴テーブル（提供元・動作環境・呼び出し方・スキル種別 の4行）が存在する
3. `## 4つの設計観点` テーブル（観点・説明・出力例 の3列、4行）が存在する
4. `## 入力パラメータ` テーブル（6パラメータ全行: requirements, tech_stack, current_architecture, constraints, design_focus, include_diagram）が存在する
5. `## 出力スキーマ` JSON（architecture_overview / component_tree / state_management / data_flow / optimization_recommendations）が存在する
6. `design_focus=state` の絞り込み例が存在する
7. `design_focus=components` の絞り込み例が存在する
8. 次のステップリンク `03-3b-ui-ux-pro-max.md` が存在する
9. 次のステップリンク `04-problem-skill-mapping.md` が存在する
10. `> Copilot にプリインストール済みのため` の注記が存在する

- [ ] **Step 4: 追加・変更コンテンツの存在を確認する（8項目）**

1. `## Copilot だけで頼むと` セクションが冒頭付近に存在する
2. `SearchComponent` の 300行コードブロック（Before シーン）が存在する
3. 「動く。でも誰も触りたくないコードが完成した。」の締め文が存在する
4. `## @frontend-design を加えると` セクションが存在する
5. `SearchContainer` ツリー図（After シーン）が存在する
6. 「コードの前に設計図が出てくる。」の締め文が存在する
7. `## 同じ依頼で何が変わるのか` が独立した `##` セクションとして存在する（他セクション内に入れ子ではない）
8. 「必要なときに参照してください。最初から全部覚える必要はありません。」が `## 4つの設計観点` 直下に存在する

- [ ] **Step 5: 削除必須コンテンツの不在を確認する（2項目）**

1. `## 詳細説明` セクションが存在しない
2. `> **注意**: frontend-design は Anthropic 公式提供のスキルです。Skill Creator で生成する必要はなく、GitHub Copilot にプリインストールされています。` ブロックが存在しない

- [ ] **Step 6: コミットする**

```bash
git add docs/03-frameworks/03-3a-frontend-design.md
git commit -m "docs: 03-3a-frontend-design.md を物語構造に再構成"
```

---

### Task 2: 実装計画ファイル自体をコミットする

**Files:**
- Commit: `docs/superpowers/plans/2026-06-20-frontend-design-doc-restructure.md`

- [ ] **Step 1: 計画ファイルをコミットする**

```bash
git add docs/superpowers/plans/2026-06-20-frontend-design-doc-restructure.md
git commit -m "docs: 03-3a-frontend-design.md リストラクチャリングの実装計画を追加"
```
