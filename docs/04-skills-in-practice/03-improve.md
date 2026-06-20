# 4-3: improve — コード改善スキル（Matt Pocock）

> **学習時間**: 25分 | **難易度**: ⭐⭐⭐ | **カテゴリ**: リファクタリング

## このスキルについて

**improve** は Matt Pocock 氏が公開するコード改善スキルです。既存コードを分析し、パフォーマンス最適化・リファクタリング・モダナイゼーションの3観点から、難易度と期待効果の評価付きで改善提案を返します。

- **出典**: [mattpocock/skills — improve](https://github.com/mattpocock/skills/blob/main/skills/productivity/improve/SKILL.md)
- **用途**: レガシーコードのモダナイゼーション、パフォーマンスボトルネックの特定、技術負債の返済計画

---

## なぜこのスキルが必要か

「このコード、なんか遅い気がするけど、どこから手をつければ？」—— 問題の特定から改善案の優先順位づけまで、手作業では時間がかかります。improve は「難易度×効果」マトリックスで改善案を整理し、今すぐ着手できる `quick_wins` から長期的な改善まで、具体的な実行計画として返します。

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

## この SKILL.md から学べる設計パターン

1. **難易度×効果マトリックス** — 改善案を列挙するだけでなく `quick_wins`（難易度低・効果高）と `long_term` に分類することで、出力が「実行計画」になる。スキルの出力を「何ができるか」ではなく「何から始めるか」に変換する設計。
2. **制約を入力として受け取る** — `constraints` パラメータで現実的な条件（IE11対応、bundle size制限など）を注入することで、「理想論」ではなく「実現可能な改善」を返せる。プロジェクト固有の制約に対応するパターン。
3. **観点の絞り込み機能** — `improvement_type` で特定の観点だけを分析できる設計は、大きなスキルを部分的に使える柔軟性を生む。スキルを「全か無か」でなく「必要な部分だけ使える」設計にすることで、適用範囲が広がる。

---

## カスタマイズのヒント

**チーム標準の規約を注入する**
関数の最大行数・命名規則などをリファクタリング基準として SKILL.md に追記すると、コードレビューとの整合性が高まります。

**grill-me との連携**
grill-me でレビュー → improve で改善案取得 → 実装 のサイクルを組むことで、品質向上ループを自動化できます。

---

## 次のステップ

→ [3-3: frontend-design — フロントエンド設計支援スキル](../03-frameworks/03-frontend-design.md)
→ [4-9: 問題 × スキル解決マッピング](09-problem-skill-mapping.md)
