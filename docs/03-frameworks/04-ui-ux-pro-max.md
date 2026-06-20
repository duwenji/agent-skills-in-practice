# 3-4: ui-ux-pro-max — UI/UX最適化スキル（コミュニティ）

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


→ [3-6: 問題 × スキル解決マッピング](06-problem-skill-mapping.md) で、全スキルの関係性を整理する
→ [Part 4: 実践スキル実装編](../04-skills-in-practice/05-ui-ux-pro-max.md) で、実際にスキルを作成して動かす
