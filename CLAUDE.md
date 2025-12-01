# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## プロジェクト概要

Qiita CLI を使用してQiita記事を管理するリポジトリ。記事はMarkdownファイルとして `public/` ディレクトリに保存され、GitHub Actionsを通じて自動的にQiitaへ公開される。

## コマンド

```zsh
# 新規記事作成
pnpm qiita new <title>

# プレビュー（localhost:8888）
pnpm preview

# Qiitaから記事を同期
pnpm pull

# ログイン
pnpm login
```

## ディレクトリ構成

- `public/` - Qiita記事のMarkdownファイル
  - 各記事はYAML frontmatterを持つ（title, tags, private, id等）
- `.github/workflows/publish.yml` - main/masterへのpush時に記事を自動公開
- `qiita.config.json` - Qiita CLI設定

## 記事の構造

記事ファイルには以下のfrontmatterが必要：
```yaml
---
title: 記事タイトル
tags:
  - タグ1
  - タグ2
private: false
updated_at: ''
id: null  # 公開後にQiitaが自動設定
organization_url_name: null
slide: false
ignorePublish: false
---
```

## CI/CD

- main/masterブランチへのpushで自動公開
- `QIITA_TOKEN` シークレットの設定が必要
