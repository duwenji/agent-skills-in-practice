# 0-2: 環境セットアップ

> **学習時間**: 10分 | **難易度**: ⭐

## 前提条件

- **Claude Code ユーザー**: Anthropic アカウント + Claude Code がインストール済み
- **GitHub Copilot ユーザー**: GitHub アカウント（Copilot サブスクリプション付き）
- テキストエディタ（VS Code 推奨）
- （オプション）GitHub CLI（gh）がインストールされた環境

## ステップ1: Claude Code のセットアップ

### Claude Code のインストール

```bash
# npm 経由でインストール
npm install -g @anthropic-ai/claude-code

# または Homebrew（macOS）
brew install claude-code
```

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

### gh skill コマンドの確認

```bash
# GitHub CLI でスキル関連コマンドを確認
gh skill --help
```

## ステップ3: 両方の環境で使える共通スキルを作成する

このチュートリアルのサンプルスキルは、**Claude Code と GitHub Copilot の両方で動作する**ように設計されています。SKILL.md のフォーマットは Agent Skills オープンスタンダードに準拠しており、配置場所を変えるだけで両方のプラットフォームで使用できます。

### Claude Code で使う場合

```bash
# プロジェクト用（Matt Pocock の grill-me を例に）
mkdir -p .claude/skills/grill-me/
curl -o .claude/skills/grill-me/SKILL.md \
  https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grill-me/SKILL.md
```

### GitHub Copilot で使う場合

```bash
mkdir -p .github/skills/grill-me/
curl -o .github/skills/grill-me/SKILL.md \
  https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grill-me/SKILL.md
```

## トラブルシューティング

| 問題 | 原因 | 解決策 |
|------|------|--------|
| Claude Code が起動しない | インストール未完了 | `npm install -g @anthropic-ai/claude-code` を再実行 |
| スキルが認識されない | パスが間違っている | `.claude/skills/<name>/SKILL.md` のパスを確認 |
| Copilot がスキルを実行しない | スキル名が間違っている | `.github/skills/` のディレクトリ名とスキル名を確認 |
| gh skill が使えない | GitHub CLI 未インストール | `gh` コマンドが使えるか確認 |

## 参考リンク

- [Claude Code Skills ドキュメント](https://code.claude.com/docs/en/skills)
- [GitHub Copilot Agent Skills ドキュメント](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)
- [Agent Skills オープンスタンダード](https://agentskills.io)
- [agentskills/agentskills (GitHub)](https://github.com/agentskills/agentskills)
- [awesome-copilot（コミュニティスキル集）](https://github.com/github/awesome-copilot)

## 次のステップ

環境が整いました！次のセクションに進みましょう：

→ [1-1: Agent Skills とは](../01-skill-creation/01-what-are-agent-skills.md)
