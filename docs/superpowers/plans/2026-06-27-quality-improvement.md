# 教材品質向上（Why/When セクション追加）実装計画

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 各章に「設計の意図（Why）」と「この設計を変えるとき（When to diverge）」セクションを追加し、上級者が設計判断を自分でできるようになる学習体験を実現する。

**Architecture:** Tier 1（実践スキル章・スキル作成入門）→ Tier 2（概念・フレームワーク章）→ Tier 3（構造矛盾修正）の順に改修する。各章に 2 つのセクションを追加し、新出用語は章内インライン注釈と `08-glossary/01-glossary.md` の両方に反映する。

**Tech Stack:** Markdown 編集のみ。コード変更なし。

## Global Constraints

- インライン注釈形式: 新規固有名詞は `用語`（: 〜の意）、集約概念は `N〇〇（要素1・要素2・…のN種類の〇〇）`
- Why セクションの代替案は 1〜2 案、各案に理由を一文で添える
- When to diverge は「こういうときは変えてよい」という能動的な条件文で書く
- 用語集の重複エントリは追加しない（追加前に既存エントリを確認すること）
- 完了基準は spec ファイル `docs/superpowers/specs/2026-06-27-quality-improvement-design.md` の「完了基準」チェックリストを参照

---

### Task 1: grill-me.md に Why/When セクションを追加

**Files:**
- Modify: `agent-skills-in-practice/docs/04-skills-in-practice/01-grill-me.md`
- Modify: `agent-skills-in-practice/docs/08-glossary/01-glossary.md`

**Interfaces:**
- Produces: `## 設計の意図` セクション（「この SKILL.md から学べる設計パターン」の直前に挿入）
- Produces: `## この設計を変えるとき` セクション（「次のステップ」の直前に挿入）
- Produces: 用語集に「CI」「評価軸」を追加

- [ ] **Step 1: grill-me.md に「設計の意図」セクションを追加**

「この SKILL.md から学べる設計パターン」見出しの直前に以下を挿入する:

```markdown
## 設計の意図

### なぜ評価軸を4つにするのか

4軸（可読性・パフォーマンス・セキュリティ・保守性の4つの評価観点）を選んだ理由: 各軸が独立した関心事のため、`focus_areas`（評価対象を特定軸に絞り込むパラメータ）による選択的実行が成立する。

**代替案との比較**:
- 2軸（品質 / リスク）: シンプルだが「パフォーマンス問題だけ見たい」という絞り込みができない
- 6軸以上: `description`（スキルの自動発動トリガーとなる説明文）が長くなり、発動精度が下がる

### なぜ重大度を3段階にするのか

Critical / Major / Minor の3段階（止める・警告・参考の3つの対処レベル）にしている。2段階では警告の表現力がなく、4段階以上では受け取る側が優先判断に迷う。

### なぜ positive_feedback を含めるのか

問題点だけを返すレビューは、指摘する側と受ける側の非対称な関係を強化する。`positive_feedback`（良い点を明示するフィールド）を組み込むことで、レビューを「審判の判定」から「対話」に変える。

```

- [ ] **Step 2: grill-me.md に「この設計を変えるとき」セクションを追加**

「次のステップ」見出しの直前に以下を挿入する:

```markdown
## この設計を変えるとき

- **軸を増やすとき**: チームに WCAG（Web Content Accessibility Guidelines: Web アクセシビリティの国際基準）準拠が必須になった場合、`accessibility` 軸を追加してよい。ただし `description` も更新しないと自動発動の精度が落ちる。
- **重大度を変えるとき**: CI（Continuous Integration: コードを自動テスト・検証する仕組み）に組み込んで Critical のみ自動ブロックする運用なら、Critical の定義をチームのマージポリシーに合わせて再定義すること。
- **positive_feedback を外すとき**: 自動化パイプラインで機械処理する場合など出力をコンパクトにしたいときは除外してよい。ただし人間がレビュー結果を読むワークフローでは残すことを推奨する。

```

- [ ] **Step 3: 用語集に新出用語を追加**

`08-glossary/01-glossary.md` の「評価・品質」テーブルに以下の行を追加する:

```markdown
| 評価軸 | 評価・品質 | スキルの評価観点をグループ化した軸。grill-me では「可読性・パフォーマンス・セキュリティ・保守性」の4軸を使用 | docs/04-skills-in-practice/01-grill-me.md |
```

「概念」テーブルに以下の行を追加する:

```markdown
| CI（Continuous Integration） | 概念 | 継続的インテグレーション。コードをリポジトリに統合するたびに自動テスト・検証を実行する開発プラクティス | docs/04-skills-in-practice/01-grill-me.md |
```

- [ ] **Step 4: 追加内容を確認するチェックリスト**

以下を目視確認する:
- [ ] 「設計の意図」セクションに代替案が2案ある
- [ ] 集約概念「4軸」が構成要素付きで展開されている
- [ ] 「この設計を変えるとき」に WCAG と CI のインライン注釈がある
- [ ] 用語集の重複がない（WCAG はすでに存在するため追加不要）

- [ ] **Step 5: コミット**

```bash
git add agent-skills-in-practice/docs/04-skills-in-practice/01-grill-me.md
git add agent-skills-in-practice/docs/08-glossary/01-glossary.md
git commit -m "docs: add Why/When sections to grill-me.md"
```

---

### Task 2: triage-issue-analysis.md に Why/When セクションを追加

**Files:**
- Modify: `agent-skills-in-practice/docs/04-skills-in-practice/02-triage-issue-analysis.md`
- Modify: `agent-skills-in-practice/docs/08-glossary/01-glossary.md`

**Interfaces:**
- Produces: `## 設計の意図` セクション（「この SKILL.md から学べる設計パターン」の直前）
- Produces: `## この設計を変えるとき` セクション（「次のステップ」の直前）
- Produces: 用語集に「SLA」「コンテキスト注入パターン」を追加

- [ ] **Step 1: triage-issue-analysis.md に「設計の意図」セクションを追加**

「この SKILL.md から学べる設計パターン」見出しの直前に以下を挿入する:

```markdown
## 設計の意図

### なぜ優先度を4段階にするのか

P0〜P3 の4段階（即時対応・高優先・通常・低優先の4つの対応レベル）にしている。2段階（緊急/通常）では「高優先だが今夜でなくていい」を表現できず、5段階以上では判定基準の境界が曖昧になりやすい。

### なぜ project_context をオプション入力にするのか

スキル本体は汎用ロジックとして保ち、プロジェクト固有の文脈を外から注入するコンテキスト注入パターン（スキルのロジックと文脈を分離し、文脈を呼び出し側から渡す設計方法）を採用している。必須にするとインストール直後に動かず採用率が下がる。

**代替案との比較**:
- `project_context` を必須にする: 精度は上がるが、未入力でエラーになるためハードルが高い
- スキルをプロジェクトごとに複製する: カスタマイズ性は高いが、バグ修正のたびに全コピーを更新する必要がある

### なぜ不足情報の自動検出を含めるのか

再現手順・影響範囲・環境情報が欠けている Issue は精度の高いトリアージができない。不足情報を指摘するロジックを組み込むことで、スキルが「回答者」ではなく「対話のパートナー」として機能し、Issue 報告品質の底上げにも繋がる。

```

- [ ] **Step 2: triage-issue-analysis.md に「この設計を変えるとき」セクションを追加**

「次のステップ」見出しの直前に以下を挿入する:

```markdown
## この設計を変えるとき

- **優先度段階を変えるとき**: SLA（Service Level Agreement: サービスレベル合意書。応答時間などの品質基準を定めた契約）に「P0 は 30 分以内」などの明示的な基準がある場合、基準をそのまま SKILL.md の判定ロジックに転記すること。段階数は変えても構わない。
- **project_context を必須にするとき**: 単一プロジェクト専用スキルとして使う場合、`project_context` をフロントマターに固定値で書き込むと入力漏れを防げる。
- **自動化パイプラインに組み込むとき**: GitHub Actions からトリガーする場合、出力フォーマットを JSON に固定し `recommendation` フィールドのみを取り出すよう SKILL.md を調整すること。

```

- [ ] **Step 3: 用語集に新出用語を追加**

`08-glossary/01-glossary.md` の「技術規格」テーブルに以下の行を追加する:

```markdown
| SLA（Service Level Agreement） | 技術規格 | サービスレベル合意書。応答時間・可用性などのサービス品質基準を定めた契約または内部規定 | docs/04-skills-in-practice/02-triage-issue-analysis.md |
```

「概念」テーブルに以下の行を追加する:

```markdown
| コンテキスト注入パターン | 概念 | スキル本体は汎用ロジックとして保ち、プロジェクト固有の文脈（コンテキスト）を呼び出し側から渡す設計パターン。1つのスキルを複数プロジェクトで再利用可能にする | docs/04-skills-in-practice/02-triage-issue-analysis.md |
```

- [ ] **Step 4: 確認チェックリスト**

- [ ] 集約概念「P0〜P3 の4段階」が構成要素付きで展開されている
- [ ] 「コンテキスト注入パターン」のインライン注釈がある
- [ ] SLA のインライン注釈がある
- [ ] 代替案が2案ある

- [ ] **Step 5: コミット**

```bash
git add agent-skills-in-practice/docs/04-skills-in-practice/02-triage-issue-analysis.md
git add agent-skills-in-practice/docs/08-glossary/01-glossary.md
git commit -m "docs: add Why/When sections to triage-issue-analysis.md"
```

---

### Task 3: improve.md に Why/When セクションを追加

**Files:**
- Modify: `agent-skills-in-practice/docs/04-skills-in-practice/03-improve.md`
- Modify: `agent-skills-in-practice/docs/08-glossary/01-glossary.md`

**Interfaces:**
- Produces: `## 設計の意図` セクション（「この SKILL.md から学べる設計パターン」の直前）
- Produces: `## この設計を変えるとき` セクション（「次のステップ」の直前）
- Produces: 用語集に「難易度×効果マトリクス」「quick_wins」を追加

- [ ] **Step 1: improve.md に「設計の意図」セクションを追加**

「この SKILL.md から学べる設計パターン」見出しの直前に以下を挿入する:

```markdown
## 設計の意図

### なぜ「難易度×効果」マトリクスで分類するのか

難易度×効果マトリクス（改善案を「実装の難しさ」と「期待される効果」の2軸で4象限に分類する手法）を使う理由: 改善案を列挙するだけでは「何から始めるか」が分からない。`quick_wins`（難易度が低く効果が高い改善案）を明示することで、出力が実行計画になる。

**代替案との比較**:
- 全提案をフラットに列挙: シンプルだが受け取る側が優先判断をゼロから行う必要がある
- 効果のみで並べる: 難易度の高い改善案が上位に来て着手できずに終わるリスクがある

### なぜ改善観点を3つにするのか

パフォーマンス・リファクタリング・モダナイゼーションの3観点（速さを改善するか・構造を整えるか・最新技術に置き換えるか）は、それぞれ異なるリソースと意思決定者が必要なため独立している。`improvement_type` による絞り込みが成立するのはこの独立性による。

### なぜ constraints をオプションパラメータにするのか

現実の制約（IE11 対応・bundle size 上限など）なしの提案は「理想論」になりやすい。一方、制約を必須にするとスキルの起動ハードルが上がる。オプションにすることで最低限の情報でも動作しつつ、詳細情報があれば精度が上がる設計にしている。

```

- [ ] **Step 2: improve.md に「この設計を変えるとき」セクションを追加**

「次のステップ」見出しの直前に以下を挿入する:

```markdown
## この設計を変えるとき

- **観点を追加するとき**: チームにセキュリティ改善の専任担当がいる場合、`security` 観点を追加してよい。ただし `grill-me` のセキュリティ軸との役割分担を SKILL.md 内に明記すること。
- **マトリクスの軸を変えるとき**: スプリント内に収まるかどうかを基準にしたい場合、難易度の代わりに「推定工数（日）」を軸にしてもよい。判定基準を SKILL.md 内に数値で定義すること。
- **constraints を必須にするとき**: 単一プロジェクト専用として使う場合、フロントマターに制約を固定値で記述すると入力漏れを防げる。

```

- [ ] **Step 3: 用語集に新出用語を追加**

`08-glossary/01-glossary.md` の「概念」テーブルに以下の行を追加する:

```markdown
| 難易度×効果マトリクス | 概念 | 改善案を「実装の難しさ」と「期待される効果」の2軸で分類する手法。improve スキルの `quick_wins` / `long_term` 分類の基礎 | docs/04-skills-in-practice/03-improve.md |
```

「評価・品質」テーブルに以下の行を追加する:

```markdown
| quick_wins | 評価・品質 | improve スキルの出力分類。難易度が低く効果が高い改善案。すぐ着手できる改善として優先的に提示される | docs/04-skills-in-practice/03-improve.md |
```

- [ ] **Step 4: 確認チェックリスト**

- [ ] 集約概念「3観点」が構成要素付きで展開されている
- [ ] 「難易度×効果マトリクス」のインライン注釈がある
- [ ] 代替案が2案ある

- [ ] **Step 5: コミット**

```bash
git add agent-skills-in-practice/docs/04-skills-in-practice/03-improve.md
git add agent-skills-in-practice/docs/08-glossary/01-glossary.md
git commit -m "docs: add Why/When sections to improve.md"
```

---

### Task 4: what-are-agent-skills.md に Why/When セクションを追加

**Files:**
- Modify: `agent-skills-in-practice/docs/01-skill-creation/01-what-are-agent-skills.md`
- Modify: `agent-skills-in-practice/docs/08-glossary/01-glossary.md`

**Interfaces:**
- Produces: `## 設計の意図` セクション（「スキルの配置場所」の直前）
- Produces: `## この設計を変えるとき` セクション（「次のステップ」の直前）
- Produces: 用語集に「トークン」を追加

- [ ] **Step 1: what-are-agent-skills.md に「設計の意図」セクションを追加**

「スキルの配置場所」見出しの直前に以下を挿入する:

```markdown
## 設計の意図

### なぜ YAML フロントマターと Markdown 本文に分けるのか

2部構成（YAML メタデータと Markdown 本文を `---` で分けた構造）にしている理由: エージェントは `description` フィールドだけを読んで「このスキルを今読むべきか」を判断する。本文全体を読み込むのは確定してから行うため、2部に分けることでトークン（AI が一度に処理する文字・単語の単位。処理コストの基準になる）消費を抑えられる。

**代替案との比較**:
- メタデータを本文末尾に置く: 判定に必要な情報を最後まで読まないといけない
- JSON 形式のみ: 人間が読み書きしにくく、Markdown エディタでの編集体験が悪い

### なぜ description を name と別フィールドにするのか

`name`（スキルの識別子: ユーザーが `/スキル名` で呼び出すときに使う）と `description`（自動発動の判定基準: エージェントが「今の会話に関連するか」を判断するための説明文）は役割が異なる。同一フィールドにまとめると、名前が短いスキル（例: `review`）の自動発動精度が下がる。

```

- [ ] **Step 2: what-are-agent-skills.md に「この設計を変えるとき」セクションを追加**

「次のステップ」見出しの直前に以下を挿入する:

```markdown
## この設計を変えるとき

- **プラットフォーム固有機能を使うとき**: `!` 構文（動的コンテキスト注入）など Claude Code 専用機能を使う場合、クロスプラットフォーム互換性が失われる。SKILL.md の冒頭に「Claude Code 専用」と明記すること。
- **description を長くするとき**: 詳細な発動条件を書くほど自動読み込みの精度は上がるが、150 文字を超えると逆効果になることがある。`/skill-creator` の Description 最適化機能で適切な長さを確認すること。

```

- [ ] **Step 3: 用語集に新出用語を追加**

`08-glossary/01-glossary.md` の「概念」テーブルに以下の行を追加する:

```markdown
| トークン | 概念 | AI が一度に処理する文字・単語の単位。SKILL.md の読み込みコストはトークン数で計測される。フロントマターを分離することでトークン消費を最小化できる | docs/01-skill-creation/01-what-are-agent-skills.md |
```

- [ ] **Step 4: 確認チェックリスト**

- [ ] 集約概念「2部構成」が構成要素付きで展開されている
- [ ] 「トークン」のインライン注釈がある
- [ ] `name` と `description` の役割の違いが明確に述べられている

- [ ] **Step 5: コミット**

```bash
git add agent-skills-in-practice/docs/01-skill-creation/01-what-are-agent-skills.md
git add agent-skills-in-practice/docs/08-glossary/01-glossary.md
git commit -m "docs: add Why/When sections to what-are-agent-skills.md"
```

---

### Task 5: best-practices.md に Why/When セクションを追加

**Files:**
- Modify: `agent-skills-in-practice/docs/01-skill-creation/04-best-practices.md`

**Interfaces:**
- Produces: `## 設計の意図` セクション（「スキル品質評価チェックリスト」の直前）
- Produces: `## この設計を変えるとき` セクション（「次のステップ」の直前）
- Produces: 用語集への追加なし（新出用語は Task 1〜4 で追加済み）

- [ ] **Step 1: best-practices.md に「設計の意図」セクションを追加**

「スキル品質評価チェックリスト」見出しの直前に以下を挿入する:

```markdown
## 設計の意図

### なぜ単一責任の原則をスキルに適用するのか

単一責任の原則（1 つのモジュールが 1 つの関心事だけを担う設計原則）をスキルに適用する理由: 「コードレビュー＋テスト生成＋ドキュメント作成」を 1 スキルにまとめると、`description` が長くなり自動発動の精度が下がる。また、一部の機能だけ使いたい場合に分割できない。

**代替案との比較**:
- 多機能スキル: セットアップが 1 回で済むが、不要な機能が常に実行される
- 機能ごとに独立したスキル（推奨）: `description` が短く精度が上がり、組み合わせが自由になる

### なぜ description の最適化を反復サイクルに組み込むのか

スキルを一度作って `description` を固定する設計では、実際の使用パターンと自動発動条件がずれていく。反復改善サイクル（作成→テスト→確認→改善のループ）の中に `description` の見直しを組み込むことで、トリガー精度（`description` がスキル自動読み込みを正確に判断できる度合い）を継続的に保てる。

```

- [ ] **Step 2: best-practices.md に「この設計を変えるとき」セクションを追加**

「次のステップ」見出しの直前に以下を挿入する:

```markdown
## この設計を変えるとき

- **複合スキルを作るとき**: 「設計→実装→テスト」を一貫して行うスキルが必要な場合、単一責任を意図的に緩めてよい。ただしその場合は `invoke: user` に設定して手動呼び出し専用にし、自動発動を無効にすること。
- **クロスプラットフォームを諦めるとき**: `!` 構文や `approved_tools` など Claude Code 固有機能を使う場合、GitHub Copilot での動作が保証されなくなる。SKILL.md の冒頭に「Claude Code 専用」と明記すること。

```

- [ ] **Step 3: 確認チェックリスト**

- [ ] 「単一責任の原則」のインライン注釈がある
- [ ] 「反復改善サイクル」が構成要素付きで展開されている
- [ ] 「トリガー精度」のインライン注釈がある（用語集の既存エントリへの参照でも可）

- [ ] **Step 4: コミット**

```bash
git add agent-skills-in-practice/docs/01-skill-creation/04-best-practices.md
git commit -m "docs: add Why/When sections to best-practices.md"
```

---

### Task 6: superpowers.md に Why/When セクションを追加

**Files:**
- Modify: `agent-skills-in-practice/docs/03-frameworks/01-superpowers.md`

**Interfaces:**
- Produces: `## 設計の意図` セクション（「哲学」セクションの直前）
- Produces: `## この設計を変えるとき` セクション（「次のステップ」の直前）

- [ ] **Step 1: superpowers.md に「設計の意図」セクションを追加**

「哲学」見出しの直前に以下を挿入する:

```markdown
## 設計の意図

### なぜワークフローを7段階のスキルに分割するのか

7段階（brainstorming・worktree・計画・実装・テスト・レビュー・完了の一連のフロー）を 1 つのスキルにまとめず分割している理由: 各段階は独立して使える。「設計だけ Superpowers、実装は通常モード」という部分採用が可能で、チームへの段階的導入ができる。また各スキルのコンテキストが小さくなり、エージェントの推論精度が上がる。

**代替案との比較**:
- 1 つの大スキルで全段階をカバー: セットアップが楽だが、途中から参加したチームメンバーが学習しにくい
- スキルなしで自然言語プロンプトだけで制御: 毎回同じ指示を書く必要があり、指示のブレが生じる

### なぜ HARD-GATE を使うのか

HARD-GATE（特定の条件を満たすまで次のアクションを禁止する強制ゲート）を使う理由: 「設計なしに実装を始める」という最も多いエージェントの失敗パターンを、ルールではなく構造で防ぐ。エージェントが「うっかり」実装に移れないようにする。

**代替案との比較**:
- CLAUDE.md への指示のみ: エージェントが状況によって指示を無視することがある
- ユーザーが毎回口頭で制止する: 自動化の恩恵が薄れ、人的コストがかかる

```

- [ ] **Step 2: superpowers.md に「この設計を変えるとき」セクションを追加**

「次のステップ」見出しの直前に以下を挿入する:

```markdown
## この設計を変えるとき

- **ワークフローを短縮するとき**: 小規模な修正（1 ファイル・1 関数の変更）では brainstorming をスキップして writing-plans から始めてよい。ただし要件が曖昧な場合は省略しないこと。
- **HARD-GATE を緩めるとき**: 熟練した開発者だけのチームで設計合意が口頭で取れている場合、HARD-GATE の強制を外してもよい。ただしその場合でも「実装前に設計を言語化する」習慣は維持すること。

```

- [ ] **Step 3: 確認チェックリスト**

- [ ] 集約概念「7段階」が構成要素付きで展開されている
- [ ] 「HARD-GATE」が既存のインライン説明と矛盾していない（用語集の既存エントリと一致）
- [ ] 代替案が各 Why に 2 案ある

- [ ] **Step 4: コミット**

```bash
git add agent-skills-in-practice/docs/03-frameworks/01-superpowers.md
git commit -m "docs: add Why/When sections to superpowers.md"
```

---

### Task 7: frontend-design.md に Why/When セクションを追加

**Files:**
- Modify: `agent-skills-in-practice/docs/03-frameworks/05-frontend-design.md`

**Interfaces:**
- Produces: `## 設計の意図` セクション（「次のステップ」の直前）
- Produces: `## この設計を変えるとき` セクション（「次のステップ」の直前、「設計の意図」の後）

- [ ] **Step 1: frontend-design.md の末尾構造を確認**

ファイルを読み、「次のステップ」の直前に挿入する位置を特定すること。

- [ ] **Step 2: frontend-design.md に「設計の意図」セクションを追加**

「次のステップ」見出しの直前に以下を挿入する:

```markdown
## 設計の意図

### なぜコードより先にアーキテクチャを出力させるのか

通常のコード生成（要件→即コード）では、コンポーネントの責任範囲・状態の持ち場・データの流れが暗黙のままコードに埋め込まれる。一度コードが存在すると、設計の見直しはリファクタリングコストになる。アーキテクチャ（システムの構成要素と要素間の関係を定義した設計図）を先に出力させることで、コードを書く前に設計の問題を発見できる。

### なぜ観点を4つにするのか

コンポーネント分割・状態管理・データフロー・レンダリング最適化の4観点（UI の分割方法・データの置き場所・データの流れ・描画パフォーマンスの4つの設計軸）は、フロントエンドアーキテクチャの相互依存する4領域に対応している。コンポーネント構成を決めると状態の持ち場が絞られ、状態を決めるとデータフローが決まる順序関係があるため、この 4 つをセットで設計する。

**代替案との比較**:
- 観点をユーザーに選ばせる: 自由度が上がるが、相互依存を見落としやすい
- 2 観点に絞る（分割・状態のみ）: 素早く設計できるがレンダリング問題が後で表面化する

```

- [ ] **Step 3: frontend-design.md に「この設計を変えるとき」セクションを追加**

「設計の意図」セクションの直後（「次のステップ」の直前）に以下を挿入する:

```markdown
## この設計を変えるとき

- **小規模プロジェクトで観点を絞るとき**: ページ数が 3 以下の小規模サイトでは「コンポーネント分割のみ」に絞ってよい。状態管理とデータフローが自明なため設計コストが見合わない。
- **フレームワークが設計を規定するとき**: Next.js の App Router・Remix など、フレームワークがルーティングとデータフェッチを規定している場合、データフロー観点の設計はフレームワークの規約に委ねて省略してよい。

```

- [ ] **Step 4: 確認チェックリスト**

- [ ] 集約概念「4観点」が構成要素付きで展開されている
- [ ] 「アーキテクチャ」のインライン注釈がある
- [ ] 代替案が 2 案ある

- [ ] **Step 5: コミット**

```bash
git add agent-skills-in-practice/docs/03-frameworks/05-frontend-design.md
git commit -m "docs: add Why/When sections to frontend-design.md"
```

---

### Task 8: evaluation-cycle.md に Why/When セクション追加と構造修正

**Files:**
- Modify: `agent-skills-in-practice/docs/06-advanced/03-evaluation-cycle.md`
- Modify: `agent-skills-in-practice/docs/08-glossary/01-glossary.md`

**Interfaces:**
- Produces: `## 設計の意図` セクション（「継続的改善のベストプラクティス」の直前）
- Produces: `## この設計を変えるとき` セクション（「次のステップ」の直前）
- Produces: 見出し番号「5-3」→「6-3」の修正
- Produces: 誤った `@copilot` 記法の修正
- Produces: 範囲外の「まとめ」セクションを削除
- Produces: 用語集に「Semantic Versioning」を追加

- [ ] **Step 1: 見出し番号を修正**

ファイル冒頭の `# 5-3: スキル評価と改善サイクル` を以下に変更する:

```markdown
# 6-3: スキル評価と改善サイクル
```

- [ ] **Step 2: @copilot 記法を修正**

以下の行を変更する:

変更前:
```
@copilot grill-me スキルを改善して：
```

変更後:
```
/grill-me スキルを改善して：
```

- [ ] **Step 3: 範囲外の「まとめ」セクションを削除**

「## まとめ」から始まり「これらの知識を活用して〜」で終わるブロック（チュートリアル全体のまとめ）を削除する。削除後、「次のステップ」へ直接続くようにする。

- [ ] **Step 4: evaluation-cycle.md に「設計の意図」セクションを追加**

「継続的改善のベストプラクティス」見出しの直前に以下を挿入する:

```markdown
## 設計の意図

### なぜ評価を4軸にするのか

正確性・一貫性・網羅性・実用性の4軸（スキルが正しく・安定して・広く・実際に役立つかを測る4つの評価観点）で評価する理由: 「テストが通れば良い」（正確性のみ）では、同じ入力に毎回違う結果が出る問題（一貫性の欠如）や、エッジケースに対応できない問題（網羅性の欠如）を見落とす。4 軸を揃えることで「リリース可能な品質」を多角的に判断できる。

**代替案との比較**:
- テスト合格率のみ: 計測しやすいが実用性（現場で使われるか）が見えない
- ユーザーフィードバックのみ: 定性的すぎて改善の優先度が判断しにくい

### なぜ Semantic Versioning を使うのか

Semantic Versioning（`vMajor.Minor.Patch` 形式のバージョン番号規則。メジャーは破壊的変更・マイナーは後方互換の機能追加・パッチはバグ修正を意味する）を使う理由: スキルを共有・配布するとき、利用者が「このバージョンに更新すると何が変わるか」を番号だけで判断できる。

```

- [ ] **Step 5: evaluation-cycle.md に「この設計を変えるとき」セクションを追加**

「次のステップ」見出しの直前に以下を挿入する:

```markdown
## この設計を変えるとき

- **評価軸を変えるとき**: チームが「レスポンス速度の安定性」を重視する場合、実用性の代わりに「パフォーマンス」軸を追加してよい。
- **バージョン管理を省略するとき**: 個人利用・社内限定スキルではバージョン番号なしでもよい。ただし共有・配布を始めたら Semantic Versioning を後付けすること。

```

- [ ] **Step 6: 用語集に新出用語を追加**

`08-glossary/01-glossary.md` の「技術規格」テーブルに以下の行を追加する:

```markdown
| Semantic Versioning | 技術規格 | `vMajor.Minor.Patch` 形式のバージョン番号規則。メジャーは破壊的変更、マイナーは後方互換の機能追加、パッチはバグ修正を意味する | docs/06-advanced/03-evaluation-cycle.md |
```

- [ ] **Step 7: 確認チェックリスト**

- [ ] 見出しが「6-3:」になっている
- [ ] `@copilot` 記法が `/{スキル名}` 形式に修正されている
- [ ] 「まとめ」セクション（チュートリアル全体のサマリー）が削除されている
- [ ] 集約概念「4軸」が構成要素付きで展開されている
- [ ] 「Semantic Versioning」のインライン注釈がある

- [ ] **Step 8: コミット**

```bash
git add agent-skills-in-practice/docs/06-advanced/03-evaluation-cycle.md
git add agent-skills-in-practice/docs/08-glossary/01-glossary.md
git commit -m "docs: add Why/When sections to evaluation-cycle.md and fix structural issues"
```

---

### Task 9: 用語集の最終検証

**Files:**
- Read: `agent-skills-in-practice/docs/08-glossary/01-glossary.md`

**Interfaces:**
- Consumes: Task 1〜8 で追加した用語集エントリ
- Produces: 重複・欠落・リンク切れのない用語集

- [ ] **Step 1: 追加された用語の一覧確認**

以下の用語が用語集に存在することを確認する:

| 用語 | カテゴリ | 追加タスク |
|------|---------|-----------|
| 評価軸 | 評価・品質 | Task 1 |
| CI（Continuous Integration） | 概念 | Task 1 |
| SLA（Service Level Agreement） | 技術規格 | Task 2 |
| コンテキスト注入パターン | 概念 | Task 2 |
| 難易度×効果マトリクス | 概念 | Task 3 |
| quick_wins | 評価・品質 | Task 3 |
| トークン | 概念 | Task 4 |
| Semantic Versioning | 技術規格 | Task 8 |

- [ ] **Step 2: 重複エントリがないことを確認**

上記の各用語が 1 行のみ存在することを確認する（同じ用語が複数行あれば重複した方を削除）。

- [ ] **Step 3: spec の完了基準チェックリストを確認**

`docs/superpowers/specs/2026-06-27-quality-improvement-design.md` の完了基準の各項目が満たされていることを確認し、チェックを入れる。

- [ ] **Step 4: 最終コミット**

```bash
git add agent-skills-in-practice/docs/08-glossary/01-glossary.md
git commit -m "docs: final glossary verification for quality improvement"
```
