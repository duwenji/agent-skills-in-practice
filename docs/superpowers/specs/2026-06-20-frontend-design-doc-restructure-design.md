# frontend-design ドキュメント再構成 設計仕様

**日付**: 2026-06-20  
**対象ファイル**: `docs/03-frameworks/03-3a-frontend-design.md`  
**目的**: 冒頭の価値訴求を強化し、読者が「これは私の問題の解決策だ」と感じる物語構造に再構成する

---

## 読者プロフィール

- Copilot を使い始めているが、生成コードが散らかりがち
- React の基礎はある
- AI ツールの使い方を洗練させたい中級者

## フックスタイル

Before/After 直球型：Copilot 単体 vs `@frontend-design` の対比で始める

---

## 新しい構成

### ① Copilot だけで頼むと（Before）— 冒頭フック前半

チャット形式で「設計なしで頼んだ場合」を示す。

**具体的なシーン:**
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

締めの一文:「動く。でも誰も触りたくないコードが完成した。」

### ② @frontend-design を加えると（After）— 冒頭フック後半

同じ依頼を `@frontend-design` 付きで行った結果を並べて示す。

**具体的なシーン:**
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

締めの一文:「コードの前に設計図が出てくる。」

### ③ frontend-design とは（`## frontend-design とは`）

Anthropic 公式提供のフロントエンド設計支援スキルの説明。

**含める内容:**
- 4観点の概要（コンポーネント分割・状態管理・データフロー・レンダリング最適化）
- 特徴テーブル（提供元・動作環境・呼び出し方・スキル種別）
- Copilot プリインストール済みの注意書き（「Skill Creator で作成する必要はありません」）

### ④ 同じ依頼で何が変わるのか（`## 同じ依頼で何が変わるのか`）

Before/After を観点ごとに比較する表（独立した `##` セクション）。

| 観点 | Copilot 単体 | @frontend-design あり |
|------|-------------|----------------------|
| コンポーネント | 1ファイルに全機能 | Container/Presentational に分割 |
| 状態管理 | useState を羅列 | Zustand + React Query に最適化 |
| データフロー | 暗黙的・双方向 | 単方向フローを明示 |
| 最初の出力 | コード | 設計図 |
| 保守性 | 触るのが怖い | 誰でも変更できる |

### ⑤ 4つの設計観点（`## 4つの設計観点`）

現行の詳細説明テーブルを独立した `##` セクションとして昇格。

冒頭に一文追加:「必要なときに参照してください。最初から全部覚える必要はありません。」

### ⑥ 入力パラメータ（`## 入力パラメータ`）

現行の `### 入力パラメータ` テーブルを `##` に昇格して維持。

### ⑦ 出力スキーマ（`## 出力スキーマ`）

現行の `### 出力スキーマ` JSON を `##` に昇格して維持。

### ⑧ 使い方（`## 使い方`）

現行の `## 使い方` を維持。Copilot プリインストール注意書きは③へ移動済みのため、その `> 注意:` ブロックは削除。呼び出し方と `design_focus` 絞り込み例はそのまま維持。

### ⑨ 次のステップ（`## 次のステップ`）

現行のリンクをそのまま維持。

---

## 保持必須コンテンツ（ゼロ削除）

- `@frontend-design` 呼び出し例コードブロック
- 特徴テーブル（提供元・動作環境・呼び出し方・スキル種別・設計観点）
- 4観点テーブル（観点・説明・出力例 の3列）
- 入力パラメータテーブル（6パラメータ全行）
- 出力スキーマ JSON（architecture_overview / component_tree / state_management / data_flow / optimization_recommendations）
- `design_focus` 絞り込み例（state / components）
- 次のステップリンク（03-3b-ui-ux-pro-max.md, 04-problem-skill-mapping.md）

## 削除するコンテンツ

- `> **注意**: frontend-design は Anthropic 公式提供のスキルです。Skill Creator で生成する必要はなく…` ブロック（③に統合するため）

## 追加するコンテンツ

- ① Copilot 単体 Before シーン
- ② @frontend-design After シーン
- ④ Before/After 比較表

## セクション構造変更

- `## 詳細説明` 廃止 → `## 4つの設計観点`、`## 入力パラメータ`、`## 出力スキーマ` の3セクションに分割・昇格
- `### 入力パラメータ` → `##` に昇格
- `### 出力スキーマ` → `##` に昇格
