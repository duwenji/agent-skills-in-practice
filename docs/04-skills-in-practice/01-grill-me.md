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
