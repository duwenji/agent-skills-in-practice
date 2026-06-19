---
name: markdown-to-office
description: "Markdown ファイルを Word (.docx) または PDF に変換する。社内作成の Markdown 文書を外部提出用 Office 形式に変換する場合に使用する。テンプレートの有無と出力形式をユーザーに確認してから変換する。"
---

# Markdown → Office 変換

Pandoc を使って Markdown ファイルを Word (.docx) または PDF に変換します。

## 前提条件確認

```bash
pandoc --version
```

インストールされていない場合は実行前にユーザーに確認し、承認を得てからインストールする：

```bash
# Windows
winget install JohnMacFarlane.Pandoc

# macOS
brew install pandoc

# Linux (Debian/Ubuntu)
sudo apt-get install pandoc
```

PDF 出力が必要な場合は PDF エンジンも確認する：

```bash
# weasyprint（推奨: インストールが簡単）
pip install weasyprint

# または wkhtmltopdf（高品質だが環境構築が複雑）
```

## 手順

### 1. 入力と出力形式の確認

ユーザーから受け取った情報を確認する：

- 入力 Markdown ファイルのパス
- 出力形式（`docx` または `pdf`）
- スタイルテンプレート（社内テンプレート `.docx` の指定があれば使用）
- 出力先ディレクトリ（指定がなければ入力ファイルと同じ場所）

### 2. Markdown の事前チェック

<DECISION-GATE>
変換前に入力 Markdown を確認し、Pandoc が正しく処理できない可能性のある要素をユーザーに報告する。
確認を取らずに変換を開始してはならない。
</DECISION-GATE>

以下の要素が含まれる場合は変換結果への影響をユーザーに事前に伝える：

| Markdown の要素 | Word/PDF での変換結果 |
|----------------|---------------------|
| コードブロック (` ``` `) | 等幅フォントのテキストブロックになる（テンプレート依存） |
| Mermaid / DOT 図 | **変換されない**。画像に変換済みの場合のみ埋め込み可能 |
| 画像参照 `![](path)` | 参照先ファイルが存在する場合のみ埋め込まれる |
| 数式 (`$...$`) | LaTeX 環境がない場合はプレーンテキストになる |
| 日本語テキスト | フォント設定によっては文字化けの可能性あり（テンプレートで対応） |

### 3. テンプレートの確認

社内テンプレート（`.docx`）が指定されていない場合、以下を提案する：

```bash
# Pandoc のデフォルトテンプレートを取得して社内スタイルに編集
pandoc --print-default-data-file reference.docx > company-template.docx
# → company-template.docx を Word で開いてフォント・スタイル・ヘッダー/フッターを編集後、
#   次回から --reference-doc=company-template.docx として使用する
```

テンプレートなしで変換すると Pandoc のデフォルトスタイルが適用されることをユーザーに伝える。

### 4. 変換実行

**Word (.docx) の場合：**

```bash
# テンプレートなし
pandoc <入力.md> -o <出力.docx>

# 社内テンプレートあり（推奨）
pandoc <入力.md> --reference-doc=<テンプレート.docx> -o <出力.docx>

# 例: 品質改善施策検討書を Word に変換
pandoc "品質改善 施策検討.md" --reference-doc=company-template.docx -o "品質改善 施策検討_提出用.docx"
```

**PDF の場合：**

```bash
# weasyprint を使用
pandoc <入力.md> -o <出力.pdf> --pdf-engine=weasyprint

# wkhtmltopdf を使用（より高品質）
pandoc <入力.md> -o <出力.pdf> --pdf-engine=wkhtmltopdf

# 例: PDF に変換
pandoc "品質改善 施策検討.md" -o "品質改善 施策検討_提出用.pdf" --pdf-engine=weasyprint
```

### 5. 変換後のレビューチェックリスト

変換が完了したら以下を確認してユーザーに報告する：

- [ ] 見出しのスタイルが正しく適用されているか（見出し1/2/3）
- [ ] 表が正しく描画されているか（列の幅・罫線）
- [ ] 箇条書き・番号付きリストが崩れていないか
- [ ] コードブロックが可読な形式で出力されているか
- [ ] 画像が正しく埋め込まれているか
- [ ] 日本語テキストが文字化けしていないか
- [ ] ページ番号・ヘッダー/フッターが要件通りか（テンプレート依存）

## 出力

変換完了後に以下を報告する：

1. 出力ファイルのパス
2. 使用したテンプレート（なしの場合はその旨を明記）
3. チェックリストの結果（体裁上の問題があれば具体的に指摘）
4. 事前チェックで警告した要素の変換結果

提出先の要件（フォント・余白・ページ設定・ファイルサイズ制限等）がある場合は、テンプレートの調整またはエクスポート設定の変更が必要なことをユーザーに伝える。

## エラー時の対応

| エラー | 対応 |
|--------|------|
| ファイルが見つからない | パスを確認してユーザーに再入力を求める |
| Pandoc 未インストール | インストール手順を OS ごとに提示し、ユーザーの確認を得てから実行する |
| PDF エンジン未インストール | `pip install weasyprint` を提案する。それも難しければ docx への変換を代替として提案する |
| 画像参照が壊れている | 参照先ファイルのパスを確認し、ユーザーに修正を求める |
| 日本語文字化け | テンプレートのフォント設定（游ゴシック・Noto Sans CJK 等）を確認するよう伝える |
| 出力ファイルが開けない | Word のバージョン互換性を確認し、必要に応じて `.doc` 形式での再変換を提案する |
