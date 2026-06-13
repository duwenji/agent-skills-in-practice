# 4-5: ui-ux-pro-max — UI/UX最適化スキル

> **学習時間**: 25分 | **難易度**: ⭐⭐⭐ | **カテゴリ**: デザイン改善

## 概要

**ui-ux-pro-max** は、UIコンポーネントやページをアクセシビリティ（WCAG 2.1）、レスポンシブデザイン、ユーザビリティ、ビジュアルデザインの4観点で監査し、改善提案を行うスキルです。フロントエンドの品質をユーザー体験の観点から総合的に向上させます。

## 学習目標

- Skill Creator を使ってUI/UX監査スキルを生成できる
- WCAG 2.1 の主要な達成基準を理解する
- レスポンシブデザインの問題を特定できる

## 利用シーン

| シーン | 説明 |
|-------|------|
| リリース前のUI品質監査 | 本番リリース前にUIの品質を総合チェック |
| アクセシビリティ対応 | WCAG 2.1 AA 準拠のための網羅的チェック |
| レスポンシブデザイン確認 | 複数ビューポートでの表示品質を確認 |
| デザインシステムの一貫性チェック | コンポーネント間のデザインの一貫性を確認 |

## SKILL.md 完全定義

`samples/ui-ux-pro-max/SKILL.md` に完全な定義があります。

### 入力パラメータ

| パラメータ | 型 | 必須 | デフォルト | 説明 |
|-----------|------|------|-----------|------|
| `component_code` | string | ✅ | — | 監査対象のUIコンポーネントコード |
| `framework` | string | ✅ | — | 使用フレームワーク |
| `audit_focus` | string[] | ❌ | 全4観点 | 監査フォーカス |
| `wcag_level` | string | ❌ | "AA" | WCAG準拠レベル |
| `viewport_sizes` | string[] | ❌ | — | テストするビューポートサイズ |
| `include_remediation` | boolean | ❌ | true | 修正コード例を含めるか |

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
    "usability": { "score": 75, "issues": [] },
    "visual": { "score": 80, "issues": [] }
  },
  "quick_wins": [
    "A11Y-1: alt属性の追加（5分）",
    "RSP-1: ハンバーガーメニュー化（30分）"
  ]
}
```

## 実践ハンズオン

### ステップ1: Skill Creator でスキルを生成

```
@copilot ui-ux-pro-max スキルを作成して。
UIコンポーネントをアクセシビリティ（WCAG 2.1 AA）、
レスポンシブデザイン、ユーザビリティ、ビジュアルデザインの
4観点で監査し、改善提案を行うスキル。
```

### ステップ2: テスト実行

以下のコードでテスト：

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

### 期待される結果

- **アクセシビリティ**: `<img>` に alt 属性がない（WCAG 1.1.1 違反）、ナビゲーションに `aria-label` がない
- **レスポンシブ**: 固定値のスタイル、ハンバーガーメニューの欠如
- **ユーザビリティ**: `alert()` の使用はモーダルに置き換え推奨
- **ビジュアル**: コントラスト比は良好

## WCAGレベルの変更

プロジェクトの要件に応じて監査レベルを変更できます：

```
# AAAレベルで厳格チェック
@ui-ux-pro-max wcag_level=AAA
[コード]

# Aレベルで最低限チェック
@ui-ux-pro-max wcag_level=A
[コード]
```

## テストケース

| # | テスト内容 | 期待結果 |
|---|-----------|---------|
| 1 | 空のコード | エラーメッセージを返す |
| 2 | アクセシビリティ問題を含むコード | alt属性欠如やコントラスト比の問題を指摘 |
| 3 | audit_focus=["responsive"] のみ | レスポンシブ関連のみの結果 |
| 4 | wcag_level=AAA を指定 | AAAレベルでの厳格なチェック結果 |
| 5 | アクセシビリティ完璧なコード | アクセシビリティスコア100 |

## 次のステップ

- [Part 5-1: パイプライン連携](../06-advanced/01-pipeline-integration.md) で全スキルの連携パイプラインを構築
- [Part 5-3: 評価サイクル](../06-advanced/03-evaluation-cycle.md) でスキル自体の品質評価
