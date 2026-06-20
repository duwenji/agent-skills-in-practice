# GLOSSARY — 用語集

教材全体で使われる用語を洗い出し、用語種を付けて整理しました。

## 用語種の凡例

| 用語種 | 説明 |
|--------|------|
| ツール名 | AIエージェント・CLI・IDEなどの製品・ツール名 |
| スキル名 | SKILL.md として定義された個別スキルの名称 |
| コマンド | スラッシュコマンド・CLI コマンド・呼び出し構文 |
| ファイル/パス | ファイル名・拡張子・ディレクトリパス |
| 概念 | Agent Skills エコシステムの抽象的な概念 |
| フレームワーク | 開発方法論・スキルセットとしてのフレームワーク |
| 技術規格 | ファイルフォーマット・業界標準・プロトコル |
| 設計原則 | スキル設計・エージェント運用における原則 |
| 評価・品質 | スキルの評価・品質管理に関する概念 |

---

## ツール名

| 用語 | 用語種 | 説明 | 参照 |
|------|--------|------|------|
| Claude Code | ツール名 | Anthropic が提供するAIコーディングエージェント（CLI） | docs/00-fundamentals/01-ecosystem-overview.md |
| GitHub Copilot | ツール名 | GitHub/Microsoft が提供するAIコーディングアシスタント | docs/00-fundamentals/01-ecosystem-overview.md |
| Copilot Editor | ツール名 | GitHub.com 上のチャットインターフェース（スキル検索に使用） | docs/02-discovery/01-find-skills.md |
| Find Skills | ツール名 | GitHub.com 上で公開スキルを検索・発見する機能 | docs/02-discovery/01-find-skills.md |
| skill.sh | ツール名 | ターミナル上でスキルをクロスプラットフォーム検索するCLIツール | docs/02-discovery/02-skill-sh-cli.md |
| gh CLI | ツール名 | GitHub 公式CLI。`gh skill` サブコマンドでスキル検索が可能 | docs/02-discovery/01-find-skills.md |
| VS Code | ツール名 | Microsoft の統合開発環境。統合ターミナル経由でCLIエージェントを利用可能 | docs/03-frameworks/01-superpowers.md |

---

## スキル名 — バンドルスキル（Claude Code 標準搭載）

| 用語 | 用語種 | 説明 | 参照 |
|------|--------|------|------|
| skill-creator | スキル名 | スキル開発のライフサイクル全体をカバーするフレームワーク。Claude Code 標準バンドル | docs/01-skill-creation/02-skill-creator-hands-on.md |

---

## スキル名 — Superpowers スキル群

| 用語 | 用語種 | 説明 | 参照 |
|------|--------|------|------|
| brainstorming | スキル名 | 実装前に要件・設計をソクラテス式対話で整理する。HARD-GATE で設計承認なしの実装を禁止 | docs/03-frameworks/01-superpowers.md |
| writing-plans | スキル名 | 合意した設計を 2〜5 分単位の小タスクに分割し、実装計画を作成する | docs/03-frameworks/01-superpowers.md |
| executing-plans | スキル名 | 実装計画をチェックポイントを挟みながらバッチ実行する | docs/03-frameworks/01-superpowers.md |
| subagent-driven-development | スキル名 | タスクごとにフレッシュなサブエージェントを起動して2段階レビューを実施する | docs/03-frameworks/01-superpowers.md |
| dispatching-parallel-agents | スキル名 | 複数のサブエージェントを並列で動作させる | docs/03-frameworks/01-superpowers.md |
| test-driven-development | スキル名 | RED→GREEN→REFACTOR のTDDサイクルを強制。テストより先に実装コードを書くことを禁止 | docs/03-frameworks/01-superpowers.md |
| systematic-debugging | スキル名 | バグを4フェーズ（根本原因調査・パターン分析・仮説検証・修正）で究明するデバッグスキル | docs/03-frameworks/01-superpowers.md |
| verification-before-completion | スキル名 | 「完了」宣言前に検証コマンドを実行し証拠を示すまで完了宣言を禁止する | docs/03-frameworks/01-superpowers.md |
| requesting-code-review | スキル名 | コードレビュー依頼前のチェックリストを自動実行。Critical な問題は進行をブロック | docs/03-frameworks/01-superpowers.md |
| receiving-code-review | スキル名 | レビュー指摘への対応を整理する | docs/03-frameworks/01-superpowers.md |
| using-git-worktrees | スキル名 | 独立した git worktree を作成し、クリーンな状態で開発を開始する | docs/03-frameworks/01-superpowers.md |
| finishing-a-development-branch | スキル名 | 作業終了時にテスト検証し、マージ/PR化/ブランチ維持/破棄を判断して worktree を後片付けする | docs/03-frameworks/01-superpowers.md |
| writing-skills | スキル名 | 独自スキルを正しく作るための設計・記述・テストを体系的に説明するガイド | docs/03-frameworks/01-superpowers.md |
| using-superpowers | スキル名 | Superpowers 自体の使い方を学ぶチュートリアルスキル | docs/03-frameworks/01-superpowers.md |

---

## スキル名 — 実践スキル（本教材メインコンテンツ）

| 用語 | 用語種 | 説明 | 参照 |
|------|--------|------|------|
| grill-me | スキル名 | コードを「可読性・パフォーマンス・セキュリティ・保守性」の4軸でレビューする | docs/04-skills-in-practice/01-grill-me.md |
| triage | スキル名 | GitHub Issue を解析し、優先度（P0〜P3）の判定・カテゴリ分類・対応推奨事項を自動生成する | docs/04-skills-in-practice/02-triage-issue-analysis.md |
| improve | スキル名 | コードのパフォーマンス最適化・リファクタリング・モダナイゼーションの改善提案を行う | docs/04-skills-in-practice/03-improve.md |
| frontend-design | スキル名 | フロントエンドのコンポーネント分割・状態管理・データフローをガイドする設計支援スキル | docs/04-skills-in-practice/04-frontend-design.md |
| ui-ux-pro-max | スキル名 | アクセシビリティ・視認性・操作性を多角的に監査する UI/UX 改善スキル | docs/04-skills-in-practice/05-ui-ux-pro-max.md |
| baoyu-diagram | スキル名 | アーキテクチャ図・フロー図をSVGで生成する図解スキル（JimLiu/baoyu-skills） | docs/04-skills-in-practice/06-baoyu-diagram.md |
| baoyu-infographic | スキル名 | データや概念を 21レイアウト×17スタイル のインフォグラフィックで整理するスキル | docs/04-skills-in-practice/07-baoyu-infographic.md |
| baoyu-comic | スキル名 | 技術概念をコミック形式でわかりやすく伝えるコンテンツ制作スキル | docs/04-skills-in-practice/08-baoyu-comic.md |

---

## スキル名 — gstack スキル群

| 用語 | 用語種 | 説明 | 参照 |
|------|--------|------|------|
| office-hours | スキル名 | YCオフィスアワー形式。6つの強制質問でプロダクトを再定義する gstack エントリーポイント | docs/03-frameworks/02-gstack-overview.md |
| plan-ceo-review | スキル名 | CEO視点で計画をレビュー。Expansion/Selective/Hold/Reduction の4モード | docs/03-frameworks/02-gstack-overview.md |
| plan-eng-review | スキル名 | EM（エンジニアリングマネージャー）視点で技術的実現可能性を確認する | docs/03-frameworks/02-gstack-overview.md |
| plan-design-review | スキル名 | デザイナー視点で計画をレビューする | docs/03-frameworks/02-gstack-overview.md |
| autoplan | スキル名 | 自動計画作成スキル | docs/03-frameworks/02-gstack-overview.md |
| design-shotgun | スキル名 | 4〜6種類のUIモックアップを生成してブラウザで比較できるようにする | docs/03-frameworks/02-gstack-overview.md |
| design-html | スキル名 | モックアップを本番品質のHTML（Pretextレイアウト）に変換する | docs/03-frameworks/02-gstack-overview.md |
| spec | スキル名 | 仕様書を生成するスキル | docs/03-frameworks/02-gstack-overview.md |
| review | スキル名 | CIでは見つからない本番環境で壊れるバグを発見するコードレビュースキル | docs/03-frameworks/02-gstack-overview.md |
| investigate | スキル名 | 問題の原因調査・デバッグを行うスキル | docs/03-frameworks/02-gstack-overview.md |
| codex | スキル名 | セカンドオピニオンを提供するスキル | docs/03-frameworks/02-gstack-overview.md |
| qa | スキル名 | 実際のブラウザを起動してアプリをテストし、バグ発見から回帰テスト生成まで行う | docs/03-frameworks/02-gstack-overview.md |
| browse | スキル名 | ブラウザを操作してWebアプリを検証するスキル | docs/03-frameworks/02-gstack-overview.md |
| benchmark | スキル名 | パフォーマンス計測を行うスキル | docs/03-frameworks/02-gstack-overview.md |
| cso | スキル名 | セキュリティ監査を行うスキル（Chief Security Officer 役） | docs/03-frameworks/02-gstack-overview.md |
| ship | スキル名 | 全チェックリスト確認後にマージを実行するリリーススキル | docs/03-frameworks/02-gstack-overview.md |
| land-and-deploy | スキル名 | マージからデプロイまでを担うスキル | docs/03-frameworks/02-gstack-overview.md |
| canary | スキル名 | カナリアリリースと本番監視を行うスキル | docs/03-frameworks/02-gstack-overview.md |
| retro | スキル名 | スプリント振り返りを行うスキル | docs/03-frameworks/02-gstack-overview.md |
| learn | スキル名 | ナレッジを蓄積するスキル | docs/03-frameworks/02-gstack-overview.md |
| document-release | スキル名 | リリースドキュメントを更新するスキル | docs/03-frameworks/02-gstack-overview.md |
| careful | スキル名 | 破壊的コマンドの前に警告を出すセーフティスキル | docs/03-frameworks/02-gstack-overview.md |
| freeze | スキル名 | 編集範囲を特定ディレクトリに制限するスキル | docs/03-frameworks/02-gstack-overview.md |
| guard | スキル名 | `/careful` と `/freeze` を同時有効化する複合セーフティスキル | docs/03-frameworks/02-gstack-overview.md |
| pair-agent | スキル名 | マルチエージェント連携を行うパワーツール | docs/03-frameworks/02-gstack-overview.md |

---

## コマンド

| 用語 | 用語種 | 説明 | 参照 |
|------|--------|------|------|
| `/skill-creator` | コマンド | Claude Code でスキル生成フレームワークを起動するスラッシュコマンド | docs/01-skill-creation/02-skill-creator-hands-on.md |
| `/plugin install` | コマンド | Claude Code にプラグインをインストールするコマンド | docs/03-frameworks/01-superpowers.md |
| `/reload-plugins` | コマンド | Claude Code のプラグインをリロードするコマンド | docs/03-frameworks/01-superpowers.md |
| `/plugin list` | コマンド | インストール済みプラグインの一覧を表示するコマンド | docs/03-frameworks/01-superpowers.md |
| `gh skill` | コマンド | GitHub CLI でスキルを検索・操作するサブコマンド | docs/02-discovery/01-find-skills.md |
| `@skill-name` | コマンド | GitHub Copilot チャット上でスキルを明示的に呼び出す構文 | docs/03-frameworks/01-superpowers.md |
| `@copilot` | コマンド | GitHub Copilot Editor でのチャット宛先指定構文 | docs/02-discovery/01-find-skills.md |
| `!` (バング構文) | コマンド | SKILL.md 内でコマンドを実行し、その出力をインライン展開する動的コンテキスト注入構文（Claude Code 専用） | docs/01-skill-creation/03-skillmd-customization.md |

---

## ファイル/パス

| 用語 | 用語種 | 説明 | 参照 |
|------|--------|------|------|
| SKILL.md | ファイル/パス | スキルの指示・手順・説明を記述するメインファイル。YAMLフロントマター＋Markdown本文の2部構成 | docs/01-skill-creation/01-what-are-agent-skills.md |
| `.claude/skills/<name>/SKILL.md` | ファイル/パス | Claude Code のプロジェクト用スキル配置パス | docs/01-skill-creation/01-what-are-agent-skills.md |
| `.github/skills/<name>/SKILL.md` | ファイル/パス | GitHub Copilot のプロジェクト用スキル配置パス | docs/01-skill-creation/01-what-are-agent-skills.md |
| `~/.claude/skills/<name>/SKILL.md` | ファイル/パス | Claude Code の個人用スキル配置パス（全プロジェクトに適用） | docs/01-skill-creation/01-what-are-agent-skills.md |
| `~/.copilot/skills/<name>/SKILL.md` | ファイル/パス | GitHub Copilot の個人用スキル配置パス | docs/01-skill-creation/01-what-are-agent-skills.md |
| `~/.claude/settings.json` | ファイル/パス | Claude Code の設定ファイル。`enabledPlugins` などを管理 | docs/03-frameworks/01-superpowers.md |
| `.skill` | ファイル/パス | スキルの配布用パッケージファイル形式。`skill-creator` の最終出力 | docs/06-advanced/04-skill-creator-deep-dive.md |
| CLAUDE.md | ファイル/パス | Claude Code のプロジェクト設定ファイル | docs/03-frameworks/02-gstack-overview.md |

---

## 概念

| 用語 | 用語種 | 説明 | 参照 |
|------|--------|------|------|
| Agent Skills | 概念 | AIエージェント（Claude Code・GitHub Copilot 等）に特定タスクを実行させるための指示書 | docs/01-skill-creation/01-what-are-agent-skills.md |
| Agent Skills オープンスタンダード | 概念 | 複数のAIツール間でスキルを共有するための共通フォーマット規格（agentskills.io） | docs/00-fundamentals/01-ecosystem-overview.md |
| バンドルスキル | 概念 | Claude Code に標準搭載されているスキル（`/skill-creator`、`/code-review` 等） | docs/01-skill-creation/01-what-are-agent-skills.md |
| 自動読み込み | 概念 | 会話の内容がスキルの `description` にマッチした場合にエージェントがスキルを自動的に読み込む機能 | docs/01-skill-creation/01-what-are-agent-skills.md |
| 明示的な呼び出し | 概念 | ユーザーが `/スキル名` でスキルを直接実行する操作 | docs/01-skill-creation/01-what-are-agent-skills.md |
| クロスプラットフォーム | 概念 | Claude Code と GitHub Copilot の両方で同じスキル（SKILL.md）が動作すること | docs/01-skill-creation/01-what-are-agent-skills.md |
| 動的コンテキスト注入 | 概念 | `!` 構文で SKILL.md 内にコマンド出力をインライン展開する機能（Claude Code 専用） | docs/01-skill-creation/03-skillmd-customization.md |
| 呼び出し制御（invoke） | 概念 | フロントマターの `invoke` フィールドでスキルを誰が呼び出せるかを制御する設定（`user` / `auto` / `both`） | docs/01-skill-creation/03-skillmd-customization.md |
| ツール事前承認（approved_tools） | 概念 | フロントマターの `approved_tools` フィールドで、スキルが使用するツールをユーザー確認不要とする設定 | docs/01-skill-creation/03-skillmd-customization.md |
| フロントマター | 概念 | SKILL.md の先頭にある `---` で囲まれた YAML 形式のメタデータ部分。`name`・`description`・`invoke` 等を記述 | docs/01-skill-creation/01-what-are-agent-skills.md |
| プラグイン | 概念 | エージェントに追加機能を提供する拡張モジュール。Superpowers は Claude Code のプラグインとして提供される | docs/03-frameworks/01-superpowers.md |
| Plugin Marketplace | 概念 | プラグインを配布・インストールするための公式ストア | docs/03-frameworks/01-superpowers.md |
| Worktree（git worktree） | 概念 | 同じリポジトリから独立した作業ディレクトリを複数作成できる Git の機能。Superpowers がクリーン開発環境の確保に利用 | docs/03-frameworks/01-superpowers.md |
| HARD-GATE | 概念 | Superpowers スキル内の強制ゲート。設計承認など特定条件を満たすまで次のアクション（コードを書くなど）を禁止する | docs/03-frameworks/01-superpowers.md |
| サブエージェント | 概念 | メインエージェントから起動される子エージェント。独立したコンテキストを持ち、親セッションの履歴を継承しない | docs/03-frameworks/01-superpowers.md |
| スキルパイプライン | 概念 | 複数のスキルを連携させたワークフロー。シーケンシャル・パラレル・条件分岐の3パターンがある | docs/06-advanced/01-pipeline-integration.md |
| シーケンシャルパターン | 概念 | スキルA→B→C と前のスキルの出力を次のスキルの入力に使う直列パイプライン | docs/06-advanced/01-pipeline-integration.md |
| パラレルパターン | 概念 | 1つの入力に対して複数のスキルを同時実行する並列パイプライン | docs/06-advanced/01-pipeline-integration.md |
| 条件分岐パターン | 概念 | スキルの出力に応じて次に実行するスキルを切り替えるパイプライン | docs/06-advanced/01-pipeline-integration.md |
| with-skill | 概念 | skill-creator の評価フェーズにおけるスキルあり実行。baseline と比較して品質向上を定量評価する | docs/06-advanced/04-skill-creator-deep-dive.md |
| baseline | 概念 | skill-creator の評価フェーズにおけるスキルなし実行。with-skill との比較対象 | docs/06-advanced/04-skill-creator-deep-dive.md |
| 評価ビューア | 概念 | skill-creator のベンチマーク結果をブラウザで確認する画面。Outputs タブと Benchmark タブを持つ | docs/06-advanced/04-skill-creator-deep-dive.md |
| トリガー精度 | 概念 | `description` がスキル自動読み込みを正確に判断できる度合い | docs/06-advanced/04-skill-creator-deep-dive.md |
| Description 最適化 | 概念 | 20個のトリガーテストクエリを使って、スキル自動読み込み精度を最大化するよう `description` を自動改善するプロセス | docs/06-advanced/04-skill-creator-deep-dive.md |
| 反復改善サイクル | 概念 | スキル作成→テスト実行→結果確認→改善のループ。3〜5回の繰り返しを想定する | docs/01-skill-creation/04-best-practices.md |
| 仮想チーム | 概念 | gstack が実現するAIによる役割分担体制。1人のAIに全役割を任せず、役割ごとに専門スキルを割り当てる | docs/03-frameworks/02-gstack-overview.md |
| スプリント | 概念 | gstack が想定する開発サイクル：Think→Plan→Build→Review→Test→Ship→Reflect | docs/03-frameworks/02-gstack-overview.md |
| 前端大神問題 | 概念 | フロントエンドAIコード生成における3つの代表的な課題。概念層のスタート地点として参照される | docs/00-fundamentals/01-ecosystem-overview.md |
| 4層構造 | 概念 | 本教材の構成：発見層・作成層・概念層・実践層 | docs/00-fundamentals/01-ecosystem-overview.md |
| 発見層 | 概念 | Find Skills / gh skill / skill.sh でスキルを探し・見つけ・実行する層 | docs/00-fundamentals/01-ecosystem-overview.md |
| 作成層 | 概念 | Claude Code `/skill-creator` または手書き SKILL.md でスキルを作成する層 | docs/00-fundamentals/01-ecosystem-overview.md |
| 概念層 | 概念 | Superpowers / GStack / 前端大神問題を通じて理論・フレームワークを理解する層 | docs/00-fundamentals/01-ecosystem-overview.md |
| 実践層 | 概念 | grill-me / triage / improve / frontend-design / ui-ux-pro-max 等の実践スキルを使いこなす層 | docs/00-fundamentals/01-ecosystem-overview.md |
| 応用層 | 概念 | コンテンツ生成パイプライン・画像生成バックエンド・カスタムスキル開発の層 | docs/00-fundamentals/01-ecosystem-overview.md |

---

## フレームワーク

| 用語 | 用語種 | 説明 | 参照 |
|------|--------|------|------|
| Superpowers | フレームワーク | Jesse Vincent（Prime Radiant）が開発したコーディングエージェント向け開発方法論プラグイン。インストールだけでエージェントに「段取り」を習得させる | docs/03-frameworks/01-superpowers.md |
| gstack | フレームワーク | Garry Tan（Y Combinator）が開発した Claude Code 向けのオープンソーススキルセット。AIを「仮想エンジニアリングチーム」として運用する（23専門家ロール＋8パワーツール） | docs/03-frameworks/02-gstack-overview.md |
| TDD（Test-Driven Development） | フレームワーク | テスト駆動開発。テストを先に書いてから実装コードを書く開発手法 | docs/03-frameworks/01-superpowers.md |
| RED-GREEN-REFACTOR | フレームワーク | TDDの3フェーズサイクル。RED（失敗テストを書く）→GREEN（最小限のコードで通す）→REFACTOR（コードを整理する） | docs/03-frameworks/01-superpowers.md |

---

## 技術規格

| 用語 | 用語種 | 説明 | 参照 |
|------|--------|------|------|
| agentskills.io | 技術規格 | Agent Skills オープンスタンダードの公式サイト・規格の起点 | docs/01-skill-creation/01-what-are-agent-skills.md |
| YAML | 技術規格 | SKILL.md フロントマターに使用するデータ記述言語 | docs/01-skill-creation/01-what-are-agent-skills.md |
| Markdown | 技術規格 | SKILL.md 本文に使用するテキストマークアップ言語 | docs/01-skill-creation/01-what-are-agent-skills.md |
| JSON | 技術規格 | スキル出力フォーマットや設定ファイルに使用するデータ交換形式 | docs/01-skill-creation/02-skill-creator-hands-on.md |
| SVG | 技術規格 | baoyu-diagram が生成するスケーラブルベクターグラフィクス形式。コード生成で図を作るアプローチに使用 | docs/04-skills-in-practice/06-baoyu-diagram.md |
| WCAG | 技術規格 | Web Content Accessibility Guidelines。ui-ux-pro-max スキルのアクセシビリティチェック基準 | docs/04-skills-in-practice/09-problem-skill-mapping.md |
| P0〜P3 | 技術規格 | triage スキルの優先度分類。P0：即時対応 / P1：高優先 / P2：通常 / P3：低優先 | docs/04-skills-in-practice/02-triage-issue-analysis.md |
| Git submodule | 技術規格 | スキルリポジトリを別リポジトリのサブモジュールとして追加する Git の機能 | docs/02-discovery/01-find-skills.md |

---

## 設計原則

| 用語 | 用語種 | 説明 | 参照 |
|------|--------|------|------|
| 単一責任の原則 | 設計原則 | 1つのスキルは1つのことを得意とする設計。「コードレビュー＋テスト生成＋ドキュメント作成」を1スキルにまとめない | docs/01-skill-creation/04-best-practices.md |
| 段階的拡張 | 設計原則 | シンプルに作ってから必要に応じて機能を追加する。最初から完璧を目指さない | docs/01-skill-creation/04-best-practices.md |
| Evidence over claims | 設計原則 | 完了を宣言する前に必ず検証コマンドを実行して証拠を示す（Superpowers の哲学） | docs/03-frameworks/01-superpowers.md |
| Systematic over ad-hoc | 設計原則 | 当てずっぽうではなくプロセスに従う（Superpowers の哲学） | docs/03-frameworks/01-superpowers.md |
| Complexity reduction | 設計原則 | シンプルさを最優先する（Superpowers の哲学） | docs/03-frameworks/01-superpowers.md |
| 明確な契約 | 設計原則 | 利用者が「何を渡せば、何が返ってくるか」を一目で理解できるよう入出力を明確に定義する | docs/01-skill-creation/04-best-practices.md |
| プラットフォーム互換性 | 設計原則 | 可能な限り Claude Code と GitHub Copilot の両方で動作するよう設計し、プラットフォーム固有機能への過度な依存を避ける | docs/01-skill-creation/04-best-practices.md |

---

## 評価・品質

| 用語 | 用語種 | 説明 | 参照 |
|------|--------|------|------|
| 定量的アサーション | 評価・品質 | skill-creator の評価フェーズで使う、数値ベースの合格/不合格判定 | docs/06-advanced/04-skill-creator-deep-dive.md |
| 定性的レビュー | 評価・品質 | スキル評価フェーズで行う人間によるレビュー | docs/06-advanced/04-skill-creator-deep-dive.md |
| テストケース | 評価・品質 | スキルの動作を確認するための入力例。skill-creator は 2〜3 個を自動生成する | docs/06-advanced/04-skill-creator-deep-dive.md |
| エッジケース | 評価・品質 | 境界条件・例外条件のテストケース。通常の正常系とは別に設計する | docs/06-advanced/04-skill-creator-deep-dive.md |
| ベンチマーク | 評価・品質 | with-skill と baseline の比較評価。評価ビューアの Benchmark タブで確認できる | docs/06-advanced/04-skill-creator-deep-dive.md |
| トリガーテストクエリ | 評価・品質 | Description 最適化で使う 20 個のテスト入力（発動すべきケース 8〜10 件＋発動すべきでないケース 8〜10 件） | docs/06-advanced/04-skill-creator-deep-dive.md |
