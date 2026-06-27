# 環境セットアップ

> **学習時間**: 10分 | **難易度**: ⭐

## 前提条件

- **Claude Code ユーザー**: Anthropic アカウント + Claude Code がインストール済み
- **GitHub Copilot ユーザー**: GitHub アカウント（Copilot サブスクリプション付き）
- テキストエディタ（VS Code 推奨）
- （オプション）GitHub CLI（gh）がインストールされた環境

## ステップ1: Claude Code のセットアップ

### Claude Code のインストール

```bash
# npm 経由でインストール（公式・推奨）
npm install -g @anthropic-ai/claude-code
```

> **注意**: Homebrew での `brew install claude-code` は公式サポート外です。npm を使ってください。

### スキルディレクトリの確認

Claude Code は自動的に以下のディレクトリからスキルを読み込みます：

| 種類 | パス | 適用範囲 |
|------|------|---------|
| 個人用 | `~/.claude/skills/<name>/SKILL.md` | 全プロジェクト |
| プロジェクト用 | `.claude/skills/<name>/SKILL.md` | そのプロジェクトのみ |

### 動作確認

```bash
# Claude Code を起動
claude

# セッション内でバンドルスキルを確認
/help
```

## ステップ2: GitHub Copilot のセットアップ

### スキルディレクトリの準備

GitHub Copilot では、リポジトリの `.github/skills/` ディレクトリにスキルを配置します：

```bash
# リポジトリのルートで実行
mkdir -p .github/skills/
```

### ディレクトリ構成例

```
.github/skills/
├── grill-me/
│   └── SKILL.md
├── triage/
│   └── SKILL.md
├── improve/
│   └── SKILL.md
├── frontend-design/
│   └── SKILL.md
└── ui-ux-pro-max/
    └── SKILL.md
```

### GitHub Copilot CLI の確認

```bash
# GitHub CLI がインストールされているか確認
gh --version

# GitHub アカウントにログイン（未ログインの場合）
gh auth login

# Copilot 拡張の確認（GitHub CLI v2.40+ で利用可能）
gh copilot --help
```

> **注意**: `gh skill` というコマンドは存在しません。GitHub CLI の Copilot 機能は `gh copilot` サブコマンドで提供されます。スキルファイルの管理は `.github/skills/` ディレクトリへの手動配置が基本です。

## ステップ3: 両方の環境で使える共通スキルを作成する

このチュートリアルのサンプルスキルは、**Claude Code と GitHub Copilot の両方で動作する**ように設計されています。SKILL.md のフォーマットは Agent Skills オープンスタンダードに準拠しており、配置場所を変えるだけで両方のプラットフォームで使用できます。

### Claude Code で使う場合

```bash
# プロジェクト用（anthropics/skills の grill-me を例に）
mkdir -p .claude/skills/grill-me/
curl -o .claude/skills/grill-me/SKILL.md \
  https://raw.githubusercontent.com/anthropics/skills/main/skills/grill-me/SKILL.md
```

### GitHub Copilot で使う場合

```bash
mkdir -p .github/skills/grill-me/
curl -o .github/skills/grill-me/SKILL.md \
  https://raw.githubusercontent.com/anthropics/skills/main/skills/grill-me/SKILL.md
```

> **ヒント**: スキルファイルのパスはリポジトリ構造によって異なります。取得前に [anthropics/skills](https://github.com/anthropics/skills) でディレクトリ構造を確認してください。

## トラブルシューティング

| 問題 | 原因 | 解決策 |
|------|------|--------|
| Claude Code が起動しない | インストール未完了 | `npm install -g @anthropic-ai/claude-code` を再実行 |
| スキルが認識されない | パスが間違っている | `.claude/skills/<name>/SKILL.md` のパスを確認 |
| Copilot がスキルを実行しない | スキル名が間違っている | `.github/skills/` のディレクトリ名とスキル名を確認 |
| `gh copilot` が使えない | GitHub CLI 未インストール・古いバージョン | `gh --version` で確認し、v2.40 以上にアップデート |

## 参考リンク

- [Claude Code ドキュメント](https://docs.anthropic.com/en/docs/claude-code/)
- [GitHub Copilot Agent Skills ドキュメント](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)
- [anthropics/skills（公式スキルリポジトリ）](https://github.com/anthropics/skills)
- [awesome-copilot（コミュニティスキル集）](https://github.com/github/awesome-copilot)

## 次のステップ

環境が整いました！次のセクションに進みましょう：

→ [2-1: Agent Skills とは](../02-skill-creation/01-what-are-agent-skills.md)
