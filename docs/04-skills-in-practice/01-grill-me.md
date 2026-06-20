# 4-1: grill-me — コードレビュースキル（Matt Pocock）

> **学習時間**: 25分 | **難易度**: ⭐⭐⭐ | **カテゴリ**: 品質検証

## このスキルについて

**grill-me** は Matt Pocock 氏が公開するコードレビュースキルです。コードの品質を「可読性」「パフォーマンス」「セキュリティ」「保守性」の4軸で徹底的にレビューし、重大度付きの改善提案を返します。

- **出典**: [mattpocock/skills — grill-me](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md)
- **用途**: PR レビュー前のセルフチェック、コード品質の統一基準、ジュニア開発者への教育

## なぜこのスキルが必要か

PR レビューで「なんとなく気になるけど、どう言えばいいか分からない」という場面はないですか？重大度の基準が暗黙知になっていると、指摘する側も受ける側も優先度の判断に迷い、対話が生産的になりません。grill-me は評価軸と重大度を SKILL.md で明文化し、レビューを「感覚」から「基準」へ変えます。

```mermaid
flowchart LR
    A["Phase A<br>SKILL.md を読む"] --> B["Phase B<br>インストール・動作確認"]
    B --> C["Phase C<br>解析と実行結果の照合"]
```

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

## Phase C: 解析と実行結果の照合

実行結果を見ながら、SKILL.md の設計と照らし合わせる問いです：

1. 実際に返ってきた重大度分類は SKILL.md の基準と一致しているか？
2. `positive_feedback` はどのタイミングで返ってきたか？どのコードが評価されたか？
3. `focus_areas: ["security"]` に絞った場合、出力はどう変わるか？

## この SKILL.md から学べる設計パターン

自分のスキルを作るときに応用できる設計の視点：

1. **多軸評価の独立性** — 評価を複数の軸（可読性・パフォーマンス・セキュリティ・保守性）に分けることで、`focus_areas` による絞り込みが可能になる。軸を独立させて定義する設計が再利用性を高める。
2. **重大度の三段階** — 「問題あり/なし」ではなく Critical / Major / Minor を出力に含めると、受け取る側が次のアクションを自分で判断できる。スキルの出力を「判断の材料」として設計するパターン。
3. **ポジティブフィードバックの組み込み** — 指摘だけでなく `positive_feedback` も返す設計は、スキルの出力を一方的な批評でなく対話にする。自分のスキルに「良い点の明示」を加えると、使い続けたいと思われやすくなる。

## カスタマイズのヒント

**観点を追加する**
SKILL.md に `accessibility`（WCAG 準拠チェック）軸を追加することで、フロントエンド特化のレビューが可能になります。

**重大度基準を調整する**
チームのコーディング規約に合わせて Critical の定義を変更すると、PR マージ判断の自動化に活用できます。

## 次のステップ

→ [4-2: triage — Issue 分析スキル](02-triage-issue-analysis.md)
→ [4-9: 問題 × スキル解決マッピング](09-problem-skill-mapping.md)
