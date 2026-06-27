# コンテンツ生成スキルを使いこなす

> **学習時間**: 20分 | **難易度**: ⭐⭐⭐

## 概要

このセクションでは、baoyu-skills の主要なコンテンツ生成スキルを実際のユースケースに沿って使いこなす方法を学びます。各スキルの基本的な使い方は Part 5 で学びましたが、ここでは**実践的な組み合わせと応用**に焦点を当てます。

## シナリオ: 技術記事の作成

ある技術記事を例に、baoyu-skills をフル活用する流れを見ていきます。

> **💡 実行方法について**: baoyu-skills の各スキルは、エージェントのランタイムに応じて呼び出し方が異なります。Claude Code ではスラッシュコマンド（`/baoyu-cover-image`）、Codex CLI では `npx skills run` 経由、また直接スクリプトを実行することもできます。以下の例では主にスラッシュコマンド形式で示します。

### ステップ1: カバー画像の生成（baoyu-cover-image）

記事の顔となるカバー画像を生成します。

```bash
# 記事の内容から自動生成（Claude Code）
/baoyu-cover-image articles/kubernetes-networking.md

# スタイルを指定して生成
/baoyu-cover-image articles/kubernetes-networking.md \
  --type conceptual \
  --palette cool \
  --rendering digital

# アスペクト比を指定（ブログの推奨サイズ）
/baoyu-cover-image articles/kubernetes-networking.md --aspect 2.35:1
```

**5Dスタイル体系の活用ポイント**:

| 次元 | 技術記事向けの推奨設定 |
|------|---------------------|
| Type | conceptual（概念図）または metaphor（比喩表現） |
| Palette | cool（クール）または dark（ダーク） |
| Rendering | digital（デジタル）または flat-vector（フラット） |
| Text | title-subtitle（タイトル+サブタイトル） |
| Mood | balanced（バランス）または bold（大胆） |

### ステップ2: 図解の生成（baoyu-diagram）

記事内で説明する概念を図解します。baoyu-diagram は画像生成APIを使わず、Claude が SVG コードを直接記述する点が特徴です。

```bash
# 記事の特定セクションから図を生成
/baoyu-diagram "Kubernetes networking: how pods communicate with each other"

# 図タイプを指定
/baoyu-diagram "Kubernetes networking architecture" --type structural

# 出力先を指定
/baoyu-diagram "Kubernetes networking architecture" \
  --type structural \
  --out images/k8s-networking-architecture.svg
```

**図タイプ選択のコツ**:

| 説明したい内容 | 推奨図タイプ |
|--------------|------------|
| 処理の流れ | flowchart |
| コンポーネント間通信 | sequence |
| システム構成 | structural |
| 概念の仕組み | illustrative |
| データモデル | class |

### ステップ3: インフォグラフィックの生成（baoyu-infographic）

記事の要点をまとめたインフォグラフィックを生成します。21のレイアウトと17のスタイルから自動推薦されます。

```bash
# 記事全体から自動推薦
/baoyu-infographic articles/kubernetes-networking.md

# 比較表として生成
/baoyu-infographic articles/kubernetes-networking.md \
  --layout comparison-table \
  --style technical-schematic

# 縦長で生成（SNS投稿用）
/baoyu-infographic articles/kubernetes-networking.md \
  --layout pyramid \
  --aspect portrait
```

### ステップ4: プレゼン資料の生成（baoyu-slide-deck）

記事を基にしたプレゼン資料を生成します。

```bash
# 記事からスライドを自動生成
/baoyu-slide-deck articles/kubernetes-networking.md

# スタイルと対象者を指定
/baoyu-slide-deck articles/kubernetes-networking.md \
  --style blueprint \
  --audience intermediate

# スライド数を指定
/baoyu-slide-deck articles/kubernetes-networking.md --slides 15
```

## スキル間の連携パターン

### パターン1: 記事→図→インフォグラフィック

```
記事を書く
    ↓
baoyu-diagram で技術的な図解を生成
    ↓
baoyu-infographic で記事の要点を視覚化
    ↓
両方を記事に埋め込んで公開
```

### パターン2: 記事→カバー→スライド

```
記事を書く
    ↓
baoyu-cover-image でカバー画像を生成
    ↓
baoyu-slide-deck でプレゼン資料を生成
    ↓
カバー画像をスライドの表紙に設定
```

### パターン3: 記事→多言語化→公開

```
記事を書く
    ↓
baoyu-translate で英語/中国語に翻訳
    ↓
baoyu-cover-image で各言語版のカバー画像を生成
    ↓
baoyu-markdown-to-html でHTML出力
```

## 実践的なヒント

### 1. スタイルの一貫性を保つ

複数のスキルを使う場合、スタイルを統一することでプロフェッショナルな印象になります：

```bash
# カバー画像とインフォグラフィックで同じパレットを使用
/baoyu-cover-image article.md --palette cool
/baoyu-infographic article.md --style technical-schematic
# → coolパレットとtechnical-schematicは相性が良い
```

### 2. アスペクト比を統一する

ブログやSNSに合わせてアスペクト比を統一しましょう：

| プラットフォーム | 推奨アスペクト比 |
|----------------|----------------|
| ブログ（アイキャッチ） | 2.35:1 または 16:9 |
| Twitter/X | 16:9 |
| Instagram（フィード） | 1:1（スクエア） |
| Instagram（ストーリー） | 9:16（ポートレート） |
| LinkedIn | 1.91:1 |

### 3. プロンプトを再利用する

生成されたプロンプトは `prompts/` ディレクトリに保存されるため、微調整や再生成が容易です：

```bash
# プロンプトを編集して再生成
# prompts/01-cover.md を編集
/baoyu-cover-image article.md --prompts-only
# → 編集後に --images-only で再生成
```

## 次のステップ

→ [6-3: AI画像生成バックエンドの選択](03-image-gen-backends.md)
