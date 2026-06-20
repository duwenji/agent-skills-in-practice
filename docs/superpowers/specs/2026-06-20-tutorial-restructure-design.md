# 設計仕様: チュートリアル教材の全面見直し

**日付**: 2026-06-20  
**対象**: agent-skills-in-practice チュートリアル  
**方針**: grill-me / triage / improve を Matt Pocock 公開スキルとして正しく扱い、「読んで動かして学ぶ」教材に転換する

---

## 背景と問題認識

`grill-me`、`triage`、`improve` は Matt Pocock 氏が公開している実在のスキルである。現行教材はこれらを「チュートリアルで自作するスキル」として扱い、`samples/` 配下に日本語化した独自 SKILL.md を配置していた。これは事実と異なる扱いであるため、以下の方針で全面的に見直す。

- 公開スキルの複製（samples/）を削除する
- 紹介ページ（03-frameworks/06〜08）を削除する
- Part 4 の実装体験教材を「公開 SKILL.md を解析し、実際に動かして設計を学ぶ」教材に転換する

---

## 変更方針

**C方針 + アプローチ A**:  
公開スキルを「読んで学ぶ」教材に転換し、1スキル＝1ファイルの構成を維持したまま各ファイルで「解析 → インストール → 実行 → 照合」を完結させる。

---

## ファイル操作の仕様

### 削除（6アイテム）

| 対象パス | 理由 |
|---------|------|
| `samples/grill-me/` | Matt Pocock 公開スキルの無断複製 |
| `samples/triage/` | 同上 |
| `samples/improve/` | 同上 |
| `docs/03-frameworks/06-grill-me.md` | 削除スキルの紹介ページ |
| `docs/03-frameworks/07-triage.md` | 同上 |
| `docs/03-frameworks/08-improve.md` | 同上 |

### 移動（2ファイル）

| 移動元 | 移動先 | 備考 |
|--------|--------|------|
| `docs/03-frameworks/09-problem-skill-mapping.md` | `docs/04-skills-in-practice/09-problem-skill-mapping.md` | Part 4 の締めくくりとして配置。番号はそのまま 09 |
| `docs/03-frameworks/05-baoyu-skills-architecture.md` | `docs/05-content-creation/01-baoyu-ecosystem.md` にマージ | 独立ファイルは削除、内容を 01 に統合 |

### 書き換え（3ファイル）

`docs/04-skills-in-practice/01-grill-me.md`、`02-triage-issue-analysis.md`、`03-improve.md` を以下のテンプレートで全面書き換えする。

#### 各ファイルの共通構成

```
# 4-X: <スキル名> — <役割>（Matt Pocock）

学習時間 / 難易度 / カテゴリ

## このスキルについて
公開スキルの概要・用途・出典 GitHub URL

## Phase A: SKILL.md を読む
### 構造の解析
フロントマター・手順・制約を読み解く

### 設計上の注目ポイント
「なぜこう書いてあるか」の解説（2〜3点）

## Phase B: インストールして動かす
### セットアップ
Claude Code へのインストール手順

### テスト実行
具体的なプロンプト例と期待される出力

## Phase C: 解析と実行結果の照合
動かした結果が SKILL.md の設計意図とどう対応しているかを確認する問い

## カスタマイズのヒント
自分のプロジェクトへの応用例（1〜2パターン）
```

#### 各ファイルの学習の核心

| ファイル | 学習の核心 |
|---------|-----------|
| `01-grill-me.md` | 多軸レビューの構造化・重大度分類の設計 |
| `02-triage-issue-analysis.md` | 優先度判定ロジックの記述方法 |
| `03-improve.md` | 提案の「難易度×効果」マトリックスの実装 |

### 更新（4〜5ファイル）

| ファイル | 更新内容 |
|---------|---------|
| `docs/00-COVER.md` | Part 3 タイトル・学習時間を更新。合計時間を 9時間35分 → 9時間に修正 |
| `docs/04-skills-in-practice/09-problem-skill-mapping.md`（移動後） | 内部リンクを新パスに修正（`06-grill-me` → `01-grill-me` 等） |
| `docs/03-frameworks/03-frontend-design.md` | 末尾「次のステップ」から `06-grill-me` への参照を削除 |
| `docs/03-frameworks/04-ui-ux-pro-max.md` | 同上（`07-triage` 等への参照を削除） |
| `docs/04-skills-in-practice/01〜03.md`（書き換え後） | `samples/` 参照を Matt Pocock GitHub URL に差し替え |

---

## 変更後の構成

### Part 3（docs/03-frameworks/）

```
01-superpowers.md
02-gstack-overview.md
03-frontend-design.md
04-ui-ux-pro-max.md
```

- タイトル: **フレームワーク：Superpowers と設計スキル**
- 学習時間: **40分**（旧: 80分）

### Part 4（docs/04-skills-in-practice/）

```
01-grill-me.md              ← 書き換え（解析＋実行）
02-triage-issue-analysis.md ← 書き換え（解析＋実行）
03-improve.md               ← 書き換え（解析＋実行）
04-frontend-design.md       ← 変更なし
05-ui-ux-pro-max.md         ← 変更なし
06-baoyu-diagram.md         ← 変更なし
07-baoyu-infographic.md     ← 変更なし
08-baoyu-comic.md           ← 変更なし
09-problem-skill-mapping.md ← 03-frameworks から移動
```

### Part 5（docs/05-content-creation/）

```
01-baoyu-ecosystem.md       ← baoyu-skills-architecture の内容をマージ
02-content-skills-in-action.md
03-image-gen-backends.md
04-skill-pipeline.md
05-custom-skill-development.md
```

---

## 変更スコープまとめ

| 種類 | 件数 |
|------|------|
| 削除 | 6（samples 3ディレクトリ + docs 3ファイル） |
| 移動 | 2ファイル |
| 書き換え | 3ファイル |
| マージ | 1ファイル |
| 更新（リンク・メタ） | 4〜5ファイル |

---

## 未解決事項

なし。

---

## 次のステップ

このスペックを元に writing-plans スキルで実装プランを作成する。
