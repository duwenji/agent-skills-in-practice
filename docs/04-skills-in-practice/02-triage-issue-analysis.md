# 4-2: triage — Issue 分析スキル（Matt Pocock）

> **学習時間**: 25分 | **難易度**: ⭐⭐⭐ | **カテゴリ**: 優先順位付け

## このスキルについて

**triage** は Matt Pocock 氏が公開する Issue 分析スキルです。GitHub Issue の内容を解析し、優先度（P0〜P3）の判定、カテゴリ分類、影響範囲の特定、対応推奨事項を自動生成します。

- **出典**: [mattpocock/skills — triage](https://github.com/mattpocock/skills/blob/main/skills/productivity/triage/SKILL.md)
- **用途**: 新規 Issue の自動トリアージ、バックログ整理、スプリント計画の最適化

---

## なぜこのスキルが必要か

「このバグ、どれくらい急いで直すべきか」を毎回手作業で判断していませんか？担当者によって優先度の解釈が変わると、対応漏れや重複が起きます。triage は P0〜P3 の判定基準を SKILL.md に明文化し、担当者の経験に依存しない一貫したトリアージを実現します。

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

## この SKILL.md から学べる設計パターン

1. **コンテキスト注入による汎用性** — スキル本体は汎用ロジックとして保ち、`project_context` で個別の文脈を外から注入する設計は、1つのスキルを複数プロジェクトで再利用可能にする。スキルを「ロジック」と「文脈」に分離する考え方。
2. **必須/オプション入力の分離** — `issue_title`/`issue_body` を必須、`labels`/`project_context` をオプションにすることで、最低限の情報でも動作しつつ詳細情報があれば精度が上がる。スキルの「エントリーハードル」を下げながら品質も上げる設計。
3. **不足情報の自動検出** — 入力が不十分なときに「何が足りないか」を返す設計は、ユーザーとのやり取りを通じてより良い出力を引き出す。スキルを「完成品」でなく「対話のパートナー」として設計するパターン。

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
