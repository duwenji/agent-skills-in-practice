# 02-gstack-overview.md リストラクチャリング 実装計画

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** `docs/03-frameworks/02-gstack-overview.md` を物語構造に再構成し、初心者・中級者が冒頭から「AIに全役割を任せることの問題への答えだ」と感じながら読み進められるようにする。

**Architecture:** 新規①②③セクション（共感フック・解決策・Before/After）を冒頭に追加し、既存コンテンツを再配置。Mermaid 図3つを1つに削減（比較表で代替）。情報削除はゼロ。

**Tech Stack:** Markdown のみ（コードなし）

## Global Constraints

- 対象ファイルは `docs/03-frameworks/02-gstack-overview.md` 1ファイルのみ
- 削除してよい要素：現行「背景：単一AIアシスタント問題」セクション全体（①の具体的シーンで代替）、Mermaid gstack 構造ノード図、Mermaid スプリント比較 LR グラフ
- 保持必須：インストールコマンド全て・全スキル一覧テーブル・主要スキル詳細・比較表・Mermaid シーケンス図（起動方式）・VS Code ASCII 図・マルチエージェント対応テーブル・設計の教訓5項目・次のステップリンク
- Garry Tan 実績テーブルは②セクション内に移動（独立セクションとしては削除）
- 他のドキュメントファイルへの変更は行わない

---

### Task 1: ドキュメント全体を新構成で書き直す

**Files:**
- Modify: `docs/03-frameworks/02-gstack-overview.md`

**Interfaces:**
- Consumes: なし（単体ファイル）
- Produces: 新構成の `docs/03-frameworks/02-gstack-overview.md`

- [ ] **Step 1: 現在のファイルの保持すべき要素を確認する**

  以下が全て存在することを確認してから作業を開始する：
  - 30秒クイックスタートの `git clone` コマンド
  - チームモードの `./setup --team` コマンド
  - VS Code の ASCII 図（`┌─────...`）
  - マルチエージェント対応テーブル（8エージェント）
  - 全スキル一覧テーブル（7フェーズ）
  - 主要スキル詳細（/office-hours, /plan-ceo-review, /review, /qa, /careful, /design-shotgun）
  - Mermaid シーケンス図（起動方式の違い）
  - 比較表（8行）
  - 設計の教訓5項目
  - 次のステップリンク（03-3a-frontend-design.md, 03-3b-ui-ux-pro-max.md）

- [ ] **Step 2: ファイルを新構成で上書き書き込む**

  以下の内容で `docs/03-frameworks/02-gstack-overview.md` を上書きする：

  ````markdown
  # 3-2: gstack — Garry Tan の Claude Code スキルセット

  > **学習時間**: 15分 | **難易度**: ⭐⭐

  ## AIに「全部やって」と頼んでいませんか？

  エージェントを使い始めると、こんな状況に気づきます。

  ---

  **シーン1：AIが自分のコードを自分でレビューした**

  > 「このコードをレビューして」

  エージェントは丁寧にレビューしました。「問題ありません、よく書けています」。
  でもそのコードを書いたのも同じAIです。
  設計の意図も、妥協の経緯も、全部知っている「本人」が審査しています。

  ---

  **シーン2：「なぜこうなったのか」が誰にもわからない**

  > 「この機能を設計して、実装して」

  AIは設計し、実装しました。でも1週間後に仕様が変わったとき、
  「なぜこのアーキテクチャを選んだのか」を説明できるものが何もありませんでした。
  設計者と実装者が同一人物だったからです。

  ---

  **シーン3：QAもセキュリティも「自己申告」だった**

  > 「テストして、問題なければリリースして」

  AIは「テスト済み、問題なし」と報告しました。
  でも本番環境に出すと、SQLインジェクションの脆弱性が見つかりました。
  セキュリティの観点で見るAIと、コードを書いたAIが同じだったのです。

  ---

  これは「AIが賢くない」のではありません。
  **1人の人間に、設計者・実装者・QA・セキュリティ監査を同時に兼任させているのが問題です。**
  人間のチームでは当然やる「役割分担」が、エージェントには存在しないのです。

  ## gstack — AIエージェントを「仮想チーム」に変える

  **gstack** は、Y Combinator の President & CEO **Garry Tan** が開発した
  **Claude Code 向けのオープンソーススキルセット**です。

  - **リポジトリ**: [github.com/garrytan/gstack](https://github.com/garrytan/gstack)
  - **ライセンス**: MIT
  - **スター数**: 109,000+（2026年6月時点）
  - **構成**: 23の専門家ロールスキル + 8のパワーツール

  gstack のアイデアはシンプルです。
  1人のAIに全役割を任せるのではなく、**役割ごとに専門のスキルを用意する**。

  ```
  /office-hours      → 今日のCEO役：「本当にそれを作るべきか？」
  /plan-eng-review   → 今日のEM役：「技術的に実現可能か？」
  /qa                → 今日のQAリード役：「本当に動いているか？」
  /cso               → 今日のセキュリティ担当役：「脆弱性はないか？」
  ```

  これにより Claude Code が「1人のアシスタント」から
  「**CEO・エンジニアリングマネージャー・QAリード・セキュリティオフィサーを擁する仮想エンジニアリングチーム**」に変わります。

  ### Garry Tan の実績

  Garry Tan は YC の CEO としてフルタイムで働きながら、gstack を使って60日間で以下の成果を上げています：

  | 指標 | 数値 |
  |------|------|
  | **期間** | 60日間 |
  | **出荷したプロダクションサービス** | 3 |
  | **出荷した機能** | 40+ |
  | **論理コード生産量（2013年比）** | **810倍** |
  | **2026年の貢献数** | 1,237（2026年4月時点） |
  | **総コード行数** | 600K+ 行 |
  | **テストカバレッジ向上** | 35% |

  > 「LOC（コード行数）批判は、AIで行数が水増しされるという点では間違っていない。しかし、インフレ調整後の生産性が落ちているという点では間違っている。私は**大幅に**生産性が上がっている。」 — Garry Tan

  > 「私は2013年12月以来、おそらく一行もコードをタイプしていない。これは極めて大きな変化だ」 — Andrej Karpathy（OpenAI共同創業者）

  ## 同じ依頼で何が変わるのか

  ### Before：gstack なし

  ```
  $ claude "毎日のカレンダーブリーフィングアプリを作りたい"

  Claude: わかりました。実装します。
  [設計の確認なし、代替案の提示なし、すぐに実装開始]
  ... 2時間後 ...
  Claude: 実装が完了しました！
  $ # → 「それはパーソナルチーフオブスタッフAIでは？」
    # → 「通知機能は？音声読み上げは？ユーザーが本当に欲しいものは？」
    # → 誰も聞かなかった。
  ```

  ### After：gstack あり

  ```
  $ /office-hours
  Claude（CEO役）: 「毎日のカレンダーブリーフィングアプリ」と言いましたが、
                   実際にあなたが説明したのは「パーソナルチーフオブスタッフAI」です。

                   6つの質問に答えてください：
                   1. 誰のためのツールですか？（あなた個人？チーム？）
                   2. 一番の「痛み」は何ですか？
                   ...
                   [隠れた要件を抽出、前提に挑戦、3つの実装アプローチを工数付きで提案]
                   → 設計ドキュメントを自動生成

  $ /plan-eng-review
  Claude（EM役）: 技術的な実現可能性を確認します。
                 APIレート制限とコスト試算を見てください...

  $ /qa
  Claude（QAリード役）: 実際のブラウザでテストします。
                       バグを1件発見。アトミックコミットで修正します...

  $ /ship
  Claude（リリースエンジニア役）: 全チェックリストを確認。マージします。✅
  ```

  役割が分かれると、**それぞれの専門家が本来の仕事をする**ようになります。

  ## スプリントの流れ

  gstack はスプリントの流れに沿って設計されています：

  ```
  Think → Plan → Build → Review → Test → Ship → Reflect
  ```

  各スキルは前のスキルの出力を次のスキルが読み取る形で連携します。`/office-hours` が設計ドキュメントを書き、`/plan-ceo-review` がそれを読み、`/review` がバグを検出し、`/ship` が修正を確認します。

  ## 全スキル一覧（概要）

  > 必要なときに参照してください。最初から全部覚える必要はありません。

  gstack は **23の専門家ロールスキル + 8のパワーツール** で構成されています。スプリントの流れに沿って以下のフェーズに分類されます：

  | フェーズ | 主要スキル | 役割 |
  |---------|-----------|------|
  | **Think** | `/office-hours` | YC オフィスアワー — 6つの強制質問でプロダクトを再定義 |
  | **Plan** | `/plan-ceo-review`, `/plan-eng-review`, `/plan-design-review`, `/autoplan` | CEO/EM/デザイナーによる多層レビュー |
  | **Build** | `/design-shotgun`, `/design-html`, `/spec` | モックアップ生成→本番HTML変換 |
  | **Review** | `/review`, `/investigate`, `/codex` | スタッフエンジニアレビュー、デバッグ、セカンドオピニオン |
  | **Test** | `/qa`, `/browse`, `/benchmark`, `/cso` | 実ブラウザQA、パフォーマンス計測、セキュリティ監査 |
  | **Ship** | `/ship`, `/land-and-deploy`, `/canary` | マージ→デプロイ→本番監視 |
  | **Reflect** | `/retro`, `/learn`, `/document-release` | 振り返り、ナレッジ蓄積、ドキュメント更新 |

  **パワーツール**: `/careful`（破壊的コマンド警告）, `/freeze`（編集ロック）, `/guard`（両方）, `/pair-agent`（マルチエージェント連携）

  **iOS スキル**（v1.43.0.0+）: `/ios-qa`, `/ios-fix`, `/ios-design-review`, `/ios-clean`

  > 各スキルの詳細は [github.com/garrytan/gstack](https://github.com/garrytan/gstack) を参照してください。

  ## 主要スキルの詳細

  ### `/office-hours` — YC オフィスアワー

  gstack のエントリーポイント。コードを書く前に「何を作るべきか」を問い直します。

  ```
  あなた: 毎日のカレンダーブリーフィングアプリを作りたい
  Claude: 「『毎日のブリーフィングアプリ』と言いましたが、
          実際にあなたが説明したのはパーソナルチーフオブスタッフAIです」
          [5つの隠れた要件を抽出]
          [4つの前提にチャレンジ]
          [3つの実装アプローチを工数見積もり付きで提案]
          → 設計ドキュメントを自動生成
  ```

  ### `/plan-ceo-review` — CEO レビュー

  プロダクトの視点から計画をレビュー。4つのモードがあります：

  | モード | 説明 |
  |--------|------|
  | **Expansion** | 「もっと大きく考えよう」— リクエストの裏にある10xプロダクトを探す |
  | **Selective Expansion** | 特定の部分だけ拡張 |
  | **Hold Scope** | 現状のスコープを維持 |
  | **Reduction** | 「これは本当に必要か？」— 削れるものを特定 |

  ### `/review` — コードレビュー

  CIでは見つからない本番環境で壊れるバグを発見します。自動修正可能な問題は自動で修正し、判断が必要なものはフラグを立てます。

  ### `/qa` — QA テスト

  実際のブラウザを起動してアプリをテストします。バグを見つけると：
  1. アトミックコミットで修正
  2. 回帰テストを自動生成
  3. 修正を再検証

  ### `/careful` / `/freeze` / `/guard` — セーフティ

  | コマンド | 機能 |
  |---------|------|
  | `be careful` | 破壊的コマンドの前に警告 |
  | `/freeze` | 編集を1ディレクトリに制限 |
  | `/guard` | 両方を同時有効化 |

  ### `/design-shotgun` → `/design-html` — デザインパイプライン

  ```
  あなたのアイデア
      ↓
  /design-shotgun: 4-6種類のモックアップを生成 → ブラウザで比較
      ↓ フィードバック
  /design-shotgun: 改善版を再生成（味覚記憶が学習）
      ↓ 承認
  /design-html: 本番品質のHTMLに変換（Pretextレイアウト）
  ```

  ## インストール方法

  ### 30秒クイックスタート

  Claude Code を開いて以下のコマンドを実行するだけです：

  ```bash
  git clone --single-branch --depth 1 \
    https://github.com/garrytan/gstack.git \
    ~/.claude/skills/gstack \
    && cd ~/.claude/skills/gstack \
    && ./setup
  ```

  **必要条件**: Claude Code, Git, Bun v1.0+, Node.js（Windowsのみ）

  ### チームモード（推奨）

  リポジトリ内で以下のコマンドを実行すると、チーム全員が自動的にgstackを使えるようになります：

  ```bash
  (cd ~/.claude/skills/gstack && ./setup --team) \
    && ~/.claude/skills/gstack/bin/gstack-team-init required \
    && git add .claude/ CLAUDE.md \
    && git commit -m "require gstack for AI-assisted work"
  ```

  ### VS Code での利用について

  gstack は **Claude Code（ターミナル上のCLI）** を主ターゲットとして設計されています。VS Code 上の環境では、以下のように**使える場所と使えない場所**があります：

  ```
  ┌─────────────────────────────────────────────────┐
  │                  VS Code                         │
  │                                                  │
  │  ┌───────────────────┐  ┌───────────────────┐   │
  │  │ チャット画面       │  │ 統合ターミナル     │   │
  │  │ (Ctrl+I)          │  │                    │   │
  │  │                   │  │  $ claude          │   │
  │  │  ❌ gstack非対応   │  │  ───────────────  │   │
  │  │                   │  │  Claude Code起動    │   │
  │  │  @skill-name      │  │  ↓                 │   │
  │  │  (Copilot Skills) │  │  /office-hours ✅  │   │
  │  │  は使える          │  │  /plan-ceo ✅     │   │
  │  └───────────────────┘  │  /review ✅        │   │
  │                          │  /qa ✅            │   │
  │                          │  /ship ✅          │   │
  │                          └───────────────────┘   │
  │                                                  │
  │  ┌───────────────────┐  ┌───────────────────┐   │
  │  │ エージェントモード  │  │ サイドパネル      │   │
  │  │ (Ctrl+Shift+I)    │  │ (@Copilot)        │   │
  │  │  ❌ gstack非対応   │  │  ❌ gstack非対応   │   │
  │  └───────────────────┘  └───────────────────┘   │
  └─────────────────────────────────────────────────┘
  ```

  | 環境 | gstack の対応 |
  |------|-------------|
  | **VS Code 統合ターミナル + Claude Code CLI** | ✅ 対応。ターミナル上で `claude` を起動して使用 |
  | **VS Code 統合ターミナル + Cursor CLI** | ✅ 対応。`--host cursor` でインストール |
  | **VS Code 統合ターミナル + Codex CLI** | ✅ 対応。`--host codex` でインストール |
  | **VS Code Copilot チャット**（`Ctrl+I`） | ❌ 非対応。プラグイン機構がない |
  | **VS Code Copilot エージェントモード**（`Ctrl+Shift+I`） | ❌ 非対応 |
  | **VS Code サイドパネル**（`@Copilot`） | ❌ 非対応 |

  > 💡 **ポイント**: VS Code 上で gstack を使うには、**統合ターミナル**（`` Ctrl+` ``）で Claude Code や Codex CLI を起動し、そのセッション内で gstack のスラッシュコマンドを使用します。VS Code のチャット画面では動作しませんが、ターミナル上の CLI エージェントであれば問題なく利用できます。

  ### マルチエージェント対応

  gstack は Claude Code だけでなく、10種類のAIコーディングエージェントに対応しています：

  | エージェント | フラグ |
  |------------|--------|
  | OpenAI Codex CLI | `--host codex` |
  | OpenCode | `--host opencode` |
  | Cursor | `--host cursor` |
  | Factory Droid | `--host factory` |
  | Slate | `--host slate` |
  | Kiro | `--host kiro` |
  | Hermes | `--host hermes` |
  | GBrain (mod) | `--host gbrain` |

  ## Superpowers との比較

  gstack と Superpowers（3-1で学んだJesse Vincentの開発方法論）は、どちらも「スキルによってAIエージェントを強化する」という点で共通しますが、アプローチが異なります。

  ### 起動方式の違い

  ```mermaid
  sequenceDiagram
      participant U as あなた
      participant G as gstack
      participant S as Superpowers

      Note over U,S: gstack: 明示的コマンド
      U->>G: /office-hours
      G->>U: 設計ドキュメント
      U->>G: /review
      G->>U: レビュー結果

      Note over U,S: Superpowers: 自動起動
      U->>S: 「この機能を実装して」
      S->>S: 自動: brainstorming起動
      S->>U: 設計を確認して良いですか？
      U->>S: はい
      S->>S: 自動: writing-plans起動
      S->>U: 実装計画を作成しました
  ```

  ### 比較表

  | 観点 | gstack（Garry Tan） | Superpowers（Jesse Vincent） |
  |------|-------------------|------------------------------|
  | **目的** | 個人がチームのように出荷する | 開発プロセス全体の方法論を注入する |
  | **提供形態** | OSSスキルセット（git clone） | Claude Plugin Marketplace |
  | **起動方法** | **明示的**（スラッシュコマンド） | **自動的**（状況に応じて自律起動） |
  | **役割モデル** | CEO/EM/QA/Release Managerなど**役割ベース** | brainstorming/writing-plansなど**プロセスベース** |
  | **スキル数** | 23 specialists + 8 power tools | 15スキル |
  | **カバー範囲** | 設計→実装→レビュー→QA→セキュリティ→デプロイ→振り返り | 設計→実装→テスト→デバッグ→レビュー→Git運用 |
  | **特徴** | 役割分担による品質担保、実ブラウザQA、セキュリティ監査 | HARD-GATEによる強制、サブエージェント駆動、TDD強制 |
  | **対応エージェント** | Claude Code含む10種類 | Claude Code含む8種類 |
  | **ライセンス** | MIT | MIT |

  両者は排他的ではなく、**併用も可能**です。Superpowers の「考えてから書く」プロセス設計思想は、gstack の各スキル定義にも応用できます。

  ## gstack が示すスキル設計の教訓

  ### 1. 役割分担の重要性

  1つのAIに全てを任せるのではなく、**役割ごとにスキルを分離**することで、各タスクに最適なプロンプトとコンテキストを提供できます。

  ### 2. スプリントの流れに沿った設計

  Think → Plan → Build → Review → Test → Ship → Reflect という自然な開発フローに沿ってスキルを配置することで、**何をすべきかが明確**になります。

  ### 3. 防護機構の組み込み

  `/careful`（破壊的コマンドの警告）、`/freeze`（編集範囲の制限）、`/guard`（両方）といった**セーフティネット**を標準装備することで、AIの暴走を防ぎます。

  ### 4. 実環境での検証

  `/browse` や `/qa` による**実際のブラウザ操作**での検証は、AIが生成したコードが実際に動くことを保証します。

  ### 5. オープンソースによる進化

  MITライセンスで公開され、誰でもフォークして自分用にカスタマイズできます。コミュニティによる改善が継続的に行われています。

  ## 次のステップ

  → [3-3a: frontend-design — フロントエンド設計支援スキル](03-3a-frontend-design.md)
  → [3-3b: ui-ux-pro-max — UI/UX最適化スキル](03-3b-ui-ux-pro-max.md)
  ````

- [ ] **Step 3: 保持すべき情報がすべて含まれているか確認する**

  以下をファイル内で目視チェック：
  - [ ] `git clone --single-branch --depth 1` コマンドが残っている
  - [ ] `./setup --team` コマンドが残っている
  - [ ] VS Code の ASCII 図（`┌─────...`）が残っている
  - [ ] マルチエージェント対応テーブル（OpenAI Codex CLI, OpenCode, Cursor など8行）が残っている
  - [ ] 全スキル一覧テーブル（Think/Plan/Build/Review/Test/Ship/Reflect の7フェーズ）が残っている
  - [ ] `/office-hours`, `/plan-ceo-review`, `/review`, `/qa`, `/careful`, `/design-shotgun` の詳細説明が残っている
  - [ ] Mermaid シーケンス図（sequenceDiagram）が残っている
  - [ ] 比較表（観点・目的・提供形態・起動方法・役割モデル・スキル数・カバー範囲・特徴・対応エージェント・ライセンスの10行）が残っている
  - [ ] 設計の教訓 5項目（役割分担・スプリント設計・防護機構・実環境検証・OSS進化）が残っている
  - [ ] 次のステップリンク（03-3a-frontend-design.md, 03-3b-ui-ux-pro-max.md）が残っている

- [ ] **Step 4: 新規追加・削除されたセクションを確認する**

  新規追加（存在するか）：
  - [ ] `## AIに「全部やって」と頼んでいませんか？` が冒頭付近に存在する
  - [ ] シーン1（AIが自分のコードをレビュー）・シーン2（設計者と実装者が同一）・シーン3（QA自己申告）の3つが存在する
  - [ ] `## gstack — AIエージェントを「仮想チーム」に変える` が存在する
  - [ ] `/office-hours → CEO役`, `/qa → QAリード役` などの役割説明コードブロックが存在する
  - [ ] `### Garry Tan の実績` が `## gstack` セクション内のサブセクションとして存在する
  - [ ] `## 同じ依頼で何が変わるのか` セクションが存在する
  - [ ] Before（gstack なし）のターミナル出力が存在する
  - [ ] スキル一覧の直下に「必要なときに参照してください」の一文が存在する

  削除されたもの（存在しないか）：
  - [ ] `## 背景：単一AIアシスタント問題` セクションが存在しない
  - [ ] `## Garry Tan の実績` が独立した `##` セクションとして存在しない
  - [ ] `graph TB` の Mermaid 図（gstack 構造ノード図）が存在しない
  - [ ] `graph LR` の Mermaid 図（スプリント比較図）が存在しない

- [ ] **Step 5: コミットする**

  ```bash
  git add docs/03-frameworks/02-gstack-overview.md
  git commit -m "docs: 02-gstack-overview.md を物語構造に再構成

  初心者・中級者が冒頭から価値訴求を感じながら読み進められるよう再設計。
  AIに全役割を任せる問題への共感フックから仮想チームの解決策へ。情報削除はゼロ。"
  ```

---

### Task 2: 実装計画ファイル自体をコミットする

**Files:**
- Modify: `docs/superpowers/plans/2026-06-20-gstack-doc-restructure.md`（このファイル）

**Interfaces:**
- Consumes: Task 1 完了後の状態
- Produces: コミット済みの計画ファイル

- [ ] **Step 1: 計画ファイルをコミットする**

  ```bash
  git add docs/superpowers/plans/2026-06-20-gstack-doc-restructure.md
  git commit -m "docs: 02-gstack-overview.md リストラクチャリングの実装計画を追加"
  ```
