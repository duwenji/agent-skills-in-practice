# QUICK REFERENCE

| 読者 | 最初に読む資料 | 目的 |
|------|---------------|------|
| 初学者 | `docs/00-fundamentals/01-ecosystem-overview.md` | Agent Skills エコシステムの全体像をつかむ |
| Claude Code ユーザー | `docs/01-skill-creation/01-what-are-agent-skills.md` | Agent Skills の基本を理解する |
| ハンズオン重視 | `docs/01-skill-creation/02-skill-creator-hands-on.md` | `/skill-creator` で最初のスキルを作る |
| 実践スキル利用 | `docs/04-skills-in-practice/` | 8つの実践スキルをすぐ使う |
| チーム導入担当 | `docs/02-discovery/03-sharing-team-deployment.md` | スキルの共有・展開方法を学ぶ |
| コンテンツ生成 | `docs/05-content-creation/01-baoyu-ecosystem.md` | baoyu-skills で画像・図解・マンガを生成 |
| カスタムスキル開発 | `docs/05-content-creation/05-custom-skill-development.md` | baoyu流のスキル設計パターンを学ぶ |

## 5層構造クイックマップ

```
発見層  ── Find Skills / gh skill / skill.sh / baoyu-skills 発見
作成層  ── Claude Code /skill-creator + 手書き SKILL.md
概念層  ── Superpowers（OSSプラグイン）/ GStack / baoyu-skills アーキテクチャ
実践層  ── grill-me / triage / improve / frontend-design / ui-ux-pro-max / baoyu-*
応用層  ── コンテンツ生成パイプライン / 画像生成バックエンド / カスタムスキル開発
```

## スキル配置場所早見表

| プラットフォーム | 個人用 | プロジェクト用 |
|----------------|--------|--------------|
| **Claude Code** | `~/.claude/skills/<name>/SKILL.md` | `.claude/skills/<name>/SKILL.md` |
| **GitHub Copilot** | （個人設定で管理） | `.github/skills/<name>/SKILL.md` |
