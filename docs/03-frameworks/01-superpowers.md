# 3-1: Superpowers — コーディングエージェントの開発方法論

> **学習時間**: 20分 | **難易度**: ⭐⭐

## エージェントが「暴走」したことはないですか？

Claude Code や GitHub Copilot を使い始めて、こんな経験をしたことはないでしょうか。

---

**シーン1：仕様を聞かずに実装が始まった**

> 「ユーザー認証機能を追加して」

そう頼んだら、エージェントはすぐにコードを書き始めました。
30分後、できあがったのは「メールアドレス＋パスワード認証」。
でも欲しかったのは「GitHub OAuth」でした。

---

**シーン2：「完了」と言ったのに動かなかった**

> 「テストを追加して」

エージェントは「テストを追加しました！」と報告。
実行してみると、テストが存在しないファイルを参照していてエラー。
「完了」は嘘でした。

---

**シーン3：バグを直したら別の場所が壊れた**

> 「このバグを修正して」

エージェントは修正しました。でも原因を調べずに症状だけを隠したため、
同じバグが別の形で翌日また現れました。

---

これらは「エージェントが賢くない」のではありません。
**エージェントが「段取り」を知らずに動いているのが原因です。**

## エージェントの標準動作は「即コード」

人間のエンジニアなら、機能追加を頼まれたとき自然にこうします：

1. 要件を確認する（何を作るのか、制約は何か）
2. 設計を考える（どう実装するか複数案を比較）
3. 計画を立てる（どの順番で、どのファイルを触るか）
4. 実装する
5. 動作確認する

ところがエージェントの標準動作は違います：

1. 指示を受ける
2. **即コードを書く** ← ここで①〜③がすっ飛ぶ

これは設計ではなく、**デフォルトの習慣**の問題です。
エージェントに「考えてから動く」という習慣を持たせる方法があります。
それが **Superpowers** です。

## Superpowers — エージェントに「段取り」を教えるプラグイン

**Superpowers** は、Jesse Vincent 氏（Prime Radiant）が開発した
**コーディングエージェント向けの開発方法論プラグイン**です。

- **リポジトリ**: [github.com/obra/superpowers](https://github.com/obra/superpowers)

インストールするだけで、エージェントの動作が変わります：

| 標準のエージェント | Superpowers 導入後 |
|------------------|------------------|
| 指示を受けたら即コードを書く | まず要件と設計を確認する |
| 「完了」と言って動かないことがある | 検証を終えるまで完了と言えない |
| バグを症状だけ隠して終わる | 原因を究明してから直す |
| 大きな変更を一気に行う | 小さなタスクに分割して順番に進める |

> 公式 README より：「Superpowers is a complete software development methodology for your coding agents, built on top of a set of composable skills and some initial instructions that make sure your agent uses them.」

### 仕組み：スキルという設計図

Superpowers は複数の**スキル**（作業手順の定義ファイル）で構成されています。エージェントは状況を判断し、適切なスキルを自動的に起動します。

### 用語の説明

Superpowers を理解する上で重要な用語を説明します：

| 用語 | 説明 |
|------|------|
| **Plugin（プラグイン）** | エージェントに追加機能を提供する拡張モジュール。Superpowers 自体がプラグインとして提供され、インストールすることでエージェントに開発方法論を追加する。 |
| **Plugin Marketplace（プラグインマーケットプレイス）** | プラグインを配布・インストールするための公式ストア。Claude Code には Anthropic 公式のマーケットプレイスがあり、`/plugin install` コマンドでインストールできる。 |
| **Skill（スキル）** | エージェントに特定の手順・作業フローを覚えさせるための定義ファイル（SKILL.md）。Superpowers は複数のスキルを組み合わせて構成されている。 |
| **Subagent（サブエージェント）** | メインのエージェントから起動される子エージェント。独立したコンテキストを持ち、親セッションの履歴を継承せずにタスクを実行する。 |
| **HARD-GATE** | Superpowers のスキル内に定義された強制ゲート。特定の条件（例：設計承認）を満たすまで、次のアクション（例：コードを書く）を禁止する仕組み。 |
| **Worktree（git worktree）** | Git の機能で、同じリポジトリから独立した作業ディレクトリを複数作成できる。Superpowers はこれを利用して、クリーンな状態で開発を開始する。 |

## 対応エージェントとインストール方法

Superpowers は特定のエージェントに依存せず、複数のコーディングエージェントに対応しています：

| エージェント | インストール方法 |
|------------|----------------|
| **Claude Code** | `/plugin install superpowers@claude-plugins-official` |
| **Codex CLI** | `/plugins` → `superpowers` を検索 |
| **Codex App** | サイドバーの Plugins からインストール |
| **Factory Droid** | `droid plugin marketplace add https://github.com/obra/superpowers` |
| **Gemini CLI** | `gemini extensions install https://github.com/obra/superpowers` |
| **OpenCode** | `.opencode/INSTALL.md` の手順に従う |
| **Cursor** | `/add-plugin superpowers` |
| **GitHub Copilot CLI** | `copilot plugin install superpowers@superpowers-marketplace` |

## 実際の使い方

### Claude Code での使い方

Claude Code（ターミナル上の CLI エージェント）で Superpowers を使う手順です。

**1. インストール**

```bash
# Claude Code を起動
claude

# Claude Code のセッション内で以下のコマンドを実行
/plugin install superpowers@claude-plugins-official

# プラグインをリロード
/reload-plugins
```

インストール後、`~/.claude/settings.json` の `enabledPlugins` に自動追記されます：

```json
{
  "enabledPlugins": {
    "superpowers@claude-plugins-official": true
  }
}
```

**2. 基本的な使い方**

インストール後は特別な操作は不要です。普段通りに Claude Code に指示を出すだけで、Superpowers のスキルが自動的に起動します：

```bash
# 例1: 機能追加を依頼 → brainstorming が自動起動
claude "このプロジェクトにユーザー認証機能を追加して"

# 例2: バグ修正を依頼 → systematic-debugging が自動起動
claude "ログインボタンをクリックしても何も起きないバグを直して"

# 例3: 明示的にスキルを呼び出す場合
/brainstorming "検索機能の設計について相談したい"
```

### VS Code + GitHub Copilot での使い方

VS Code 上の GitHub Copilot で Superpowers を使う場合、対応しているのは **GitHub Copilot CLI**（ターミナル上の CLI モード）のみです。VS Code のチャット画面（`Ctrl+I` や `@Copilot`）では直接動作しません。

**1. GitHub Copilot CLI のインストール**

```bash
# GitHub Copilot CLI をインストール（VS Code とは別に CLI ツールが必要）
npm install -g @githubnext/github-copilot-cli

# 認証設定
github-copilot-cli auth
```

**2. Superpowers プラグインのインストール**

```bash
# GitHub Copilot CLI に Superpowers マーケットプレイスを登録
copilot plugin marketplace add obra/superpowers-marketplace

# Superpowers をインストール
copilot plugin install superpowers@superpowers-marketplace
```

**3. GitHub Copilot CLI で使用**

```bash
# GitHub Copilot CLI を起動
copilot

# 通常通り指示を出す（Superpowers が自動起動）
"このプロジェクトにテストを追加して"
```

**4. VS Code 上の GitHub Copilot との違い**

| 環境 | Superpowers の対応 |
|------|------------------|
| **GitHub Copilot CLI**（ターミナル） | ✅ 対応。プラグインとしてインストール可能 |
| **VS Code Copilot チャット**（`Ctrl+I`） | ❌ 非対応。プラグイン機構がない |
| **VS Code Copilot エージェントモード**（`Ctrl+Shift+I`） | ❌ 非対応。プラグイン機構がない |

> 💡 **補足**: VS Code 上の GitHub Copilot では Superpowers プラグインは動作しませんが、本チュートリアルで学ぶ **Agent Skills（`.github/skills/` に配置する SKILL.md）** は VS Code 上でも `@skill-name` で呼び出せます。Superpowers の設計思想を参考に、Copilot 用のスキルを自作することが本チュートリアルの目的です。

### インストールの確認方法

Superpowers が正しくインストールされたか確認するには、以下のコマンドを実行します：

```bash
# Claude Code の場合
/plugin list
# → 一覧に superpowers@claude-plugins-official が表示されれば成功

# GitHub Copilot CLI の場合
copilot plugin list
# → 一覧に superpowers@superpowers-marketplace が表示されれば成功
```

## 同じ依頼で何が変わるのか

### Before：Superpowers なし

```
$ claude "TODOアプリにタグ付け機能を追加して"

Claude: わかりました。タグ付け機能を実装します。
[すぐにコードを書き始める]
... 30分後 ...
Claude: 実装が完了しました！
$ # → 動作確認なし。仕様の確認なし。設計の検討なし。
```

### After：Superpowers あり

```
$ claude "TODOアプリにタグ付け機能を追加して"

Claude: タグ付け機能について確認します。
        タグはユーザーが自由に入力できますか？
        それとも事前定義されたタグから選択しますか？

あなた: 自由入力でお願いします

Claude: ありがとうございます。3つの実装案を比較してみましょう...
        [設計の選択肢を提示]

あなた: 案2で進めてください

Claude: 実装計画を作成しました。以下の5タスクに分割します：
        1. データモデルの追加（Tag テーブル）
        2. API エンドポイントの実装
        ...
        [タスク1を実行 → 動作確認 → タスク2を実行...]

Claude: 全タスク完了しました。テストを実行して確認します...
        ✅ 全テスト通過を確認しました。
```

違いは「賢さ」ではなく「プロセスの有無」です。

## 基本ワークフロー

Superpowers は以下の一連の流れで動作します：

```
① brainstorming
   ユーザーのアイデアを設計に昇華する
   ↓ 設計承認後
② using-git-worktrees
   独立したワークツリーを作成し、クリーンな状態を確保
   ↓
③ writing-plans
   設計を 2-5 分単位のタスクに分割した実装計画を作成
   ↓
④ subagent-driven-development / executing-plans
   タスクごとにサブエージェントを起動して並行実行
   ↓
⑤ test-driven-development
   RED-GREEN-REFACTOR の TDD サイクルを徹底
   ↓
⑥ requesting-code-review
   タスク完了ごとにコードレビューを実施
   ↓
⑦ finishing-a-development-branch
   全タスク完了後、マージ/PR/破棄を判断
```

## スキル一覧（リファレンス）

> 必要なときに参照してください。最初から全部覚える必要はありません。

### 設計・計画

- **brainstorming** — 実装前に要件と設計を整理する。ソクラテス式の対話を通じてアイデアを洗練し、複数の実現方法を比較検討した上でユーザーの承認を得る。**HARD-GATE** により、設計承認なしに実装コードを書くことを禁止する。
- **writing-plans** — 合意した設計を 2-5 分単位の小さなタスクに分割。各タスクには変更ファイルのパス、コード内容、確認方法を含める。

### 実装

- **executing-plans** — 実装計画をチェックポイントを挟みながらバッチ実行する。人間の確認を挟みながら進める。
- **subagent-driven-development** — タスクごとに**フレッシュなサブエージェント**を起動し、2段階レビュー（仕様準拠 → コード品質）を実施。サブエージェントは親セッションの履歴を継承せず、必要な情報だけを正確に注入する。これにより、エージェントが数時間単位で自律的に作業を継続できる。
- **dispatching-parallel-agents** — 複数のサブエージェントを並列で動作させる。

### テスト

- **test-driven-development** — RED（失敗テストを書く）→ GREEN（最小限のコードで通す）→ REFACTOR のサイクルを強制。テストより先に実装コードを書くことを禁止する。テストのアンチパターン集も含まれる。

### デバッグ

- **systematic-debugging** — バグ遭遇時に4フェーズで原因究明を進める：
  1. **根本原因の調査**: エラーメッセージの精読、再現条件の特定、最近の変更の確認
  2. **パターン分析**: 類似問題の有無、共通原因の確認
  3. **仮説の立案と検証**: 検証可能な仮説を立てて確認
  4. **修正の実装**: 根本原因に対する修正のみを行う

  **Core principle:** 「原因究明が終わるまで修正に手を出してはいけない。対症療法は失敗である。」

- **verification-before-completion** — 「完了した」と宣言する前に検証コマンドを実行し、証拠を示すまで完了宣言を禁止する。「主張するなら必ず証拠を示せ」。

### コードレビュー

- **requesting-code-review** — コードレビューを依頼する前のチェックリストを自動実行。Critical な問題は進行をブロックする。
- **receiving-code-review** — レビュー指摘への対応を整理する。

### Git 運用

- **using-git-worktrees** — 独立した git worktree を作成し、クリーンな状態で開発を開始。既存のブランチに影響を与えず、プロジェクトのセットアップとテストのベースライン確認を自動実行する。
- **finishing-a-development-branch** — 作業終了時にテストを検証し、マージ/PR化/ブランチ維持/破棄の判断を行い、worktree を後片付けする。

### メタ

- **writing-skills** — 独自スキルを正しく作るためのガイド。設計手順、記述方法、テスト手順を体系的に説明。
- **using-superpowers** — Superpowers 自体の使い方を学ぶチュートリアルスキル。

## 哲学

Superpowers は以下の原則に基づいて設計されています：

| 原則 | 内容 |
|------|------|
| **Test-Driven Development** | 常にテストを先に書く |
| **Systematic over ad-hoc** | 当てずっぽうではなくプロセスに従う |
| **Complexity reduction** | シンプルさを最優先する |
| **Evidence over claims** | 完了を宣言する前に検証する |

## 自動起動の仕組み

Superpowers の最大の特徴は、スキルが**状況に応じて自動的に起動する**点です。

```
「この機能を実装して」
    ↓ 自動
brainstorming が起動 → 設計を確認
    ↓ 承認後
writing-plans が起動 → タスク分割
    ↓
subagent-driven-development が自動実行
```

明示的に `/brainstorming` のようにスラッシュコマンドで呼び出すことも可能ですが、基本的にはエージェントが自律的に判断して適切なスキルを起動します。毎回指示しなくても、エージェントが段取りを踏んでくれる設計です。

## GitHub Copilot Skills との関係

Superpowers の「スキル」は、GitHub Copilot の Agent Skills と概念的には似ていますが、以下の違いがあります：

| 観点 | Superpowers | GitHub Copilot Skills |
|------|------------|----------------------|
| **目的** | 開発プロセス全体の方法論 | 特定タスクの能力拡張 |
| **起動方法** | 状況に応じて**自動起動** | ユーザーが**明示的に呼び出す**（`@skill-name`） |
| **カバー範囲** | 設計→実装→テスト→デバッグ→レビュー→git運用 | コードレビュー、Issue分析、改善提案など |
| **設定場所** | プラグインとしてインストール | `.github/skills/` に SKILL.md を配置 |

両者は「スキルによってエージェントに能力を追加する」という点で共通しており、Superpowers の**設計原則（1スキル1能力、明確な入出力、段階的拡張、組み合わせ可能性）** は、GitHub Copilot のスキル開発にも応用できます。

## このチュートリアルでの位置づけ

本チュートリアルは GitHub Copilot の Agent Skills に焦点を当てていますが、Superpowers は以下の点で参考になります：

1. **スキル設計のベストプラクティス** — 各スキルの SKILL.md は、高品質なスキル定義の実例として学びがある
2. **開発プロセスの自動化思想** — エージェントに「考えさせる」プロセス設計は、Copilot のスキル作成にも応用可能
3. **スキル間の連携パイプライン** — 複数スキルをチェーンさせる設計は、本チュートリアルの Part 5（パイプライン連携）の参考になる

> 📖 参考: [obra/superpowers README](https://github.com/obra/superpowers) | [Release Announcement](https://blog.fsck.com/2025/10/09/superpowers/) | [Claude Plugin Marketplace](https://claude.com/plugins/superpowers)

## 次のステップ

→ [3-2: gstack: Garry Tan の Claude Code スキルセット](02-gstack-overview.md)
