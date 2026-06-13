# 2-2: skill.sh によるCLI検索

> **学習時間**: 15分 | **難易度**: ⭐⭐

## 概要

**skill.sh** は、コマンドラインからスキルを検索・実行するためのツールです。GitHub CLI（gh）と連携して動作し、ターミナルから直接スキルを操作できます。

## 前提条件

- GitHub CLI（gh）がインストールされている
- `gh` で GitHub アカウントにログイン済み
- Copilot サブスクリプションが有効

## インストール

```bash
# GitHub CLI のインストール確認
gh --version

# skill.sh のダウンロード
curl -O https://raw.githubusercontent.com/github-copilot/skill.sh/main/skill.sh
chmod +x skill.sh
```

## 基本的な使い方

### スキルの検索

```bash
# キーワードで検索
./skill.sh search code-review

# タグでフィルタリング
./skill.sh search --tag frontend

# 詳細表示
./skill.sh search --verbose accessibility
```

### スキルの実行

```bash
# スキルを直接実行
./skill.sh run code-review --input "コードをここに"

# パラメータを指定して実行
./skill.sh run code-review \
  --param code="function add(a,b) { return a+b; }" \
  --param language="javascript"
```

### スキル情報の表示

```bash
# スキルの詳細情報を表示
./skill.sh info code-review

# スキルのパラメータ一覧
./skill.sh params code-review
```

## 主なコマンド一覧

| コマンド | 説明 | 使用例 |
|---------|------|--------|
| `search` | スキルを検索 | `skill.sh search code-review` |
| `run` | スキルを実行 | `skill.sh run <スキル名>` |
| `info` | スキル詳細を表示 | `skill.sh info <スキル名>` |
| `params` | パラメータ一覧 | `skill.sh params <スキル名>` |
| `list` | 利用可能なスキル一覧 | `skill.sh list` |
| `install` | スキルをインストール | `skill.sh install <URL>` |

## 実践例

### コードレビューの自動化

```bash
# 変更されたファイルをレビュー
git diff --name-only HEAD~1 | while read file; do
  ./skill.sh run code-review \
    --param code="$(cat $file)" \
    --param language="typescript"
done
```

### Issue の一括トリアージ

```bash
# 未トリアージの Issue を一括処理
gh issue list --label "needs-triage" --json number,title,body \
  | jq -c '.[]' \
  | while read issue; do
    ./skill.sh run triage \
      --param issue_title="$(echo $issue | jq -r '.title')" \
      --param issue_body="$(echo $issue | jq -r '.body')"
  done
```

## トラブルシューティング

| 問題 | 原因 | 解決策 |
|------|------|--------|
| `gh` が見つからない | GitHub CLI 未インストール | `winget install GitHub.cli` または `brew install gh` |
| 認証エラー | ログインしていない | `gh auth login` を実行 |
| スキルが見つからない | スキル名が間違っている | `skill.sh search` で正しい名前を確認 |
| 実行権限エラー | パーミッション不足 | `chmod +x skill.sh` を実行 |

## 次のステップ

→ [2-3: スキルの共有とチーム展開](03-sharing-team-deployment.md)
