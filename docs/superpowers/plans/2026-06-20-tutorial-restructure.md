# Tutorial Restructure Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** grill-me / triage / improve を Matt Pocock 公開スキルとして正しく扱い、samples/ を削除し、Part 4 教材を「公開 SKILL.md を解析・実行して学ぶ」形式に転換する。

**Architecture:** 6タスクの順次実行。Task 1（削除）→ Task 2〜4（並列可: Part 4 書き換え）→ Task 5（移動）→ Task 6（マージ）→ Task 7（メタ更新）の順で進める。

**Tech Stack:** Markdown 編集のみ。コードの変更なし。

## Global Constraints

- すべてのファイルパスは `c:\Dev\tutorials\agent-skills-in-practice\` からの相対パスで表記
- Matt Pocock スキルの GitHub URL パターン: `https://github.com/mattpocock/skills/blob/main/skills/productivity/<skill-name>/SKILL.md`
- 各タスク完了後に git commit する
- 内部リンクは相対パスで記述する

---

### Task 1: samples/ と 03-frameworks の不要ファイルを削除する

**Files:**
- Delete: `samples/grill-me/` ディレクトリ全体
- Delete: `samples/triage/` ディレクトリ全体
- Delete: `samples/improve/` ディレクトリ全体
- Delete: `docs/03-frameworks/06-grill-me.md`
- Delete: `docs/03-frameworks/07-triage.md`
- Delete: `docs/03-frameworks/08-improve.md`

**Interfaces:**
- Produces: 削除済みの6アイテム。後続タスクはこれらへの参照を修正する。

- [ ] **Step 1: samples の3ディレクトリを削除する**

```bash
git rm -r samples/grill-me samples/triage samples/improve
```

Expected: `rm 'samples/grill-me/SKILL.md'` 等が表示される。

- [ ] **Step 2: 03-frameworks の3ファイルを削除する**

```bash
git rm docs/03-frameworks/06-grill-me.md docs/03-frameworks/07-triage.md docs/03-frameworks/08-improve.md
```

Expected: 各ファイルの削除メッセージが表示される。

- [ ] **Step 3: 削除されたことを確認する**

```bash
git status
```

Expected: 6アイテムが `deleted:` として staging されている。

- [ ] **Step 4: コミットする**

```bash
git commit -m "chore: Matt Pocock 公開スキルの複製を削除

samples/{grill-me,triage,improve} と docs/03-frameworks/{06,07,08} を削除。
これらは Matt Pocock 氏の公開スキルの複製であったため、
公式リポジトリを参照する形に切り替える。"
```

---

### Task 2: docs/04-skills-in-practice/01-grill-me.md を書き換える

**Files:**
- Modify: `docs/04-skills-in-practice/01-grill-me.md`

**Interfaces:**
- Produces: `01-grill-me.md` — Phase A（SKILL.md 解析）+ Phase B（インストール・実行）+ Phase C（照合）構成

- [ ] **Step 1: 現在のファイルを確認する**

```bash
cat docs/04-skills-in-practice/01-grill-me.md
```

内容を確認して次ステップに備える。

- [ ] **Step 2: ファイルを全面書き換えする**

`docs/04-skills-in-practice/01-grill-me.md` の内容を以下に置き換える：

```markdown
# 4-1: grill-me — コードレビュースキル（Matt Pocock）

> **学習時間**: 25分 | **難易度**: ⭐⭐⭐ | **カテゴリ**: 品質検証

## このスキルについて

**grill-me** は Matt Pocock 氏が公開するコードレビュースキルです。コードの品質を「可読性」「パフォーマンス」「セキュリティ」「保守性」の4軸で徹底的にレビューし、重大度付きの改善提案を返します。

- **出典**: [mattpocock/skills — grill-me](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md)
- **用途**: PR レビュー前のセルフチェック、コード品質の統一基準、ジュニア開発者への教育

---

## Phase A: SKILL.md を読む

[出典の SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md) をブラウザで開き、以下の観点で読みます。

### 構造の解析

| 要素 | 確認すること |
|------|------------|
| フロントマター（`name`, `description`） | どういうトリガー文脈を想定しているか |
| 評価軸の定義 | 4軸がどう記述されているか、各軸の判断基準は何か |
| 出力形式 | スコア・重大度分類・改善提案の構造 |

### 設計上の注目ポイント

**1. 評価軸の独立性**
各軸が互いに独立して定義されている。これにより `focus_areas` で特定軸だけを指定することが可能になっている。

**2. 重大度（Critical / Major / Minor）の明示**
「問題があるかどうか」だけでなく「どれくらい深刻か」を出力に含める設計。PR レビューでの優先度議論を数値化できる。

**3. `positive_feedback` フィールドの存在**
問題点だけでなく良い点も返すことで、レビューが一方的な指摘にならない構造。

---

## Phase B: インストールして動かす

### セットアップ

```bash
# プロジェクトのスキルディレクトリを作成
mkdir -p .claude/skills/grill-me/

# SKILL.md を GitHub から取得して配置
# 出典: https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md
```

または Claude Code Plugin Marketplace でインストール（利用可能な場合）。

### テスト実行

以下のプロンプトで動作を確認します：

```
/grill-me 以下のReactコンポーネントをレビューして：

function UserList() {
  const [users, setUsers] = useState([]);
  useEffect(() => {
    fetch('/api/users').then(r => r.json()).then(setUsers);
  });
  return <ul>{users.map(u => <li>{u.name}</li>)}</ul>;
}
```

**期待される出力のポイント**:

| 問題 | 分類 | 重大度 |
|------|------|--------|
| `useEffect` に依存配列がない（無限ループ） | パフォーマンス | Major |
| `<li>` に `key` がない | 保守性 | Minor |
| エラー状態・ローディング状態がない | 可読性 | Minor |

---

## Phase C: 解析と実行結果の照合

実行結果を見ながら、SKILL.md の設計と照らし合わせる問いです：

1. 実際に返ってきた重大度分類は SKILL.md の基準と一致しているか？
2. `positive_feedback` はどのタイミングで返ってきたか？どのコードが評価されたか？
3. `focus_areas: ["security"]` に絞った場合、出力はどう変わるか？

---

## カスタマイズのヒント

**観点を追加する**
SKILL.md に `accessibility`（WCAG 準拠チェック）軸を追加することで、フロントエンド特化のレビューが可能になります。

**重大度基準を調整する**
チームのコーディング規約に合わせて Critical の定義を変更すると、PR マージ判断の自動化に活用できます。

---

## 次のステップ

→ [4-2: triage — Issue 分析スキル](02-triage-issue-analysis.md)
→ [4-9: 問題 × スキル解決マッピング](09-problem-skill-mapping.md)
```

- [ ] **Step 3: コミットする**

```bash
git add docs/04-skills-in-practice/01-grill-me.md
git commit -m "docs: 4-1 grill-me を公開スキル解析・実行教材に書き換え

Matt Pocock の公開スキルを Phase A（SKILL.md 解析）+
Phase B（インストール・実行）+ Phase C（照合）構成で学ぶ形式に転換。"
```

---

### Task 3: docs/04-skills-in-practice/02-triage-issue-analysis.md を書き換える

**Files:**
- Modify: `docs/04-skills-in-practice/02-triage-issue-analysis.md`

**Interfaces:**
- Produces: `02-triage-issue-analysis.md` — Task 2 と同じ Phase A/B/C 構成

- [ ] **Step 1: ファイルを全面書き換えする**

`docs/04-skills-in-practice/02-triage-issue-analysis.md` の内容を以下に置き換える：

```markdown
# 4-2: triage — Issue 分析スキル（Matt Pocock）

> **学習時間**: 25分 | **難易度**: ⭐⭐⭐ | **カテゴリ**: 優先順位付け

## このスキルについて

**triage** は Matt Pocock 氏が公開する Issue 分析スキルです。GitHub Issue の内容を解析し、優先度（P0〜P3）の判定、カテゴリ分類、影響範囲の特定、対応推奨事項を自動生成します。

- **出典**: [mattpocock/skills — triage](https://github.com/mattpocock/skills/blob/main/skills/productivity/triage/SKILL.md)
- **用途**: 新規 Issue の自動トリアージ、バックログ整理、スプリント計画の最適化

---

## Phase A: SKILL.md を読む

[出典の SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/productivity/triage/SKILL.md) をブラウザで開き、以下の観点で読みます。

### 構造の解析

| 要素 | 確認すること |
|------|------------|
| 優先度（P0〜P3）の定義 | 各レベルの判定基準がどう記述されているか |
| 必須 vs オプション入力 | `issue_title`/`issue_body` と `labels`/`project_context` の使い分け |
| `recommendation` フィールド | 推奨アクション・担当チーム・次のステップの構造 |

### 設計上の注目ポイント

**1. 優先度判定の客観化**
P0〜P3 の基準を SKILL.md に明文化することで、担当者の経験・勘に依存しない判定が可能になる。

**2. `project_context` による柔軟性**
プロジェクト固有の文脈（例: BtoB SaaS では全ユーザー影響は即 P0）を注入できる設計。スキル本体は汎用に保たれている。

**3. 不足情報の自動検出**
再現手順・影響範囲・環境情報が欠けている場合に指摘するロジックが含まれる。

---

## Phase B: インストールして動かす

### セットアップ

```bash
mkdir -p .claude/skills/triage/
# SKILL.md を GitHub から取得して配置
# 出典: https://github.com/mattpocock/skills/blob/main/skills/productivity/triage/SKILL.md
```

### テスト実行

以下のプロンプトで動作を確認します：

```
/triage
タイトル: 「ログインページで500エラーが発生する」
本文: 本番環境でログインページにアクセスすると Internal Server Error が発生します。
エラーログには「TypeError: Cannot read properties of null」と記録されています。
再現率は100%で、全ユーザーに影響します。
```

**期待される出力のポイント**:

| 項目 | 期待値 |
|------|--------|
| 優先度 | P0（本番クラッシュ・全ユーザー影響） |
| カテゴリ | bug / authentication |
| 影響範囲 | 全ユーザー、severity: high |
| 推奨 | 即時対応、ホットフィックス |

---

## Phase C: 解析と実行結果の照合

1. P0 判定の根拠として SKILL.md のどの基準が使われたか？
2. `project_context: "BtoC サービス、DAU 10万人"` を追加すると出力はどう変わるか？
3. 情報が少ない Issue（「ログインが遅い」のみ）を入れると、不足情報として何が指摘されるか？

---

## カスタマイズのヒント

**優先度基準をプロジェクト仕様に合わせる**
P0/P1 の境界線はプロジェクトによって異なります。SKILL.md の判定基準をチームの SLA に合わせて書き換えると、自動トリアージの精度が上がります。

**GitHub Actions との連携**
出力の `category` を GitHub Actions で受け取り、ラベルを自動付与する自動化も可能です。

---

## 次のステップ

→ [4-3: improve — コード改善スキル](03-improve.md)
→ [4-9: 問題 × スキル解決マッピング](09-problem-skill-mapping.md)
```

- [ ] **Step 2: コミットする**

```bash
git add docs/04-skills-in-practice/02-triage-issue-analysis.md
git commit -m "docs: 4-2 triage を公開スキル解析・実行教材に書き換え"
```

---

### Task 4: docs/04-skills-in-practice/03-improve.md を書き換える

**Files:**
- Modify: `docs/04-skills-in-practice/03-improve.md`

**Interfaces:**
- Produces: `03-improve.md` — Task 2/3 と同じ Phase A/B/C 構成

- [ ] **Step 1: ファイルを全面書き換えする**

`docs/04-skills-in-practice/03-improve.md` の内容を以下に置き換える：

```markdown
# 4-3: improve — コード改善スキル（Matt Pocock）

> **学習時間**: 25分 | **難易度**: ⭐⭐⭐ | **カテゴリ**: リファクタリング

## このスキルについて

**improve** は Matt Pocock 氏が公開するコード改善スキルです。既存コードを分析し、パフォーマンス最適化・リファクタリング・モダナイゼーションの3観点から、難易度と期待効果の評価付きで改善提案を返します。

- **出典**: [mattpocock/skills — improve](https://github.com/mattpocock/skills/blob/main/skills/productivity/improve/SKILL.md)
- **用途**: レガシーコードのモダナイゼーション、パフォーマンスボトルネックの特定、技術負債の返済計画

---

## Phase A: SKILL.md を読む

[出典の SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/productivity/improve/SKILL.md) をブラウザで開き、以下の観点で読みます。

### 構造の解析

| 要素 | 確認すること |
|------|------------|
| 3つの改善観点の定義 | パフォーマンス・リファクタリング・モダナイゼーションがどう区別されているか |
| `difficulty` × `impact` の基準 | スコアリングのロジック |
| `quick_wins` と `long_term` の分類 | 何を基準に振り分けているか |
| `constraints` パラメータ | どのような制約を受け取れるか |

### 設計上の注目ポイント

**1. 「難易度×効果」マトリックスによる優先順位付け**
改善案を列挙するだけでなく `quick_wins`（難易度低・効果高）と `long_term` に分類することで、実行計画が立てやすくなる。

**2. `constraints` による現実的な提案**
IE11 対応・bundle size 制限・移行途中のライブラリ制約など、プロジェクト固有の制約を受け取ることで「理想論」ではなく「実現可能な改善」を提案する設計。

**3. `improvement_type` で観点を絞れる設計**
全観点の分析は時間がかかるため、`refactoring` のみなど絞り込みができる。

---

## Phase B: インストールして動かす

### セットアップ

```bash
mkdir -p .claude/skills/improve/
# SKILL.md を GitHub から取得して配置
# 出典: https://github.com/mattpocock/skills/blob/main/skills/productivity/improve/SKILL.md
```

### テスト実行

以下のプロンプトで動作を確認します：

```
/improve
言語: TypeScript/React

function SearchResults({ query, data }) {
  const [results, setResults] = useState([]);
  useEffect(() => {
    if (data) {
      const filtered = data.filter(item =>
        item.name.includes(query) || item.description.includes(query)
      );
      setResults(filtered);
    }
  }, [query, data]);
  return <div>{results.map(r => <SearchCard item={r} />)}</div>;
}
```

**期待される出力のポイント**:

| 提案 | 観点 | 分類 |
|------|------|------|
| `useMemo` でフィルタリングをメモ化 | パフォーマンス | quick_win |
| フィルタリングをカスタムフックに分離 | リファクタリング | long_term |
| `React.memo` で `SearchCard` をラップ | パフォーマンス | quick_win |

---

## Phase C: 解析と実行結果の照合

1. `quick_wins` に分類された提案は SKILL.md の難易度基準と一致しているか？
2. `constraints: ["IE11対応"]` を追加すると、モダナイゼーション提案はどう変わるか？
3. `improvement_type: "performance"` のみにした場合、リファクタリング提案は除外されるか？

---

## カスタマイズのヒント

**チーム標準の規約を注入する**
関数の最大行数・命名規則などをリファクタリング基準として SKILL.md に追記すると、コードレビューとの整合性が高まります。

**grill-me との連携**
grill-me でレビュー → improve で改善案取得 → 実装 のサイクルを組むことで、品質向上ループを自動化できます。

---

## 次のステップ

→ [4-4: frontend-design — 設計支援スキル](04-frontend-design.md)
→ [4-9: 問題 × スキル解決マッピング](09-problem-skill-mapping.md)
```

- [ ] **Step 2: コミットする**

```bash
git add docs/04-skills-in-practice/03-improve.md
git commit -m "docs: 4-3 improve を公開スキル解析・実行教材に書き換え"
```

---

### Task 5: problem-skill-mapping を移動して内部リンクを修正する

**Files:**
- Move: `docs/03-frameworks/09-problem-skill-mapping.md` → `docs/04-skills-in-practice/09-problem-skill-mapping.md`
- Modify（移動後）: `docs/04-skills-in-practice/09-problem-skill-mapping.md`（リンク修正）

**Interfaces:**
- Consumes: Task 2〜4 の書き換え済み 01〜03.md（リンク先として参照する）
- Produces: `04-skills-in-practice/09-problem-skill-mapping.md`

- [ ] **Step 1: git mv で移動する**

```bash
git mv docs/03-frameworks/09-problem-skill-mapping.md docs/04-skills-in-practice/09-problem-skill-mapping.md
```

- [ ] **Step 2: 移動後ファイルの内部リンクを修正する**

`docs/04-skills-in-practice/09-problem-skill-mapping.md` を開き、以下の差分を適用する：

| 修正前 | 修正後 |
|--------|--------|
| `[3-3 frontend-design](03-frontend-design.md)` | `[3-3 frontend-design](../03-frameworks/03-frontend-design.md)` |
| `[3-4 ui-ux-pro-max](04-ui-ux-pro-max.md)` | `[3-4 ui-ux-pro-max](../03-frameworks/04-ui-ux-pro-max.md)` |
| `[3-5 baoyu-skills](05-baoyu-skills-architecture.md)` | `[5-1 baoyu-ecosystem](../05-content-creation/01-baoyu-ecosystem.md)` |
| `[3-6 grill-me](06-grill-me.md)` | `[4-1 grill-me](01-grill-me.md)` |
| `[3-7 triage](07-triage.md)` | `[4-2 triage](02-triage-issue-analysis.md)` |
| `[3-8 improve](08-improve.md)` | `[4-3 improve](03-improve.md)` |
| `→ [Part 4: 実践スキル実装編](../04-skills-in-practice/01-grill-me.md)` | `→ [4-1: grill-me](01-grill-me.md)` |

- [ ] **Step 3: 修正を確認する**

```bash
grep -n "06-grill\|07-triage\|08-improve\|05-baoyu-skills-architecture\|03-frontend-design\.md\|04-ui-ux-pro-max\.md" docs/04-skills-in-practice/09-problem-skill-mapping.md
```

Expected: 出力なし（古いリンクがすべて置換されている）

- [ ] **Step 4: コミットする**

```bash
git add docs/04-skills-in-practice/09-problem-skill-mapping.md
git commit -m "docs: problem-skill-mapping を Part 4 の締めくくりとして移動・リンク修正"
```

---

### Task 6: baoyu-skills-architecture を 01-baoyu-ecosystem にマージする

**Files:**
- Read: `docs/03-frameworks/05-baoyu-skills-architecture.md`（マージ元、削除する）
- Modify: `docs/05-content-creation/01-baoyu-ecosystem.md`（マージ先）
- Delete: `docs/03-frameworks/05-baoyu-skills-architecture.md`

**Interfaces:**
- Produces: `05-content-creation/01-baoyu-ecosystem.md`（baoyu-skills-architecture の内容を統合済み）

- [ ] **Step 1: 両ファイルの内容を確認する**

```bash
cat docs/03-frameworks/05-baoyu-skills-architecture.md
cat docs/05-content-creation/01-baoyu-ecosystem.md
```

重複セクション・追加すべき固有セクションを特定する。

- [ ] **Step 2: 01-baoyu-ecosystem.md に統合内容を追加する**

`05-baoyu-skills-architecture.md` の以下のセクションが `01-baoyu-ecosystem.md` に存在しない場合、末尾に追加する：

- 「3大フレームワークの比較」テーブル（Superpowers / gstack / baoyu-skills の比較）
- 「baoyu-skills のアーキテクチャ」（3層アーキテクチャ図）
- 「5D スタイル体系」（設計上の特徴）

既に類似内容がある場合は重複を避け、固有情報のみを追記する。

- [ ] **Step 3: 05-baoyu-skills-architecture.md を削除する**

```bash
git rm docs/03-frameworks/05-baoyu-skills-architecture.md
```

- [ ] **Step 4: コミットする**

```bash
git add docs/05-content-creation/01-baoyu-ecosystem.md
git commit -m "docs: baoyu-skills-architecture を 01-baoyu-ecosystem に統合

05-baoyu-skills-architecture.md の内容を 05-content-creation/01-baoyu-ecosystem.md に
マージし、原本ファイルを削除。アーキテクチャ解説はエコシステム概要として統合。"
```

---

### Task 7: COVER.md とナビゲーションリンクを更新する

**Files:**
- Modify: `docs/00-COVER.md`
- Modify: `docs/03-frameworks/03-frontend-design.md`（末尾リンク修正）
- Modify: `docs/03-frameworks/04-ui-ux-pro-max.md`（末尾リンク修正）

**Interfaces:**
- Consumes: Task 5 で確定した `04-skills-in-practice/09-problem-skill-mapping.md` の新パス

- [ ] **Step 1: 00-COVER.md の Part 3 行を更新する**

`docs/00-COVER.md` の以下の行を修正する：

修正前:
```markdown
| Part 3 | 概念フレームワークと課題認識 | 80分 |
```

修正後:
```markdown
| Part 3 | フレームワーク：Superpowers と設計スキル | 40分 |
```

- [ ] **Step 2: 合計時間を更新する**

修正前:
```markdown
| **合計** | | **9時間35分** |
```

修正後:
```markdown
| **合計** | | **9時間** |
```

- [ ] **Step 3: 03-frontend-design.md の末尾リンクを更新する**

`docs/03-frameworks/03-frontend-design.md` の末尾「次のステップ」セクションを更新する：

修正前:
```markdown
→ [3-9: 問題 × スキル解決マッピング](09-problem-skill-mapping.md) で、全スキルの関係性を整理する
```

修正後:
```markdown
→ [4-9: 問題 × スキル解決マッピング](../04-skills-in-practice/09-problem-skill-mapping.md) で、全スキルの関係性を整理する
```

- [ ] **Step 4: 04-ui-ux-pro-max.md の末尾リンクを更新する**

`docs/03-frameworks/04-ui-ux-pro-max.md` の末尾「次のステップ」セクションを更新する：

修正前:
```markdown
→ [3-9: 問題 × スキル解決マッピング](09-problem-skill-mapping.md) で、全スキルの関係性を整理する
```

修正後:
```markdown
→ [4-9: 問題 × スキル解決マッピング](../04-skills-in-practice/09-problem-skill-mapping.md) で、全スキルの関係性を整理する
```

- [ ] **Step 5: リンクが正しいことを確認する**

```bash
grep -rn "09-problem-skill-mapping" docs/03-frameworks/
```

Expected: `03-frontend-design.md` と `04-ui-ux-pro-max.md` の2件のみ表示され、いずれも `../04-skills-in-practice/09-problem-skill-mapping.md` を指している。

- [ ] **Step 6: コミットする**

```bash
git add docs/00-COVER.md docs/03-frameworks/03-frontend-design.md docs/03-frameworks/04-ui-ux-pro-max.md
git commit -m "docs: COVER と 03-frameworks のナビゲーションリンクを更新

Part 3 タイトル・学習時間を更新（80分→40分、合計 9時間35分→9時間）。
problem-skill-mapping の移動に伴い、03-frontend-design と 04-ui-ux-pro-max の
次のステップリンクを新パスに修正。"
```

---

## 自己レビュー

### 仕様カバレッジ

| 設計仕様の要件 | 対応タスク |
|--------------|----------|
| samples/grill-me, triage, improve 削除 | Task 1 |
| docs/03-frameworks/06,07,08 削除 | Task 1 |
| 04-skills-in-practice/01,02,03 書き換え | Task 2, 3, 4 |
| problem-skill-mapping を Part 4 に移動 | Task 5 |
| baoyu-skills-architecture を統合 | Task 6 |
| COVER.md 更新 | Task 7 |
| 03-frontend-design.md リンク修正 | Task 7 |
| 04-ui-ux-pro-max.md リンク修正 | Task 7 |

### プレースホルダースキャン

- TBD / TODO: なし
- 「適切に処理」等の曖昧な記述: なし（各ステップに具体的な内容あり）

### 型整合性

- リンクパスの一貫性: `09-problem-skill-mapping.md` は全箇所で `04-skills-in-practice/09-problem-skill-mapping.md` を参照 ✓
- Matt Pocock URL パターン: 3ファイルすべてで統一 ✓
