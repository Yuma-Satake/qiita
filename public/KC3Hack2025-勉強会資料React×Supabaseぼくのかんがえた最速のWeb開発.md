---
title: 【KC3Hack2025-勉強会資料】React×Supabase ぼくのかんがえた最速のWeb開発
tags:
  - 'Supabase'
  - 'React'
  - '初学者'
  - 'フロントエンド'
  - 'TypeScript'
private: false
updated_at: ''
id: null
organization_url_name: null
slide: false
ignorePublish: false
---
:::note
[これは何]
KC3Hack2025の勉強会資料
:::
:::note warn
[外部公開にあたって]
この記事は初学者向けに短時間でツール群や概念を説明するために、意図的に言葉の解像度を落としたり、誇張した表現を行なっている箇所があります
:::


## 講師自己紹介

### Yuma Satake

- 名前：佐竹友真
- 学校：名古屋工学院専門学校(3年)
- 所属：Matsuriba・TechUni
- 領域：Web
- 趣味：車・旅行
- Twitter：[Yuma Satake | Matsuriba🏮
](https://x.com/yuma_satake22)

<img width="200px" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/aaf685a0-0af0-5e5b-92e9-a6f0275812fc.jpeg">

- 受賞歴（~~講師なんて、こんなもんなんぼ書いてあってもええですからねぇ~~）
   - 技育CAMP Vol.10（入賞）
   - 技育CAMP Vol.11（入賞）
   - 関西ビギナーズハッカソン（最優秀賞）
   - 技育CAMPアドバンス Vol.1 （大賞）
   - カラビナハッカソン （カラビナ賞受賞）
   - マイナポータルハッカソン （本戦出場）
   - 技育CAMP Vol.5（最優秀賞）
   - 名古屋Web3ハッカソン（4冠）
   - 技育CAMPアドバンス Vol.3（GMO賞）
   - 技育展2023（サイバーエージェント賞受賞）
   - 技育CAMP Vol.5（DeNA賞）
   - etc...


## 初めに

### 最速のWeb開発

#### 人類はなぜ速さを求めるのか

<img width="400px" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/30757e84-b2f5-465f-889f-b2f911ea1055.jpeg" />

> **完璧を目指すよりまず終わらせろ**
> Done is better than perfect
> (Meta CEO Mark Zuckerberg)

#### 素早くプロダクトを開発する事はなぜ重要？

- **改善サイクルの重要性**：最初から完璧なものを作ることは不可能で、早くリリースし、ユーザーのフィードバックを受け取り、改善を繰り返すことが重要
- **競争優位性**：AIツールが発展した現代では、素早くアイデアをプロダクトにできるようになっているため、早い段階でリリースすることが重要

### 今回紹介するスタック

キックオフ後、各チームのチャットで登場していた技術（以下）

- Next.js
- Django
- Android
- Unity
- Flutter
- etc...

**ノーコードツールを除いて、最速でWebアプリを開発するためのスタックを紹介します（諸説あり）**

- **React**：Webフロントエンドのフレームワーク
- **Supabase**：リレーショナルデータベースを簡単に使えるBaaS

## この勉強会の目的

この勉強会の目的は

:::note alert
React × Supabase を使ったプロダクトのコードが書けるようになる
:::

ではなく

:::note info
React や Supabase について知り、自分たちのチームの技術選定の幅を広げる
:::

です。

React も Supabase も、ネット上に沢山良質な記事が転がっています！
ぜひ今日の勉強会を通して"使ってみたい！"と思ったらそれらの記事を参考に開発に取り入れてみて下さい

### お品書き

ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
① **Web？モバイル？**：Webアプリとモバイルアプリの違いと選定
② **React**：選ばれたのはReactでした
③ **Supabase**：？？？「それってFirebaseじゃダメなんですか？」
④ **番外編**：最速と言ったからにはお見せしましょうライブコーディング
ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

### 注意

この記事では時間の都合で以下の内容などを省略しています。

- Webの基本的な仕組み
- 実際のコード
- DBの基本的な仕組み
- ホスティング

より初学者向けの内容については、以下の過去勉強会資料をご覧ください。

https://qiita.com/Yuma-Satake/items/06ef79d60ee7d95a0255


## ① Web？モバイル？

### Webとモバイルの比較

Webアプリにするのか、モバイルアプリにするのか、それが問題だ。

| 特徴              | Webアプリケーション                  | モバイルアプリケーション          
|-----------------|----------------------------------|----------------------------|
| アクセス方法         | ブラウザ                      | デバイスにインストール      |
| デバイス互換       | 全てのデバイスで利用可能            | 対応したOSのみ             |
| 更新方法           | サーバー側で自動更新               | ユーザーが手動で更新         |
| 使い始め        | URLを踏んで利用開始   | ストアからインストールして利用     |
| オフライン利用       | 基本的にインターネット接続が必要 | オフラインでも一部機能が利用可能|

**今から開発したいサービスはどんな特徴を持ってそう？**
例えば→（そもそも使われるのはPC？スマホ？・重い処理はある？・センサーが必要？）

### それぞれの長所（一部）

#### 🔥 Webアプリの長所
- **スタートの手軽さ**：リンクを踏むだけで使い始められる
- **デバイス互換性**：ブラウザが使える環境なら、どんな端末でもアクセス可能
- **軽量な使用**：ストレージなどを圧迫する事なく使用できる

#### 🔥 モバイルアプリの長所
- **頻繁な利用に強い**：アプリとしてワンタップでアクセスできる
- **パフォーマンスの高さ**：デバイスの性能を直接引き出せる
- **センサー等の活用**：加速度センサーなどを活かしたサービス開発ができる

<br>

✅ サービスの特徴や使われ方によって、どちらとして開発をすべきかは決まってくる

```ts
if(PCで使われそう）return Webの方が良い
if(リンクから簡単に使ってもらいたい）return Webの方が良い
if(ゲームなど、高いパフォーマンスが必要ない）return Webの方が良い
if(センサー等を使ったサービスではない）return Webの方が良い

return モバイルアプリケーションとして開発しよう
```

[補足]
もちろん勉強目的でモバイルアプリを開発する事は素晴らしいことだが、一般論としてモバイルアプリケーションは開発/運用コストが高く、Webアプリケーションで済むのであればWebアプリケーションとして展開した方が良いという考え方もある

→ 何故モバイルアプリとして開発をしました、が言えると考えられたサービスである事がわかる

## ② React

ここではフロントエンド（ここではWeb画面を描画するための技術としての意）として、最速を目指すために何故Reactをお勧めするのかを説明します。

### それって◯◯じゃダメなんですか？

同じフロントエンド開発のための技術や、フルスタックフレームワークとしての候補としては以下が挙げられそうです

1. **フルスタックフレームワークじゃダメなんですか？**：Django・Ruby on Rails・Laravel
2. **他のフロントエンドフレームワークじゃダメなんですか？**：Vue・Next.js・Angular
3. **Flutterじゃダメなんですか？**：Flutter

※ここではユースをイメージして、Next.jsをフロントエンドフレームワークに分類しています

#### ① フルスタックフレームワークじゃダメなんですか？

**Q：** Django・Ruby on Rails・Laravel などでも同様にWebの画面を記述することができますが、それでは最速でないのでしょうか？
**A：** フロントとバックの分離による開発速度の向上と、周辺技術/情報の豊富さからReactをお勧めします

<img width="400px" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/c5325c5c-8938-4449-a66b-9fe8e0213363.png" />

**フロントとバックの分離による開発速度の向上**

ハッカソンやプロダクト開発などにおいて、複数人で開発する場合、フロントエンドとバックエンドを分離することで、開発スピードを上げることができるため。

#### ② 他のフロントエンドフレームワークじゃダメなんですか？

**Q：** Vue・Next.js・Angular など、他のフロントエンドフレームワークではなく、Reactを選ぶ理由は何でしょうか？
**A：** Reactは、フロントエンドフレームワークの中で最も使用されており、Next.js等に比べて薄く使え、かつ周辺技術/情報が豊富であるためお勧めします

<img width="400px" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/269c5e18-3a05-4c28-b3fc-9c95d9bcd881.png" />

**Next.jsとの比較**

多くのチームでNext.jsが話題に上がっているのを見受けますが、個人的にはNext.jsよりReactをお勧めします。

【Nextのメリット】

- **SSR（サーバーサイドレンダリング）が使える**：SEO対策やパフォーマンス向上に有効
- **APIルートが使える**：APIのエンドポイントを簡単に作成できる

【Nextのデメリット】

- **学習コストの高さ**：Next.jsには独自の仕様が多く、設定せずとも多くのことができる反面、知らないとそれらにハマることが多い
- **インフラ面**：最新のNext.jsでは基本的にSSRできるホスティング先が必要となるため、より多くのホスティング手段が選べ、かつコストが低いReactをお勧めします（ただハッカソンでVercelに投げる場合はその限りではない）

#### ③ Flutterじゃダメなんですか？

**Q：** Flutterは、Webアプリケーションの開発にも対応しているため、Flutterを使ってWebアプリケーションを開発することはできないのでしょうか？
**A：** Flutterは、Webアプリケーションの開発にも対応していますが、SEOやパフォーマンス、周辺技術/情報の豊富さからReactをお勧めします

<img width="400px" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/9e77d24e-0540-454c-8f95-a26ffd367572.png" />

**めちゃFlutter勉強会のスライドにあったので割愛😇**

![Screenshot 2025-02-13 at 18.33.04.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/6b9952d4-eaae-411c-b270-f5aabb5163f7.png)



## ③ Supabase

### 🚀 `Supabase`とは

`Supabase`とは、`Backend as a Service（BaaS）`の一つ
認証・DB・関数実行などの本来バックエンドで実行する内容をフロントエンドのコードにまとめて記述することができるようになる。

https://supabase.com

#### 特定の値を`Create（Insert）`する
```ts
await supabase.from(('game_scores_table').insert({
  player_nickname: nickName,
  score: playScore
})
```

#### 特定の情報を`Read（Get）`する
全部のスコアを`score`で並び替えて、`limit`件上限で取得
```ts
const { data } = await supabase
    .from('game_scores_table')
    .select('*')
    .order('score', { ascending: false })
    .limit(limit);
```

#### 特定の値を`Update(Upsert)`する
`plyer_nickname`が被っている場合には上書きする
```ts
await supabase.from('game_scores_table').upsert(
    {
      player_nickname: nickName,
      score,
    },
    {
      onConflict: 'player_nickname',
    }
);
```

#### 古い値を`Delete`する
```ts
await supabase.from('game_scores_table').delete().match({
    player_nickname: player_nickname,
})
```

### 🚀 `GUI`でDB構築

#### DBムズイ

一般的にRDB（リレーショナルデータベース）を作成する場合には、SQLを実行してDBを作成する。

↓↓↓ 使っている`game_scores_table`を作成する`SQL`
```sql
CREATE TABLE game_scores_table (
    score_id UUID PRIMARY KEY,
    player_nickname TEXT NOT NULL,
    score INT8 NOT NULL,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
```

- `SQL`わからん...
- いちいちコマンドを叩かないと状況がわからない

→ 初学者には普通にむずい😇

#### `Supabase`はGUI上でDBを作成できる

<img width="300px" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/95eb51c2-5b42-0b85-325e-1129fba81a9b.png" />


### 🪐Supabaseの活用
#### [ 認証機能 ]
`Googleでログイン`や`Githubでログイン`といったよくあるログインを簡単につくれる
（ハッカソンではまじでおすすめ。認証部分だけBaaSに投げてるチームもよくみる）

https://supabase.com/docs/guides/auth

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/ba1fee35-10d2-0537-d394-59b502817110.png)


#### [ リアルタイムDB ]
通常の`WebAPI`は、呼び出さないとデータが更新されない。
`WebSocket`と呼ばれる技術を簡単に使うことができ、同時編集や、リアルタイム対戦などが実装できる。
（カーソルの位置やプレイヤーの位置をリアルタイムで反映させられる）

https://supabase.com/docs/guides/realtime

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/72445099-4aa1-76b7-9d9f-38855fbb0e98.png)

# 最後に

今回は

- Webサービスはモバイルアプリと何が違うのか
- Reactを使う理由
- Supabaseを使う理由

を取り扱いました。

### Happy Web Developer life ！！！

<br>

ぜひTwitterフォローして下さい！！

https://x.com/yuma_satake22
