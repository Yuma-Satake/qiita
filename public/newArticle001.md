---
title: 【Feature-Sliced Design】あの日みたディレクトリ構造の名前を僕達はまだ知らない。
tags:
  - React
  - Next.js
  - fsd
private: false
updated_at: '2025-12-03T22:48:13+09:00'
id: 0e9f62c6cf42d885e06c
organization_url_name: null
slide: false
ignorePublish: false
---

:::note
[これは何]
Feature-Sliced Design(FSD)というディレクトリ構造について解説し、Next.jsでの実装例とツール群を紹介する記事です
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
[【開催決定！】フロントエンドカンファレンス名古屋2026 を開催します🎉](https://note.com/fec_nagoya/n/ncf091310bc4f)

<img width="400px" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/8023873b-51e7-47df-af88-212bc45c2985.png" />

## あの日みたディレクトリ構造の名前を僕達はまだ知らない。

### Feature-Sliced Design（以下FSDという）

FSDはフロントエンドにおけるアーキテクチャ設計の手法と、それを実装に落とし込むためのツールチェーンを提供するものです。
具体的には以下のように、プロジェクト全体を6つの`Layer`として分割し、各`Layer`をさらに`Slice`、`Segment`といった単位で分割していきます。（`app`と`shared`のみ直接`Segment`を持つ）

<img width="550px" alt="Feature-Sliced Designの概念図 layer・slice・segmentの説明がある図" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/123b8b68-623e-4710-836e-0fb4392d2bc6.jpeg" />

### FSDとの出会い

2025年11月23日に開催された [TSKaigi Hokuriku 2025](https://hokuriku.tskaigi.org) のスポンサーLTにて、Feature-Sliced Design(FSD)についての発表を見ました。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">TSKaigi Hokuriku 2025のスポンサーLTで「フロントエンドアーキテクチャの設計方法論 Feature-Sliced Designの紹介」を発表しました！ <a href="https://t.co/tv3Hff5x5X">https://t.co/tv3Hff5x5X</a></p>&mdash; Sakamoto Keisuke (@motikoma) <a href="https://twitter.com/motikoma/status/1992442100428996895?ref_src=twsrc%5Etfw">November 23, 2025</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

ちょうど業務委託先で「Feature Based ディレクトリ構成って何が嬉しくて〜」みたいなことを言語化していたため、興味を持ちました。

この記事では、FSDの概要と、Feature Based ディレクトリ構成との比較、Next.jsでの実装例を紹介します。

## FSDを採用すると何が嬉しいの？

公式ドキュメントでは幾つかの利点が挙げられていますが、個人的には以下の**2点**が特に嬉しいと感じました

### ① 影響範囲がわかりやすくなって嬉しい

FSDではレイヤーの依存方向を一方通行に制限し、変更に対する予期しない箇所への影響を防ぐことができます。

### ② コードの均一化ができて嬉しい

後述のFeature Basedとの比較でも触れますが、FSDでは実装をどこに配置するかが明確に定義されており、かつそれを検証するツールも提供されています。
そのため、何をどこに実装すれば良いかが明確になり、コードベースの均一化が目指せます。

## FSDの概念

以下のドキュメントをベースにしながら説明していきます。
（FSDはコミュニティ主導のオープンソースのプロジェクトであり、そこで公開されているドキュメントです）

https://feature-sliced.design

### Layer（レイヤー）

FSDでは以下の6つの`Layer`を定義しています。

ポイントは**上位レイヤーは下位レイヤーのみを参照できる**という点です。
逆方向や同一レイヤー間の参照は禁止されています。

| レイヤー | 責務 | 呼び出し❌ | 呼び出し✅ |
|---------|------|:----:|:----:|
| app | アプリ全体の初期化（Routing、Providers） | | ↓ |
| pages | URLに対応する画面単位 | ↑ | ↓ |
| widgets | 大きな自己完結型UIブロック（Header、Sidebar等） | ↑ | ↓ |
| features | ユーザーインタラクション（form、API呼び出し等） | ↑ | ↓ |
| entities | ビジネスエンティティ（User、Product等のドメインモデル） | ↑ | ↓ |
| shared | アプリ全体で共有される基盤（ui、utils、types） | ↑ | |

この分割が最初の利点で言及した「影響範囲がわかりやすくなる」や「コードの均一化」に繋がっています。

※`processes`レイヤーは非推奨になっているため言及せず、6つのレイヤーとして説明します

#### 備考

- 全てのレイヤーを使う必要はなく、最小構成はapp、pages、sharedの3つが最小構成
- 上位のレイヤーからであれば、間のレイヤーを飛び越えて参照しても問題ない（例：pagesからentitiesを参照）

### Slice（スライス）

`Slice`は公式ドキュメントでは**ビジネスドメインによるコードの分割単位**と表現されていますが、実際には**アプリケーションにとっての意味単位での分割**と捉えた方がわかりやすいと考えています。

各レイヤーでの分割基準は以下のようになります：

- **pages** → ページ単位（home、dashboard等）
- **widgets** → UIブロック単位（header、sidebar等）
- **features** → 機能単位（auth、cart等）
- **entities** → エンティティ単位（user、product等）

Sliceはそれぞれのレイヤーの下に配置されます。ただし、`app`と`shared`はSliceを持たず、直接Segmentを配置します。

```
src/
├── app/                # Sliceなし（直接Segmentを持つ）
├── pages/
│   ├── home/           # Slice
│   └── dashboard/      # Slice
├── widgets/
│   ├── header/         # Slice
│   └── sidebar/        # Slice
├── features/
│   ├── auth/           # Slice
│   └── cart/           # Slice
├── entities/
│   ├── user/           # Slice
│   └── product/        # Slice
└── shared/             # Sliceなし（直接Segmentを持つ）
```

ルールとして、**同一レイヤー内の他のSliceを直接参照できません**。
これにより各スライスは低結合、高凝集を維持できます。

#### Public API Rule と バレルエクスポートについて

FSDでは各Sliceに`index.ts`（バレルファイル）を配置し、これをPublic APIとして定義し、カプセル化することが推奨されています。

https://feature-sliced.design/docs/reference/slices-segments

しかし、Next.jsにおいてバレルエクスポートはパフォーマンス上の問題を引き起こす可能性があることが知られています。
そのため個人的には、FSDの設計思想は理解しつつも、この辺りは実プロジェクトで採用する際に考慮し、`index.ts`を廃止して直接インポートするようにしてもいいのかなと考えています。

### Segment（セグメント）

各Slice内は**Segments**を技術的な視点で以下のように分割します。

セグメント名は**目的を表すべき**とされており、例えば`components`や`hooks`ではなく`ui`や`model`を使うべきとされています。

| セグメント | 役割 |
|-----------|------|
| ui/ | UIコンポーネント、スタイル |
| model/ | データスキーマ、ストア、ビジネスロジック |
| api/ | APIリクエスト関数、データ型  |
| lib/ | ヘルパー関数、ユーティリティ |
| config/ | フィーチャーフラグ、定数 |

公式ドキュメント中の説明の例では、以下のようなタグのリストをSegmentとして分割しています。

<img width="400px" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/900b272d-3846-4e8c-bff6-63f621d9b757.png" />

- **api/** →  利用可能なタグを取得する
- **ui/** → タグをチップとしてレンダリングする
- **model/** →  選択されたタグをクライアント上でステート管理する

## Next.js App Routerでの実装例

Next.js App RouterとFSDを組み合わせる場合の基本的な構成を紹介します

https://feature-sliced.design/docs/guides/tech/with-nextjs

### 基本的なディレクトリ構成

```
project-root/
├── app/                    # Next.js App Router
│   ├── dashboard/
│   │   └── page.tsx
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

Next.jsの`app/`フォルダはルーティングのみを担当し、FSDの各レイヤーは`src/`配下に配置します。

### 再エクスポートによる連携

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

### フォルダ名の競合問題

Next.jsの`app`や`pages`というフォルダ名がFSDのレイヤー名と競合します。
FSD公式では以下の対策が推奨されています。

- FSDのレイヤーは`src/`配下に配置する
- プロジェクトルートに空の`pages/`フォルダを配置する（Next.jsが`src/pages`をPages Routerとして認識するのを防ぐため）

```
project-root/
├── app/                    # Next.js App Router
├── pages/                  # 空フォルダ（README.mdのみ）
│   └── README.md
└── src/
    ├── app/                # FSD appレイヤー
    ├── pages/              # FSD pagesレイヤー
    └── ...
```

## ツールチェーン

FSDには思想を実際の実装に落とし込むために、コードベースを自動チェックするツールが用意されています。

### ESLint Rules

`@feature-sliced/eslint-config`はESLintのルールとして、FSDのルールに沿って依存関係をチェックしてくれます。

https://github.com/feature-sliced/eslint-config

※現時点でESLint v9のフラットコンフィグに対応していないため、ESLint v8を使用する必要があります
※Biomeで同様のルールを提供するプラグインを探しましたが、現時点では見つかりませんでした

#### 導入

```bash
npm install -D @feature-sliced/eslint-config eslint-plugin-import eslint-plugin-boundaries
```

```json
{
  "extends": ["@feature-sliced"]
}
```

#### 実際の出力例

以下のように、FSDのルールに違反している場合にエラーが表示されます。

> "shared" is not allowed to import "features" | See rules: https://feature-sliced.design/docs/reference/layers/overview eslintboundaries/element-types


<img width="400px" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/4764eebb-23da-4757-bcf5-8ba8c51a7680.png" />



### Steiger

`steiger`はFSD用のアーキテクチャリンターです。
ESLintとは異なり、ファイル・フォルダ構造自体を検証します。

https://github.com/feature-sliced/steiger

#### 導入

```bash
npm i -D steiger @feature-sliced/steiger-plugin
npx steiger ./src
```

#### 実際の出力例

> ┌ src/shared/ui/BadComponent.tsx
✘ Forbidden import from higher layer "features".
│
└ fsd/forbidden-imports

↑ sharedレイヤーから上位レイヤーであるfeaturesをインポートしているため、エラーが出ています。

> ┌ src/entities/user
✘ This slice has only one reference in slice "widgets/header". Consider merging them.
│
└ fsd/insignificant-slice

↑ entities/userスライスがwidgets/headerからしか参照されていないため、統合を検討するよう提案されています。

<img width="400px" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/78850ef0-c03a-4598-a102-2bfe8e48ab9b.png" />

## 最後に

普段は Feature Based ディレクトリを採用しているプロジェクトに関わっていることが多いですが、コードベースをドメインベースに整理する思想は共通している上で、それを明確にルールやツールでサポートしている点はFSDの魅力だと感じました。

一方で学習コストは高く、またNext.jsとの組み合わせにおいては少し面倒な部分もあるため、プロジェクトの規模やチームのメンバーの状況に応じて採用を検討するのが良いと感じました。

## フロントエンドカンファレンス名古屋について

2026年5月9日（土） にフロントエンドカンファレンス名古屋を開催します！
名古屋では初のフロカンになるので、ぜひWatchしてください🦘

https://note.com/fec_nagoya/n/ncf091310bc4f

## 資料

https://feature-sliced.design/

https://feature-sliced.design/docs/reference/slices-segments

https://feature-sliced.design/docs/guides/tech/with-nextjs

https://speakerdeck.com/motikoma/tskaigi-hokuriku-2025-hurontoentoakitekutiyanoshe-ji-fang-fa-lun-feature-sliced-designnoshao-jie

https://github.com/feature-sliced/eslint-config

https://github.com/feature-sliced/steiger
