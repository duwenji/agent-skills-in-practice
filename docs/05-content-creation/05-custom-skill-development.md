# 6-5: カスタムスキル開発（baoyu流）

> **学習時間**: 20分 | **難易度**: ⭐⭐⭐

## 概要

このセクションでは、baoyu-skills の設計パターンを参考に、**自前のコンテンツ生成スキル**を開発する方法を学びます。baoyu-skills から学んだ「自己完結型スキル」「スタイル体系」「バックエンド抽象化」などの設計原則を、自分のスキル開発に応用します。

## baoyu流スキル設計の7原則

baoyu-skills の設計から抽出した7つの原則を、カスタムスキル開発に適用します：

| # | 原則 | 説明 |
|---|------|------|
| 1 | **自己完結性** | スキルは単体で動作し、外部参照をしない |
| 2 | **インライン化** | User Input Tools / Image Generation Tools は SKILL.md に直接記述 |
| 3 | **スタイル体系** | 出力のバリエーションを次元分解して定義する |
| 4 | **バックエンド抽象化** | 実行ロジックをバックエンドに委譲する |
| 5 | **EXTEND.md 設定** | ユーザー設定を外部ファイルで管理する |
| 6 | **プロンプト管理** | 生成プロンプトを保存・再利用可能にする |
| 7 | **クロスプラットフォーム** | 複数のAIエージェントで動作するようにする |

## ステップ1: スキルの設計

### スキルの目的を定義する

まず、スキルの目的を明確にします：

```markdown
# スキル設計シート

## スキル名
baoyu-banner — ブログバナー画像生成スキル

## 目的
記事のタイトルとカテゴリから、ブログのヘッダー用バナー画像を生成する

## ターゲットユーザー
技術ブログを運営する開発者

## 入力
- 記事のタイトル（必須）
- 記事のカテゴリ（オプション）
- スタイル指定（オプション）

## 出力
- 1200×630px のバナー画像（PNG）
```

### スタイル体系を設計する

baoyu-cover-image の5Dスタイル体系を参考に、独自のスタイル体系を設計します：

```markdown
## スタイル体系

| 次元 | 説明 | 選択肢 |
|------|------|--------|
| Layout（レイアウト） | テキストと画像の配置 | centered, left-aligned, split, full-bleed |
| Palette（パレット） | 配色 | light, dark, brand, gradient |
| Accent（アクセント） | 強調色 | blue, green, orange, purple, red |
| Density（密度） | 情報量 | minimal, balanced, rich |
```

## ステップ2: SKILL.md の作成

baoyu流の自己完結型 SKILL.md を作成します。以下のポイントに従ってください：

1. **frontmatter** は実際の baoyu-skills のフォーマットに準拠（`metadata.openclaw` を含む）
2. **User Input Tools** と **Image Generation Tools** は SKILL.md に直接インライン記述（外部参照禁止）
3. **EXTEND.md** による設定管理をサポート

```yaml
---
name: baoyu-banner
description: Generates blog banner images from article titles and categories. Use when user needs a header image for a blog post.
version: 1.0.0
metadata:
  openclaw:
    homepage: https://github.com/your-name/baoyu-banner
    requires:
      anyBins:
        - bun
        - npx
---

# baoyu-banner

Generate professional blog banner images from article titles and categories.

## User Input Tools

When this skill prompts the user, follow this tool-selection rule (priority order):

1. **Prefer built-in user-input tools** exposed by the current agent runtime
2. **Fallback**: if no such tool exists, emit a numbered plain-text message
3. **Batching**: if the tool supports multiple questions per call, combine them

## Image Generation Tools

When this skill needs to render an image:

- **Use whatever image-generation tool or skill is available**
- **If multiple are available**, ask the user once which to use
- **Prompt file requirement**: write each prompt to a standalone file under `prompts/`

## EXTEND.md Configuration

This skill supports user preferences via EXTEND.md. On first run, if no EXTEND.md is found, the skill will prompt the user interactively.

**Search order** (first found wins):
1. `.baoyu-skills/baoyu-banner/EXTEND.md` (project scope)
2. `$XDG_CONFIG_HOME/baoyu-skills/baoyu-banner/EXTEND.md` (user scope)

**Example EXTEND.md**:
```yaml
default_layout: centered
default_palette: brand
default_accent: blue
default_density: balanced
```

## Usage

```bash
/baoyu-banner "Getting Started with Kubernetes" --category tech
/baoyu-banner "Design Thinking Workshop" --layout split --palette light
```

## Style System

### Layout
- **centered**: Title centered with decorative background
- **left-aligned**: Title on the left, abstract graphic on the right
- **split**: Split layout with category indicator
- **full-bleed**: Full background image with overlaid text

### Palette
- **light**: Clean white background with subtle patterns
- **dark**: Dark background with vibrant accents
- **brand**: Uses brand colors from the project
- **gradient**: Smooth gradient backgrounds

### Accent
Choose from: blue, green, orange, purple, red

### Density
- **minimal**: Just the title, lots of whitespace
- **balanced**: Title + category + subtle decoration
- **rich**: Title + category + tags + decorative elements

## Output

The generated banner will be saved to the current directory as:
`banner-<title-slug>.png`
```

## ステップ3: 実行スクリプトの作成

baoyu-skills のように、複雑なロジックはスクリプトに分離します：

```typescript
// scripts/main.ts
import { parseArgs } from "./args";
import { detectBackend } from "./backend";
import { generatePrompt } from "./prompt";

async function main() {
  // 1. 引数を解析
  const args = parseArgs(process.argv.slice(2));
  
  // 2. 利用可能な画像生成バックエンドを検出
  const backend = await detectBackend();
  if (!backend) {
    console.error("No image generation backend available.");
    console.error("Please set OPENAI_API_KEY or install baoyu-image-gen.");
    process.exit(1);
  }
  
  // 3. プロンプトを生成
  const prompt = generatePrompt({
    title: args.title,
    category: args.category,
    layout: args.layout,
    palette: args.palette,
    accent: args.accent,
    density: args.density,
  });
  
  // 4. 画像を生成
  const image = await backend.generate(prompt, {
    width: 1200,
    height: 630,
  });
  
  // 5. 保存
  const filename = `banner-${slugify(args.title)}.png`;
  await saveImage(image, filename);
  console.log(`Banner saved: ${filename}`);
}

main().catch(console.error);
```

## ステップ4: スキルのテスト

baoyu-skills のテスト方法を参考に、スキルをテストします：

```bash
# 1. 基本的な動作確認
/baoyu-banner "Test Title"

# 2. 全てのスタイルの組み合わせをテスト
for layout in centered left-aligned split full-bleed; do
  for palette in light dark brand gradient; do
    /baoyu-banner "Test $layout $palette" \
      --layout $layout --palette $palette
  done
done

# 3. エッジケースのテスト
/baoyu-banner ""  # 空のタイトル → エラーハンドリング
/baoyu-banner "A"  # 短いタイトル
/baoyu-banner "A very long title that might overflow the banner design"  # 長いタイトル
```

## ステップ5: スキルの公開

baoyu-skills のように、スキルを公開して他の人も使えるようにします：

### リポジトリ構成

```
baoyu-banner/
├── SKILL.md              # スキル定義
├── scripts/
│   ├── main.ts           # メイン実行スクリプト
│   ├── args.ts           # 引数パーサー
│   ├── backend.ts        # バックエンド検出
│   └── prompt.ts         # プロンプト生成
├── references/           # 参考資料
├── prompts/              # 生成プロンプトの保存先
├── CLAUDE.md             # Claude Code 用設定
├── package.json          # 依存関係
└── README.md             # リポジトリの説明
```

### 公開チェックリスト

- [ ] SKILL.md に明確な説明と使用例が含まれている
- [ ] 適切なタグが設定されている
- [ ] ライセンスファイルが含まれている
- [ ] README.md にインストール方法が記載されている
- [ ] テスト済みである
- [ ] 複数のAIエージェントで動作確認済み

## baoyu流 vs 標準的なスキル開発

| 観点 | 標準的なスキル開発 | baoyu流スキル開発 |
|------|------------------|-----------------|
| **SKILL.md** | プロンプトのみ | YAML front matter + 構造化された説明 |
| **実行ロジック** | SKILL.md 内に記述 | スクリプトに分離 |
| **スタイル体系** | 単純なオプション | 多次元に分解された体系 |
| **バックエンド** | 固定 | 抽象化され、選択可能 |
| **プロンプト管理** | なし | 保存・再利用可能 |
| **テスト** | 手動 | 体系的なテスト |

## まとめ

baoyu-skills の設計パターンを学ぶことで、以下のスキルが身につきました：

1. **自己完結型スキル**の設計方法
2. **スタイル体系**の設計と次元分解
3. **バックエンド抽象化**による柔軟な実行
4. **プロンプト管理**による再現性の確保
5. **クロスプラットフォーム**対応の考慮

これらの原則を適用することで、高品質で保守性の高いスキルを開発できます。

## 次のステップ

→ [Part 7: 付録・リファレンス](../07-appendix/01-glossary.md)

---

> **💡 参考リンク**: [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | [CLAUDE.md](https://github.com/JimLiu/baoyu-skills/blob/main/CLAUDE.md)
