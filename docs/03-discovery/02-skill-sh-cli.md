# gh コマンドによるスキル検索

> **学習時間**: 10分 | **難易度**: ⭐⭐

## 概要

GitHub CLI（`gh`）を使って、GitHub 上で公開されているスキルを検索・取得する方法を学びます。`gh` は GitHub が公式に提供する CLI ツールで、リポジトリ検索からファイル取得まで一貫して対応できます。

## 前提条件

- GitHub CLI（gh v2.40 以上）がインストールされている
- `gh auth login` でログイン済み
- Copilot サブスクリプションが有効

## インストール確認

```bash
# バージョン確認（v2.40 以上を推奨）
gh --version

# 未インストール・古いバージョンの場合
# macOS
brew install gh

# Windows
winget install GitHub.cli

# Ubuntu / Debian
sudo apt install gh

# ログイン
gh auth login
```

## スキルの検索

### トピック検索でスキルを探す

```bash
# "agent-skills" トピックで公開スキルを検索
gh search repos --topic agent-skills --limit 20

# "copilot-skills" トピックでも検索
gh search repos --topic copilot-skills --limit 20

# キーワードを絞り込む
gh search repos --topic agent-skills frontend --limit 10
```

### 著名なスキルリポジトリを確認する

```bash
# Anthropic 公式スキル（skill-creator, grill-me など）
gh repo view anthropics/skills

# コミュニティスキル集
gh repo view github/awesome-copilot --readme
```

## スキルの取得

### 方法1: リポジトリをクローンして必要スキルをコピー

```bash
# 公式リポジトリをクローン
gh repo clone anthropics/skills /tmp/anthropic-skills

# 必要なスキルを Claude Code 用にコピー
mkdir -p .claude/skills/grill-me/
cp /tmp/anthropic-skills/skills/grill-me/SKILL.md .claude/skills/grill-me/SKILL.md

# GitHub Copilot 用にもコピー
mkdir -p .github/skills/grill-me/
cp .claude/skills/grill-me/SKILL.md .github/skills/grill-me/SKILL.md
```

### 方法2: GitHub API 経由で直接取得（Linux / macOS）

```bash
# gh api でファイルの内容を取得し、base64 デコードして保存
mkdir -p .claude/skills/grill-me/
gh api repos/anthropics/skills/contents/skills/grill-me/SKILL.md \
  --jq '.content' | base64 -d > .claude/skills/grill-me/SKILL.md
```

### 方法3: curl で直接ダウンロード

```bash
mkdir -p .claude/skills/grill-me/
curl -o .claude/skills/grill-me/SKILL.md \
  https://raw.githubusercontent.com/anthropics/skills/main/skills/grill-me/SKILL.md
```

> **パス確認**: `raw.githubusercontent.com` の URL はリポジトリのディレクトリ構造に依存します。取得前にブラウザまたは `gh repo view` でパスを確認してください。

## 一括取得の実践例

```bash
# 複数スキルをまとめてインストール
gh repo clone anthropics/skills /tmp/anthropic-skills

for skill in grill-me triage improve; do
  mkdir -p ".claude/skills/$skill"
  cp "/tmp/anthropic-skills/skills/$skill/SKILL.md" ".claude/skills/$skill/SKILL.md" \
    && echo "✅ $skill インストール完了" \
    || echo "❌ $skill が見つかりません（パスを確認）"
done
```

## 主なコマンド一覧

| コマンド | 説明 | 使用例 |
|---------|------|--------|
| `gh search repos` | リポジトリをキーワード/トピックで検索 | `gh search repos --topic agent-skills` |
| `gh repo view` | リポジトリの詳細・README を表示 | `gh repo view anthropics/skills` |
| `gh repo clone` | リポジトリをクローン | `gh repo clone anthropics/skills` |
| `gh api` | GitHub API 経由でファイルを取得 | `gh api repos/owner/repo/contents/path` |
| `gh auth login` | GitHub アカウントにログイン | `gh auth login` |

## トラブルシューティング

| 問題 | 原因 | 解決策 |
|------|------|--------|
| `gh` が見つからない | GitHub CLI 未インストール | `winget install GitHub.cli` または `brew install gh` |
| 認証エラー | ログインしていない | `gh auth login` を実行 |
| 検索結果が少ない | トピック未設定のリポジトリが多い | `--topic` なしのキーワード検索も試す |
| `base64 -d` が使えない | Windows 環境 | 方法1（クローン）または方法3（curl）を使う |
| コピー先パスが違う | リポジトリ構造が変わった | `gh repo view` でディレクトリ構造を確認 |

## 次のステップ

→ [3-3: スキルの共有とチーム展開](03-sharing-team-deployment.md)
