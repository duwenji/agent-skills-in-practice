# 電子書籍出力ディレクトリ

このディレクトリには、チュートリアルを電子書籍形式に変換した出力ファイルを格納します。

## 出力形式（予定）

| 形式 | ファイル名 | 用途 |
|------|-----------|------|
| PDF | github-copilot-skill-creator-tutorial.pdf | KDP出版、配布用 |
| EPUB | github-copilot-skill-creator-tutorial.epub | 電子書籍リーダー |
| MOBI | github-copilot-skill-creator-tutorial.mobi | Kindle |
| HTML | index.html | Web公開用 |

## 変換手順（予定）

```bash
# Markdown → PDF（Pandoc 使用）
pandoc docs/**/*.md -o ebook-output/tutorial.pdf \
  --from markdown \
  --to pdf \
  --toc \
  --highlight-style=tango

# Markdown → EPUB
pandoc docs/**/*.md -o ebook-output/tutorial.epub \
  --from markdown \
  --to epub \
  --toc \
  --metadata title="GitHub Copilot Skill Creator チュートリアル"
```

## 注意事項

- 電子書籍化は全コンテンツ完成後に行います
- 表紙画像は `assets/cover-output/` のデータを使用
- 図表は `assets/diagrams/` のデータを埋め込み
