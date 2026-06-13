# 6-3: AI画像生成バックエンドの選択

> **学習時間**: 15分 | **難易度**: ⭐⭐

## 概要

baoyu-skills のコンテンツ生成スキル（baoyu-cover-image, baoyu-infographic, baoyu-comic など）は、実際の画像生成を**バックエンドスキル**に委譲するアーキテクチャを採用しています。このセクションでは、利用可能な画像生成バックエンドの種類と、その選択基準を学びます。

## 画像生成バックエンドの種類

baoyu-skills では以下の3つの画像生成バックエンドが利用可能です：

| バックエンド | 必要APIキー | コスト | 品質 | 速度 |
|------------|-----------|-------|------|------|
| **baoyu-image-gen** | OpenAI / Azure / Google / OpenRouter / Replicate | 従量課金 | 高い | 普通 |
| **baoyu-danger-gemini-web** | 不要（ブラウザCookie） | 無料 | 高い | 速い |
| **codex-imagegen** | Codex CLI のサブスクリプション | サブスク内 | 高い | 普通 |

### baoyu-image-gen（推奨）

最も汎用的なバックエンドです。複数の画像生成APIを統一的に扱えます。

**対応プロバイダー**:

| プロバイダー | 設定方法 |
|------------|---------|
| **OpenAI**（DALL-E 3） | `OPENAI_API_KEY` 環境変数 |
| **Azure OpenAI** | `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_ENDPOINT` |
| **Google**（Gemini Imagen） | `GOOGLE_API_KEY` 環境変数 |
| **OpenRouter** | `OPENROUTER_API_KEY` 環境変数 |
| **DashScope**（Alibaba） | `DASHSCOPE_API_KEY` 環境変数 |
| **Replicate** | `REPLICATE_API_KEY` 環境変数 |

```bash
# 環境変数の設定例（OpenAI）
export OPENAI_API_KEY="sk-..."

# プロバイダーを指定して実行
/baoyu-cover-image article.md --provider openai
```

### baoyu-danger-gemini-web

Google Gemini の Web インターフェースを経由して画像生成を行います。**APIキー不要**で利用できるのが最大のメリットです。

**仕組み**:
1. Chrome ブラウザを起動（CDP = Chrome DevTools Protocol）
2. Gemini Web にログイン（初回のみ）
3. Web インターフェース経由で画像生成を実行

```bash
# 初回セットアップ（ログイン）
/baoyu-danger-gemini-web --login

# 画像生成
/baoyu-cover-image article.md --provider gemini-web
```

**注意点**:
- Chrome ブラウザが必要
- 初回のみログイン操作が必要
- 利用規約に従う必要がある

### codex-imagegen

OpenAI Codex CLI の画像生成機能をバックエンドとして利用します。Codex CLI のサブスクリプションがあれば、追加のAPIキーは不要です。

```bash
# Codex CLI バックエンドで実行
/baoyu-cover-image article.md --provider codex-cli
```

## バックエンド選択の自動化

baoyu-skills は実行時に利用可能なバックエンドを自動検出します：

```
コンテンツスキルが画像生成を要求
    ↓
利用可能なバックエンドをチェック
    ↓
┌─ 1つだけ利用可能 → 自動的にそれを使用
├─ 複数利用可能 → ユーザーに選択を確認
└─ なし → ユーザーに設定方法を案内
```

### 優先順位の設定

`EXTEND.md` に設定を記述することで、優先的に使用するバックエンドを指定できます：

```yaml
# EXTEND.md
preferred_image_backend: openai  # openai, azure, google, openrouter, replicate, gemini-web, codex-cli
```

## バックエンドの比較と選び方

### コスト重視の場合

```
個人利用・学習目的
    ↓
baoyu-danger-gemini-web が最適
- APIキー不要
- 無料
- ただしChromeが必要
```

### 品質重視の場合

```
プロダクション利用
    ↓
baoyu-image-gen（OpenAI DALL-E 3）が最適
- 最高品質の画像生成
- 安定したAPI
- 従量課金だが信頼性が高い
```

### 既存サブスクリプションを活用する場合

```
Codex CLI ユーザー
    ↓
codex-imagegen が最適
- 追加費用なし
- Codex CLI のサブスクリプション内で完結
```

## トラブルシューティング

| 問題 | 原因 | 解決策 |
|------|------|--------|
| APIキーエラー | 環境変数が未設定 | `export OPENAI_API_KEY="sk-..."` を実行 |
| Gemini Web ログインエラー | セッション切れ | `--login` で再ログイン |
| Chrome が見つからない | Chrome 未インストール | Chrome をインストール |
| レート制限 | APIの呼び出し制限 | 時間を空けて再試行 |
| 画像品質が低い | プロバイダーの制限 | 別のプロバイダーを試す |

## 次のステップ

→ [6-4: 実プロジェクトでのスキル連携](04-skill-pipeline.md)
