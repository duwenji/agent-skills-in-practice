# 3-3b: ui-ux-pro-max — UI/UX最適化スキル（コミュニティ）

> **学習時間**: 15分 | **難易度**: ⭐⭐

## 概要

**ui-ux-pro-max** は、コミュニティ（nextlevelbuilder）が開発したUI/UX最適化スキルです。UIコンポーネントやページをアクセシビリティ（WCAG 2.1）、レスポンシブデザイン、ユーザビリティ、ビジュアルデザインの4観点で監査し、改善提案を行います。

このスキルは GitHub Copilot の Agent Skills として動作し、`@ui-ux-pro-max` で呼び出せます。

## 特徴

| 項目 | 内容 |
|------|------|
| **提供元** | nextlevelbuilder（コミュニティ） |
| **動作環境** | GitHub Copilot（VS Code チャット / エージェントモード） |
| **呼び出し方** | `@ui-ux-pro-max` |
| **スキル種別** | UI/UX 監査・改善提案 |
| **監査観点** | アクセシビリティ / レスポンシブデザイン / ユーザビリティ / ビジュアルデザイン |

## 詳細説明

### 4つの監査観点

ui-ux-pro-max は以下の4観点からUI/UXを総合的に監査します：

| 観点 | 説明 | チェック内容 |
|------|------|-------------|
| **アクセシビリティ** | WCAG 2.1 に基づくアクセシビリティ監査 | alt属性、コントラスト比、キーボード操作、aria属性 |
| **レスポンシブデザイン** | 複数ビューポートでの表示品質確認 | レイアウト崩れ、ナビゲーション、タッチターゲットサイズ |
| **ユーザビリティ** | ユーザー体験の観点からの評価 | フィードバック不足、エラーハンドリング、直感性 |
| **ビジュアルデザイン** | 視覚的な品質と一貫性のチェック | タイポグラフィ、カラースキーム、スペーシング、一貫性 |

### 入力パラメータ

| パラメータ | 型 | 必須 | 説明 |
|-----------|------|------|------|
| `component_code` | string | ✅ | 監査対象のUIコンポーネントコード |
| `framework` | string | ✅ | 使用フレームワーク（React, Vue, Angular 等） |
| `audit_focus` | string[] | ❌ | 監査フォーカス（accessibility / responsive / usability / visual / all） |
| `wcag_level` | string | ❌ | WCAG準拠レベル（A / AA / AAA、デフォルト: AA） |
| `viewport_sizes` | string[] | ❌ | テストするビューポートサイズ一覧 |
| `include_remediation` | boolean | ❌ | 修正コード例を含めるか（デフォルト: true） |

### 出力スキーマ

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
