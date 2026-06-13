# 4-6: baoyu-diagram — SVG図形生成スキル

> **学習時間**: 25分 | **難易度**: ⭐⭐⭐ | **カテゴリ**: コンテンツ生成

## 概要

**baoyu-diagram** は、ソース素材から SVG 図形を生成するスキルです。フローチャート、シーケンス図、アーキテクチャ図、概念図、クラス図の5タイプをサポートし、ダークモード対応の自己完結型 SVG を出力します。

このスキルの特徴は、**LLM の画像生成モデルを使わずに、Claude が SVG コードを直接記述する**点です。これにより、デザインシステムに従った一貫性のある図形を生成できます。

## 学習目標

- baoyu-diagram の5つの図タイプを理解する
- SVG 直書きによる図形生成の仕組みを学ぶ
- ダークモード対応の実装方法を理解する
- 図タイプの自動選択ロジックを学ぶ

## 利用シーン

| シーン | 説明 |
|-------|------|
| 技術記事の図解 | JWT認証フロー、Kubernetesアーキテクチャなどを図示 |
| ドキュメント作成 | API仕様書のシーケンス図、クラス図を自動生成 |
| プレゼン資料 | 概念図やアーキテクチャ図をスライドに埋め込み |
| 設計レビュー | システム構成を可視化してレビュー |

## 5つの図タイプ

baoyu-diagram は以下の5タイプの図をサポートしています：

| タイプ | 説明 | トリガーとなるキーワード |
|-------|------|------------------------|
| **flowchart** | ステップを順に追うプロセス図 | walk through, steps, process, lifecycle, workflow, state machine |
| **sequence** | コンポーネント間の通信順序 | protocol, handshake, auth flow, OAuth, TCP, request/response |
| **structural** | 内部構造や構成の階層図 | architecture, components, topology, layout, what's inside |
| **illustrative** | メカニズムの直感的な説明図 | how does X work, explain X, intuition for, why does X do Y |
| **class** | 型と関係性のUML図 | class diagram, UML, inheritance, interface, schema |

### 自動タイプ選択

入力内容を分析し、最適な図タイプを自動提案します：

```bash
# 自動選択（推奨）
/baoyu-diagram "how JWT authentication works"

# タイプを指定
/baoyu-diagram "Kubernetes architecture" --type structural
/baoyu-diagram "OAuth 2.0 flow" --type sequence

# ファイルから読み込み
/baoyu-diagram path/to/article.md
```

## SVG 直書きの仕組み

baoyu-diagram の核心は、**Claude が SVG コードを手計算のレイアウト計算とともに直接記述する**点です。

### デザインシステム

全ての図は統一されたデザインシステムに従います：

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <style>
    /* 統一されたスタイル定義 */
    .node { fill: #f0f4ff; stroke: #4a6cf7; stroke-width: 2; rx: 8; }
    .arrow { stroke: #666; stroke-width: 1.5; fill: none; marker-end: url(#arrowhead); }
    .label { font-family: system-ui; font-size: 13px; fill: #333; text-anchor: middle; }

    /* ダークモード対応 */
    @media (prefers-color-scheme: dark) {
      .node { fill: #1a1a2e; stroke: #6b8cff; }
      .label { fill: #e0e0e0; }
      .arrow { stroke: #999; }
    }
  </style>
  <!-- 図の内容 -->
</svg>
```

### ダークモード対応

生成される SVG は `@media (prefers-color-scheme: dark)` メディアクエリを埋め込んでおり、ユーザーのシステム設定に応じて自動的にライト/ダークモードを切り替えます。これにより、1つの SVG ファイルをどこに埋め込んでも適切に表示されます。

## 使用例

### 基本的な使い方

```bash
# トピックを指定して生成
/baoyu-diagram "how JWT authentication works"

# 言語指定
/baoyu-diagram "Kubernetesアーキテクチャ" --lang ja

# 出力先指定
/baoyu-diagram "build pipeline" --out docs/build-pipeline.svg
```

### オプション一覧

| オプション | 説明 |
|-----------|------|
| `--type <name>` | 図タイプを指定（flowchart, sequence, structural, illustrative, class, auto） |
| `--lang <code>` | 出力言語（en, zh, ja, ...） |
| `--out <path>` | 出力ファイルパス |

## 実装のポイント

### レイアウト計算

Claude は SVG を生成する際、以下のレイアウト計算を手動で行います：

1. **ノード配置**: 各要素の位置とサイズを計算
2. **エッジルーティング**: ノード間のパスを計算（曲線、直線、直交線）
3. **テキスト配置**: ラベルの位置と改行を計算
4. **階層レイアウト**: ツリー構造の自動配置

### 自己完結型 SVG

生成される SVG は以下の特徴を持ちます：

- 外部依存ゼロ（フォントは system-ui を使用）
- 埋め込みスタイル（`<style>` タグ内に全てのスタイル定義）
- ダークモード自動対応
- レスポンシブ（viewBox によるスケーリング）

## 学びのポイント

baoyu-diagram から学べるスキル設計のポイント：

1. **LLM のコード生成能力を活用**: 画像生成APIに頼らず、コード生成で図を作るアプローチ
2. **デザインシステムの統一**: 全図形で一貫したスタイルを適用
3. **自動タイプ選択**: 入力内容から最適な出力形式を判断するロジック
4. **ダークモード対応**: メディアクエリによる環境適応

## 次のステップ

→ [4-7: baoyu-infographic — インフォグラフィック生成スキル](07-baoyu-infographic.md)

---

> **💡 参考リンク**: [baoyu-diagram](https://github.com/JimLiu/baoyu-skills/tree/main/skills/baoyu-diagram)
