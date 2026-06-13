# 3-3a: frontend-design — フロントエンド設計支援スキル（Anthropic 公式）

> **学習時間**: 15分 | **難易度**: ⭐⭐

## 概要

**frontend-design** は、Anthropic が公式に提供するフロントエンド設計支援スキルです。コンポーネント分割、状態管理戦略、データフロー設計、レンダリング最適化の4つの観点から、要件に最適なアーキテクチャ設計案を提案します。

このスキルは GitHub Copilot の Agent Skills（`.github/skills/` に配置する SKILL.md）として動作し、`@frontend-design` で呼び出せます。

## 特徴

| 項目 | 内容 |
|------|------|
| **提供元** | Anthropic（公式） |
| **動作環境** | GitHub Copilot（VS Code チャット / エージェントモード） |
| **呼び出し方** | `@frontend-design` |
| **スキル種別** | アーキテクチャ設計支援 |
| **設計観点** | コンポーネント分割 / 状態管理 / データフロー / レンダリング最適化 |

## 詳細説明

### 4つの設計観点

frontend-design は以下の4観点から総合的に設計を支援します：

| 観点 | 説明 | 出力例 |
|------|------|--------|
| **コンポーネント分割** | 関心の分離に基づいた適切なコンポーネント構成 | Container/Presentational パターン、責務の明確化 |
| **状態管理戦略** | プロジェクト規模に適した状態管理の選定と設計 | Zustand + React Query、Store 設計、アクション定義 |
| **データフロー設計** | 単方向データフローを基本としたデータの流れの設計 | ユーザー入力 → Container → Custom Hook → API → Store → 再レンダリング |
| **レンダリング最適化** | パフォーマンスを考慮したレンダリング戦略 | React.memo、仮想スクロール、入力デバウンス |

### 入力パラメータ

| パラメータ | 型 | 必須 | 説明 |
|-----------|------|------|------|
| `requirements` | string | ✅ | 機能要件の説明 |
| `tech_stack` | string | ✅ | 技術スタック（React, Vue, TypeScript 等） |
| `current_architecture` | string | ❌ | 現在のアーキテクチャ説明 |
| `constraints` | string[] | ❌ | 制約条件（パフォーマンス目標、バンドルサイズ等） |
| `design_focus` | string | ❌ | 設計フォーカス（components / state / data-flow / rendering / all） |
| `include_diagram` | boolean | ❌ | コンポーネント図を含めるか（デフォルト: false） |

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

## 使い方

> **注意**: frontend-design は Anthropic 公式提供のスキルです。Skill Creator で生成する必要はなく、GitHub Copilot にプリインストールされています。

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
