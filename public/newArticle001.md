---
title: 【Feature-Sliced Design】あの日みたディレクトリ構造の名前を僕達はまだ知らない。
tags:
  - React
  - Next.js
  - fsd
private: true
updated_at: '2025-12-03T14:32:35+09:00'
id: 0e9f62c6cf42d885e06c
organization_url_name: null
slide: false
ignorePublish: false
---

:::note
[これは何]
Feature-Sliced Design(FSD)というディレクトリ構造を、主流のFeature-basedと比較しながら解説したり、Next.jsでの実装例を紹介したりする記事です
:::

:::note
[対象読者]
業務でWebアプリケーションのフロントエンド開発に携わっているエンジニアの方
:::

## 自己紹介

### Yuma Satake

プロフィールに「Webフロントやめます」って書いて3年が経ちました
普段はWebフロントエンドエンジニアをしています

- 名前：佐竹友真
- 所属：26卒@DMM.com
- 領域：Web 開発
- 趣味：車・イベント運営
- Twitter：[Yuma Satake](https://x.com/yuma_satake22)

<img width="200px" alt="Yuma Satakeのアイコンのサボテンでできた鳥の画像" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/aaf685a0-0af0-5e5b-92e9-a6f0275812fc.jpeg"/>

フロントエンドカンファレンス名古屋を立ち上げました！
▼是非ウォッチして下さい！
[【開催決定！】フロントエンドカンファレン名古屋2026 を開催します🎉](https://note.com/fec_nagoya/n/ncf091310bc4f)

<img width="400px" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/8023873b-51e7-47df-af88-212bc45c2985.png" />

## あの日みたディレクトリ構造の名前を僕達はまだ知らない。

### Feature-Sliced Design（以下FSDという）

FSDはフロントエンドにおけるアーキテクチャ設計の手法と、それを実装に落とし込むためのツールチェーンを提供するものです。
具体的には以下のように、プロジェクト全体を6つの`Layer`として分割し、各`Layer`をさらに`Slice`、`Segment`といった単位で分割していきます。（`app`と`shared`のみ直接`Segment`を持つ）

<img width="550px" alt="Feature-Sliced Designの概念図 layer・slice・segmentの説明がある図" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/123b8b68-623e-4710-836e-0fb4392d2bc6.jpeg" />

### FSDとの出会い

2025年11月23日に開催された [TSKaigi Hokuriku 2025](https://hokuriku.tskaigi.org) のスポンサーLTにて、Feature-Sliced Design(FSD)についての発表を見ました。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">TSKaigi Hokuriku 2025のスポンサーLTで「フロントエンドアーキテクチャの設計方法論 Feature-Sliced Designの紹介」を発表しました！ <a href="https://t.co/tv3Hff5x5X">https://t.co/tv3Hff5x5X</a></p>&mdash; Sakamoto Keisuke (@motikoma) <a href="https://twitter.com/motikoma/status/1992442100428996895?ref_src=twsrc%5Etfw">November 23, 2025</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

ちょうど業務委託先で「Feature Based ディレクトリ構成って何が嬉しくて〜」みたいなことを言語化していため、興味を持ちました。
この記事では、FSDの概要と、Feature Based ディレクトリ構成との比較、Next.jsでの実装例を紹介します。

## FSDの基本概念

以下のドキュメントをベースにしながら説明していきます。
（FSDはコミュニティ主導のオープンソースのプロジェクトであり、そこで公開されているドキュメントです）

https://feature-sliced.design

### Layer（レイヤー）

FSDでは以下の6つのレイヤーを定義しています。
ポイントは**上位レイヤーは下位レイヤーのみを参照できる**という点です。逆方向や同一レイヤー間の参照は禁止されています。

| レイヤー | 責務 | 呼び出し❌ | 呼び出し✅ |
|---------|------|:----:|:----:|
| app | アプリ全体の初期化（ルーティング、グローバルストア、providers） | | ↓ |
| pages | URLに対応する画面単位 | ↑ | ↓ |
| widgets | 大きな自己完結型UIブロック（Header、Sidebar等） | ↑ | ↓ |
| features | ユーザーインタラクション（form、API呼び出し等） | ↑ | ↓ |
| entities | ビジネスエンティティ（User、Product等のドメインモデル） | ↑ | ↓ |
| shared | アプリ全体で共有される基盤（ui、utils、types） | ↑ | |

#### 備考

- 全てのレイヤーを使う必要はなく、最小構成は**app、pages、shared**の3つが最小構成
- 上位のレイヤーからであれば、間のレイヤーを飛び越えて参照しても問題ありません（例：pagesからentitiesを参照）

### Slice（スライス）

Sliceは**ビジネスドメインによるコードの分割単位**です。
例えばECサイトなら`user`、`product`、`cart`、`order`といったスライスに分かれます。

```
features/
├── auth/          # 認証に関する機能
├── cart/          # カートに関する機能
└── checkout/      # 決済に関する機能
```

重要なルールとして、**同一レイヤー内の他のSliceを直接参照できません**。
これにより各スライスは低結合・高凝集を維持できます。

### Segment（セグメント）

各Slice内は**Segments**で技術的目的ごとに分割されます。

| セグメント | 役割 |
|-----------|------|
| ui/ | UIコンポーネント、スタイル |
| model/ | データスキーマ、ストア、ビジネスロジック |
| api/ | APIリクエスト関数、データ型 |
| lib/ | ヘルパー関数、ユーティリティ |
| config/ | フィーチャーフラグ、定数 |

セグメント名は**目的（why）を表すべき**とされています。
`components`や`hooks`ではなく`ui`や`model`を使うのがFSD流です。

### Public API

各Sliceは`index.ts`（バレルファイル）で**Public API**を定義し、外部に公開するインターフェースを明示します。

```typescript
// features/auth/index.ts
export { LoginForm } from './ui/LoginForm';
export { useAuth } from './model/hooks';
export type { AuthState } from './model/types';
```

これにより内部実装を隠蔽し、リファクタリングの自由度を確保できます。
外部からは`import { LoginForm } from '@/features/auth'`のようにアクセスします。

## Feature Basedとの比較
Next.jsでよく使われるFeature Basedディレクトリ構成とFSDを比較してみましょう。

### Feature Basedディレクトリ構成

Feature Basedは機能単位でディレクトリを分割する考え方です。
一般的には以下のような構成になります。

```
src/
├── features/
│   ├── auth/
│   │   ├── components/
│   │   ├── hooks/
│   │   └── api/
│   └── user/
│       ├── components/
│       ├── hooks/
│       └── api/
├── components/     # 共通コンポーネント
├── hooks/          # 共通hooks
└── utils/          # ユーティリティ
```

Feature Basedの良い点は**直感的で学習コストが低い**ことです。
「この機能に関するコードはこのフォルダ」というシンプルなルールで運用できます。

### FSDとの違い

| 観点 | Feature Based | FSD |
|------|---------------|-----|
| レイヤーの概念 | なし（フラット） | 6層の階層構造 |
| 依存関係のルール | 暗黙的 | 上位→下位のみ（厳密） |
| 共通コンポーネント | `components/`に配置 | `shared/ui/`に配置 |
| ページコンポーネント | `pages/`または`features/`内 | `pages/`レイヤーに明確に分離 |
| ウィジェット（複合UI） | 明確な置き場がない | `widgets/`レイヤー |
| ツールによる検証 | なし | ESLint config、Steiger |

最大の違いは**依存関係のルールが明文化されているかどうか**です。

Feature Basedでは「featureAからfeatureBを参照していいのか？」という問いに対する明確な答えがありません。
FSDでは「同一レイヤー間の参照は禁止」というルールがあり、ツールで自動検証できます。

### どちらを選ぶべきか

| プロジェクト規模 | 推奨 |
|-----------------|------|
| 小規模（数画面） | Feature Based |
| 中規模 | どちらでも可（チームの習熟度次第） |
| 大規模・長期運用 | FSD |

FSDは学習コストがかかりますが、**大規模プロジェクトでの保守性とスケーラビリティ**に優れています。
逆に小規模プロジェクトではオーバーヘッドがメリットを上回る可能性があります。

## Next.jsでの実装例

Next.js App RouterとFSDを組み合わせる場合、`app`と`pages`というフォルダ名が競合します。
公式推奨の解決策は以下の構造です。

```
project-root/
├── app/                    # Next.js App Router
│   ├── dashboard/
│   │   └── page.tsx        # FSD pagesから再エクスポート
│   └── layout.tsx
└── src/
    ├── app/                # FSD appレイヤー
    │   ├── providers/
    │   └── styles/
    ├── pages/              # FSD pagesレイヤー
    │   └── dashboard/
    │       ├── ui/
    │       │   └── DashboardPage.tsx
    │       └── index.ts
    ├── widgets/
    ├── features/
    ├── entities/
    └── shared/
```

Next.jsのルートファイルからFSDのpagesをインポート・再エクスポートします。

```typescript
// app/dashboard/page.tsx（Next.js側）
export { DashboardPage as default } from '@/pages/dashboard';
```

```typescript
// src/pages/dashboard/index.ts（FSD側のPublic API）
export { DashboardPage } from './ui/DashboardPage';
```

```tsx
// src/pages/dashboard/ui/DashboardPage.tsx
import { Header } from '@/widgets/header';
import { UserProfile } from '@/features/user-profile';
import { Button } from '@/shared/ui';

export const DashboardPage = () => {
  return (
    <div>
      <Header />
      <main>
        <UserProfile />
        <Button>アクション</Button>
      </main>
    </div>
  );
};
```

このように、Next.jsのルーティング機構とFSDのレイヤー構造を分離することで、両方のメリットを活かせます。

### バレルエクスポートについて

FSDでは各SliceにPublic APIとして`index.ts`（バレルファイル）を配置することが推奨されています。
しかし、Next.jsにおいてバレルエクスポートはパフォーマンス上の問題を引き起こす可能性があることが知られています

個人的には、FSDの設計思想は理解しつつも、この辺りは実プロジェクトで採用する際に考慮し、`index.ts`を廃止して直接インポートするようにしてもいいのかなと考えています。

## ツールチェーン

FSDには思想を実際の実装に落とし込むために、コードベースを自動チェックするツールが用意されています。

### ESLint Rules

`@feature-sliced/eslint-config`はESLintのルールとして、FSDのルールに沿って依存関係をチェックしてくれます

https://github.com/feature-sliced/eslint-config


#### 導入

```bash
npm install -D @feature-sliced/eslint-config eslint-plugin-import eslint-plugin-boundaries
```

```json
{
  "extends": ["@feature-sliced"]
}
```

### Steiger

`steiger`は2024年に公開されたFSD専用のアーキテクチャリンターです。ESLintとは異なり、ファイル・フォルダ構造自体を検証します。

https://github.com/feature-sliced/steiger

#### 導入

```bash
npm i -D steiger @feature-sliced/steiger-plugin
npm steiger ./src
```

## フロントエンドカンファレンス名古屋について

2026/5/9 にフロントエンドカンファレンス名古屋を開催します！
名古屋では初のフロカンになるので、ぜひNoteを見て頂けると嬉しいです🦘

https://note.com/fec_nagoya/n/ncf091310bc4f

## 最後に

Feature-Sliced Designは、フロントエンドの大規模化に伴う構造的な複雑性を制御するための方法論です。

- 6つのレイヤーで責務を明確に分離
- Slice（ビジネスドメイン）とSegment（技術的目的）による二軸の分割
- Public APIによるカプセル化
- ツールによる依存関係の自動検証

Feature Basedと比較すると学習コストは高いですが、**依存関係の明確化**と**ツールによる自動検証**という点で大きなアドバンテージがあります。

「なんとなくFeature Basedっぽい構成にしている」というチームは、一度FSDの考え方を学んでみると新しい発見があるかもしれません。

## 資料

https://feature-sliced.design/

https://speakerdeck.com/motikoma/tskaigi-hokuriku-2025-hurontoentoakitekutiyanoshe-ji-fang-fa-lun-feature-sliced-designnoshao-jie

https://github.com/feature-sliced/eslint-config

https://github.com/feature-sliced/steiger
