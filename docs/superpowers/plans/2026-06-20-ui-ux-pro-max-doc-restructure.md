# ui-ux-pro-max ドキュメント再構成 実装計画

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** `docs/03-frameworks/03-3b-ui-ux-pro-max.md` を物語構造（3シーン共感フック → 説明 → Before/After → リファレンス）に再構成し、「Copilot を使っているが生成 UI が粗削り」な読者が冒頭で即座に価値を感じられるようにする。

**Architecture:** 既存ファイルを完全に書き直す。情報はゼロ削除で、冒頭に3シーン共感フックを追加、`## 詳細説明` を3つの独立 `##` セクションに分割昇格、`## 同じコンポーネントで何が変わるのか` を独立セクションとして新規追加する。

**Tech Stack:** Markdown のみ。コード変更なし。

## Global Constraints

- 対象ファイル: `docs/03-frameworks/03-3b-ui-ux-pro-max.md` のみ
- 情報ゼロ削除: 入力パラメータ全行・出力スキーマ JSON・出力スキーマ説明文・4観点テーブル・特徴テーブル・呼び出し例（Header コード）・監査レベル変更例・フォーカス絞り込み例・次のステップリンクは全て保持
- `## 同じコンポーネントで何が変わるのか` は独立した `##` セクションとして配置（他セクション内に入れ子にしない）

---

### Task 1: 03-3b-ui-ux-pro-max.md を新構成で書き直す

**Files:**
- Modify: `docs/03-frameworks/03-3b-ui-ux-pro-max.md`

**Interfaces:**
- Consumes: 設計仕様 `docs/superpowers/specs/2026-06-20-ui-ux-pro-max-doc-restructure-design.md`
- Produces: 再構成済みの `docs/03-frameworks/03-3b-ui-ux-pro-max.md`

- [ ] **Step 1: 現行ファイルを読んで内容を把握する**

```bash
cat docs/03-frameworks/03-3b-ui-ux-pro-max.md
```

現行ファイルの構成を確認し、保持必須コンテンツを頭に入れる。

- [ ] **Step 2: 以下の完全な新ファイル内容でファイルを書き直す**

`docs/03-frameworks/03-3b-ui-ux-pro-max.md` の全内容を以下に置き換える。コードブロック内のバッククォートや絵文字はそのまま使用すること。

---

```markdown
# 3-3b: ui-ux-pro-max — UI/UX最適化スキル（コミュニティ）

> **学習時間**: 15分 | **難易度**: ⭐⭐

## AIが生成したUIに、見えない問題が潜んでいる

Copilot がロゴを実装した。

```
<img src="/logo.png" />
```

動く。表示される。でも alt 属性がない。
スクリーンリーダーは「image」と読み上げるだけだ。

---

デスクトップでは完璧に見える。
375px のスマートフォンで確認したら、
ナビゲーションが画面の右側に切れていた。

---

背景 #333 に白文字。おしゃれで読みやすい——
少なくとも自分には。
コントラスト比は 3.5:1。WCAG AA の基準は 4.5:1 だった。

---

Copilot はコードを書く。でも、誰かがこれを使えるか、は教えてくれない。

## ui-ux-pro-max とは

コミュニティ（nextlevelbuilder）が開発した UI/UX 監査スキルです。アクセシビリティ・レスポンシブデザイン・ユーザビリティ・ビジュアルデザインの4観点でコンポーネントを診断し、重大度付きの改善提案を返します。

| 項目 | 内容 |
|------|------|
| **提供元** | nextlevelbuilder（コミュニティ） |
| **動作環境** | GitHub Copilot（VS Code チャット / エージェントモード） |
| **呼び出し方** | `@ui-ux-pro-max` |
| **スキル種別** | UI/UX 監査・改善提案 |
| **監査観点** | アクセシビリティ / レスポンシブデザイン / ユーザビリティ / ビジュアルデザイン |

## 同じコンポーネントで何が変わるのか

**Before — @ui-ux-pro-max なし**

```
あなた: Header コンポーネントを実装して。

Copilot: わかりました。

function Header() {
  return (
    <header style={{background: '#333', color: 'white'}}>
      <img src="/logo.png" />
      <nav>
        <a href="/">Home</a>
        <a href="/about">About</a>
      </nav>
    </header>
  );
}
```

**After — @ui-ux-pro-max あり**

```
あなた: @ui-ux-pro-max
フレームワーク: React
[上記 Header コード]

Copilot: 監査結果（スコア: 65/100）

🔴 Critical × 2
  A11Y-1: <img> に alt 属性がない（WCAG 1.1.1）
  A11Y-2: コントラスト比 3.5:1（基準: 4.5:1）

🟡 Major × 1
  RSP-1: ナビが 375px でオーバーフロー

Quick Wins:
  alt="会社ロゴ" を追加（5分）
  ハンバーガーメニュー化（30分）
```

## 4つの監査観点

必要なときに参照してください。最初から全部覚える必要はありません。

| 観点 | 説明 | チェック内容 |
|------|------|-------------|
| **アクセシビリティ** | WCAG 2.1 に基づくアクセシビリティ監査 | alt属性、コントラスト比、キーボード操作、aria属性 |
| **レスポンシブデザイン** | 複数ビューポートでの表示品質確認 | レイアウト崩れ、ナビゲーション、タッチターゲットサイズ |
| **ユーザビリティ** | ユーザー体験の観点からの評価 | フィードバック不足、エラーハンドリング、直感性 |
| **ビジュアルデザイン** | 視覚的な品質と一貫性のチェック | タイポグラフィ、カラースキーム、スペーシング、一貫性 |

## 入力パラメータ

| パラメータ | 型 | 必須 | 説明 |
|-----------|------|------|------|
| `component_code` | string | ✅ | 監査対象のUIコンポーネントコード |
| `framework` | string | ✅ | 使用フレームワーク（React, Vue, Angular 等） |
| `audit_focus` | string[] | ❌ | 監査フォーカス（accessibility / responsive / usability / visual / all） |
| `wcag_level` | string | ❌ | WCAG準拠レベル（A / AA / AAA、デフォルト: AA） |
| `viewport_sizes` | string[] | ❌ | テストするビューポートサイズ一覧 |
| `include_remediation` | boolean | ❌ | 修正コード例を含めるか（デフォルト: true） |

## 出力スキーマ

```json
{
  "summary": {
    "total_issues": 8,
    "critical": 2,
    "major": 3,
    "minor": 3,
    "overall_ux_score": 65
  },
  "categories": {
    "accessibility": {
      "score": 45,
      "wcag_compliance": "AA",
      "issues": [
        {
          "id": "A11Y-1",
          "wcag_criteria": "1.1.1",
          "severity": "critical",
          "element": "<img>",
          "message": "画像にalt属性がありません",
          "remediation": "<img alt=\"商品の説明文\" src=\"...\">"
        }
      ]
    },
    "responsive": {
      "score": 70,
      "issues": [
        {
          "id": "RSP-1",
          "severity": "major",
          "viewport": "375px",
          "message": "ナビゲーションメニューが画面からはみ出している",
          "remediation": "ハンバーガーメニューの導入を推奨"
        }
      ]
    },
    "usability": {
      "score": 75,
      "issues": []
    },
    "visual": {
      "score": 80,
      "issues": []
    }
  },
  "quick_wins": [
    "A11Y-1: alt属性の追加（5分）",
    "RSP-1: ハンバーガーメニュー化（30分）"
  ]
}
```

出力は各観点のスコア（0-100）と、発見された問題の一覧で構成されます。各問題には **severity（critical / major / minor）** と **remediation（修正例）** が含まれ、優先順位をつけて改善を進められます。

## 使い方

### 1. 呼び出し方

VS Code の Copilot チャット（エージェントモード）で以下のように入力するだけで利用できます：


```
@ui-ux-pro-max 
フレームワーク: React

function Header() {
  return (
    <header style={{background: '#333', color: 'white'}}>
      <img src="/logo.png" />
      <nav>
        <a href="/">Home</a>
        <a href="/about">About</a>
        <a href="/contact">Contact</a>
      </nav>
      <button onClick={() => alert('menu')}>☰</button>
    </header>
  );
}
```

### 2. 監査レベルの変更


プロジェクトの要件に応じて監査レベルを変更できます：

```
# AAAレベルで厳格チェック
@ui-ux-pro-max wcag_level=AAA
[コード]

# レスポンシブだけチェック
@ui-ux-pro-max audit_focus=["responsive"]
[コード]
```

## 次のステップ


→ [3-4: 問題 × スキル解決マッピング](04-problem-skill-mapping.md) で、全スキルの関係性を整理する
→ [Part 4: 実践スキル実装編](../04-skills-in-practice/05-ui-ux-pro-max.md) で、実際にスキルを作成して動かす
```

---

- [ ] **Step 3: 保持必須コンテンツの存在を確認する（10項目）**

以下を1つずつ確認する：

1. `@ui-ux-pro-max` 呼び出し例コードブロック（`## 使い方` 内に Header コンポーネント含む）が存在する
2. 特徴テーブル（提供元・動作環境・呼び出し方・スキル種別・監査観点 の5行）が存在する
3. `## 4つの監査観点` テーブル（観点・説明・チェック内容 の3列、4行）が存在する
4. `## 入力パラメータ` テーブル（6パラメータ全行: component_code, framework, audit_focus, wcag_level, viewport_sizes, include_remediation）が存在する
5. `## 出力スキーマ` JSON（summary / categories / quick_wins）が存在する
6. 出力スキーマ直後の説明文（「出力は各観点のスコア（0-100）と…」）が存在する
7. `wcag_level=AAA` の監査レベル変更例が存在する
8. `audit_focus=["responsive"]` のフォーカス絞り込み例が存在する
9. 次のステップリンク `04-problem-skill-mapping.md` が存在する
10. 次のステップリンク `../04-skills-in-practice/05-ui-ux-pro-max.md` が存在する

- [ ] **Step 4: 追加・変更コンテンツの存在を確認する（8項目）**

1. `## AIが生成したUIに、見えない問題が潜んでいる` セクションが冒頭付近に存在する
2. シーン1（`<img src="/logo.png" />` の alt 属性なし）が存在する
3. シーン2（375px でナビが切れる）が存在する
4. シーン3（コントラスト比 3.5:1、WCAG AA 基準 4.5:1）が存在する
5. 締めの一文「Copilot はコードを書く。でも、誰かがこれを使えるか、は教えてくれない。」が存在する
6. `## 同じコンポーネントで何が変わるのか` が独立した `##` セクションとして存在する（他セクション内に入れ子ではない）
7. Before/After チャット出力比較（「Before — @ui-ux-pro-max なし」と「After — @ui-ux-pro-max あり」）が存在する
8. 「必要なときに参照してください。最初から全部覚える必要はありません。」が `## 4つの監査観点` 直下に存在する

- [ ] **Step 5: 削除必須コンテンツの不在を確認する（2項目）**

1. `## 詳細説明` セクションが存在しない
2. `## 概要` セクションが存在しない

- [ ] **Step 6: コミットする**

```bash
git add docs/03-frameworks/03-3b-ui-ux-pro-max.md
git commit -m "docs: 03-3b-ui-ux-pro-max.md を物語構造に再構成"
```

---

### Task 2: 実装計画ファイル自体をコミットする

**Files:**
- Commit: `docs/superpowers/plans/2026-06-20-ui-ux-pro-max-doc-restructure.md`

- [ ] **Step 1: 計画ファイルをコミットする**

```bash
git add docs/superpowers/plans/2026-06-20-ui-ux-pro-max-doc-restructure.md
git commit -m "docs: 03-3b-ui-ux-pro-max.md リストラクチャリングの実装計画を追加"
```
