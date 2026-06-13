# 6-4: 実プロジェクトでのスキル連携

> **学習時間**: 20分 | **難易度**: ⭐⭐⭐

## 概要

このセクションでは、baoyu-skills の複数スキルを連携させた**自動化パイプライン**を構築する方法を学びます。Part 5 で学んだスキル連携の概念を、実際のコンテンツ生成ワークフローに適用します。

## パイプラインの設計

### 全体アーキテクチャ

baoyu-skills を使ったコンテンツ生成パイプラインは以下のように設計できます：

```
                    ┌─────────────────┐
                    │  記事の作成      │
                    │  (Markdown)     │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
      ┌────────────┐ ┌────────────┐ ┌────────────┐
      │ カバー画像  │ │  図解生成   │ │ インフォ    │
      │ cover-image│ │ diagram    │ │ graphic    │
      └────────────┘ └────────────┘ └────────────┘
              │              │              │
              └──────────────┼──────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  スライド生成    │
                    │  slide-deck     │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  多言語化・公開   │
                    │  translate      │
                    │  markdown-to-html│
                    └─────────────────┘
```

## 実装例: ブログ記事生成パイプライン

### ステップ1: エージェントへの指示としてパイプラインを定義

baoyu-skills のパイプラインは、シェルスクリプトではなく**エージェントへの自然言語指示**として定義するのが実践的です。以下のような指示をエージェントに与えることで、パイプラインが実行されます：

```markdown
以下のパイプラインを実行してください：

1. articles/my-article.md から baoyu-cover-image でカバー画像を生成
   - type: conceptual, palette: cool, rendering: digital
   - 出力先: output/images/cover.png

2. 同じ記事から baoyu-diagram で図解を生成
   - type: structural
   - 出力先: output/images/diagram.svg

3. baoyu-infographic でインフォグラフィックを生成
   - layout: auto-recommend, style: technical-schematic
   - 出力先: output/images/infographic.png

4. baoyu-slide-deck でスライドを生成
   - style: blueprint, audience: intermediate
   - 出力先: output/slides/

5. baoyu-translate で英語版に翻訳
   - 出力先: output/translations/
```

### ステップ2: スクリプトベースのパイプライン（Bun）

より自動化したい場合は、baoyu-skills のスクリプトを直接呼び出す Bun スクリプトを作成します：

```typescript
// blog-pipeline.ts
import { $ } from "bun";

const article = process.argv[2];
const outputDir = "./output";

await $`mkdir -p ${outputDir}/images ${outputDir}/slides`;

console.log("=== Step 1: カバー画像生成 ===");
await $`bun run skills/baoyu-cover-image/scripts/main.ts ${article} \
  --type conceptual --palette cool \
  --out ${outputDir}/images/cover.png`;

console.log("=== Step 2: 図解生成 ===");
await $`bun run skills/baoyu-diagram/scripts/main.ts ${article} \
  --type structural \
  --out ${outputDir}/images/diagram.svg`;

console.log("=== Step 3: インフォグラフィック生成 ===");
await $`bun run skills/baoyu-infographic/scripts/main.ts ${article} \
  --style technical-schematic \
  --out ${outputDir}/images/infographic.png`;

console.log("=== Pipeline Complete ===");
```

### ステップ2: Claude Code のスキルとして定義

このパイプライン自体を1つのスキルとして定義することもできます：

```yaml
# SKILL.md
---
name: blog-pipeline
description: ブログ記事からカバー画像、図解、スライドを一括生成
author: Your Name
tags: [pipeline, content, blog]
---

## 使用方法

```bash
/blog-pipeline path/to/article.md
```

## 処理フロー

1. baoyu-cover-image でカバー画像を生成
2. baoyu-diagram で図解を生成
3. baoyu-infographic でインフォグラフィックを生成
4. baoyu-slide-deck でスライドを生成
5. 全ての出力を `output/` ディレクトリに保存
```

## 応用パターン

### パターン1: CI/CD パイプラインへの統合

GitHub Actions で記事公開時に自動生成する例：

```yaml
# .github/workflows/generate-content.yml
name: Generate Content Assets

on:
  push:
    paths:
      - 'articles/**/*.md'

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Bun
        uses: oven-sh/setup-bun@v1
      
      - name: Install baoyu-skills
        run: npx skills add jimliu/baoyu-skills
      
      - name: Generate cover images
        run: |
          for article in articles/*.md; do
            /baoyu-cover-image "$article" --quick
          done
      
      - name: Commit generated assets
        run: |
          git add images/
          git commit -m "Auto-generate content assets" || true
          git push
```

### パターン2: バッチ処理

複数の記事を一括処理する例：

```bash
#!/bin/bash
# batch-generate.sh

for article in articles/*.md; do
  name=$(basename "$article" .md)
  echo "Processing: $name"
  
  /baoyu-cover-image "$article" \
    --quick \
    --out "images/$name-cover.png"
  
  /baoyu-diagram "$article" \
    --type auto \
    --out "images/$name-diagram.svg"
done
```

### パターン3: スキル間のデータ連携

あるスキルの出力を別のスキルの入力として利用する例：

```bash
# 1. 図を生成
/baoyu-diagram "システムアーキテクチャ" \
  --type structural \
  --out images/architecture.svg

# 2. 図の説明文を生成
# （diagram の出力を infographic の入力に使う）
echo "# システムアーキテクチャの説明

## 主要コンポーネント
- Webサーバー: Nginx
- アプリケーション: Node.js
- データベース: PostgreSQL

## データフロー
1. クライアントからのリクエスト
2. Nginxがロードバランシング
3. Node.jsがビジネスロジックを処理
4. PostgreSQLにデータを保存" > /tmp/arch-desc.md

# 3. 説明からインフォグラフィックを生成
/baoyu-infographic /tmp/arch-desc.md \
  --layout layers-stack \
  --style technical-schematic
```

## パイプライン設計のベストプラクティス

### 1. エラーハンドリング

各ステップが失敗した場合のフォールバックを設計します：

```bash
# エラーハンドリング付きパイプライン
if /baoyu-cover-image article.md --quick; then
  echo "カバー画像生成成功"
else
  echo "カバー画像生成失敗、デフォルト画像を使用"
  cp templates/default-cover.png images/cover.png
fi
```

### 2. キャッシュ戦略

同じ入力に対する再生成を避けるため、キャッシュを活用します：

```bash
# キャッシュチェック
CACHE_FILE=".cache/$(md5sum article.md | cut -d' ' -f1)"
if [ -f "$CACHE_FILE" ]; then
  echo "キャッシュから復元"
  cp "$CACHE_FILE" images/cover.png
else
  /baoyu-cover-image article.md --quick
  cp images/cover.png "$CACHE_FILE"
fi
```

### 3. 並列実行

独立したステップは並列実行して高速化します：

```bash
# 並列実行（カバー画像と図解は独立）
/baoyu-cover-image article.md --quick &
/baoyu-diagram article.md --type auto &
wait  # 両方の完了を待つ

# スライド生成は上記の結果に依存
/baoyu-slide-deck article.md
```

## 次のステップ

→ [6-5: カスタムスキル開発（baoyu流）](05-custom-skill-development.md)
