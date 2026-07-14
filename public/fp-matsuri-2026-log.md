---
title: 【関数型まつり2026】参加レポート
tags:
  - カンファレンス
  - 関数型プログラミング
private: false
updated_at: '2026-07-14T21:08:08+09:00'
id: 6eef10954c039cd48b9e
organization_url_name: null
slide: false
ignorePublish: false
posting_campaign_uuid: null
agreed_posting_campaign_term: false
---

:::note
[これは何]
関数型まつり2026への参加レポート
:::

## 自己紹介

### Yuma Satake

プロフィールに「Webフロントやめます」って書いて3年が経ちました。
普段はWebエンジニアをしています。

- 名前：Yuma Satake
- 所属：DMM.com
- 職種：Webエンジニア
- 趣味：車・イベント運営
- Twitter：[@yuma_satake22](https://x.com/yuma_satake22)

<img width="200px" alt="Yuma Satakeのアイコンのサボテンでできた鳥の画像" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/aaf685a0-0af0-5e5b-92e9-a6f0275812fc.jpeg"/>

## 関数型まつり2026に参加しました

「関数型まつり2026」に参加してきました。

https://2026.fp-matsuri.org/

普段の業務でHaskellやF#などを使っているわけではなく、TSをメインで書いています。
そうした中で、関数型の考え方からよりよい設計ができるエッセンスが持ち帰れないかと思い、参加してきました。

<img width="400px" alt="関数型まつり2026オープニングスライド" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/9122c083-fb8c-4c38-b1fc-d009be6a4bf8.jpeg"/>

## 感想

全く悪い意味ではないという前置きの上でですが、本当に今まで参加をしたカンファレンスと全く異なるカンファレンスでした。

[池田さん](https://x.com/ike_keichan)とも喋ってた内容ですが、良い意味で「技術を目的にしている」方が多いなと思いました。
他のカンファレンスだとおおよそ50%ぐらいのトークはライブラリや設計の採用事例みたいな割合の中、関数型まつりでは8割以上が考え方や理論の話が中心でした。

かなりのセッションで数学の概念が持ち出されていましたが、私は高校をサボってかつ専門学校に進んだので、マジで一生Claudeとセッションを聞いてました（）

## 視聴したセッション

都合でDay2のみの参加だったので、この日聴講したセッションの感想をまとめました。

### ElixirのGenServerでアクタープログラミングしてみよう 〜Pub/Sub使って広域分散環境でマイグレーションも出来るよ〜

https://fortee.jp/2026fp-matsuri/proposal/904cc5d9-b328-450e-8f60-5c3bf4200b51

初っ端の自己紹介から、高知工科大学の教授をされてみえたり、通信事業会社を経営されてたり属性もりもりでびびりました。

多くの登壇者の皆さんの関数型愛の始まりって何だろうと思ってましたが「もともと並行プログラミングをやろうとしてPythonに手を出したものの気持ちよく書けず、最終的にElixirに辿り着いた」というお話が導入であり「そうやって辿り着くのか...」と思いました。

Elixirの「Let it Crash」という、例外をthrowするのではなくプロセスを一旦落として作り直すという思想は面白いなと思いました。

並行プログラミングについて、IoT機器ごとに別プロセスを立てて抽象化できたり、Pub/Subのような仕組みをプログラム内で完結して実現できるという話もなるほどなぁと思いながら聞いていました。
普段、こういった仕組みはクラウドインフラ側で組む前提で考えてしまっていたので、そもそも言語レベルでこれをやるという発想自体が新鮮でした。

セッション最後のプロセスマイグレーション（動いているプロセスを別のサーバに移動させる）の実演がとても盛り上がってました笑

<img width="400px" alt="GenServerセッションIoTデモ機材" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/57b154ce-303b-4ca0-980d-5cdec1239b11.jpeg"/>

### 代数的エフェクトの高速化技法と発展的な機能

https://fortee.jp/2026fp-matsuri/proposal/6d74ce7f-c22b-444d-840f-edd5a88c0631

代数的エフェクトは、使用しているエフェクト（ファイルシステムなど）と発生しえる例外を列挙して型として扱えるようにするもの、という理解で聞いていました。

最初は「これResult型の話に近い？」と思って混乱していましたが、「代数的エフェクトをインターフェースで表現しようとすると、実装で使うエフェクトにインターフェースが依存してしまう（インターフェースが具体に依存してしまう）」という話が出てきたところで、ようやくそういう嬉しさがあるのかという話についていけました。

後半の「非スコープ再開」あたりからは正直理解が追いつかず「良さそう！むずいね！！」と笑顔で聞いてました（諦め）

<img width="400px" alt="代数的エフェクトセッションハンドラの型スライド" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/7f7f91fd-67d0-41d6-987a-11a565e507a9.jpeg"/>

<img width="400px" alt="代数的エフェクトセッションProviderエフェクトスライド" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/900b3f64-2223-4fe2-9e98-6ff423d39892.jpeg"/>

### 美しいコードを書くためにF#を学んでみた話

https://fortee.jp/2026fp-matsuri/proposal/09478e6b-049e-409d-a315-0d310a687871

「設計が美しいコード」とは何なのかを追い求めたときに、それは関数型言語のドメインモデリングにあるよね、という話でした。
自分も同じモチベーションで関数型まつりに参加をしていたので、やっぱり関数型ドメインモデリング読んでみなきゃなと思いました。

<img width="400px" alt="F#セッション登壇風景" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/826130f2-0e2d-4b20-b1f3-edccaea82b07.jpeg"/>

### なぜ多くの言語はHigher Kinded Typesをサポートしないのか

https://fortee.jp/2026fp-matsuri/proposal/a7a9001c-b880-49ac-b2c5-1a9fedbccc12

そもそもHigher Kinded Types（HKT）を初めて知りました（）

話の中では、HKTは素晴らしい機能な一方、サポートするとコンパイル時の計算コストの肥大化/ランタイム上のパフォーマンス低下が発生する可能性があること。
そして多くの言語はシンプルさやメモリ安全性を優先していること、が理由として挙げられていました。

Haskellのようにサポートしている言語も、完全な形ではなく不完全な状態で提供している、という話を聞いて面白いなと思いながら聞いていました。

<img width="400px" alt="HKTセッション登壇風景" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/7b352e90-5296-4be3-9a12-e33d2340e60f.jpeg"/>

### Welcome to the "Parametricity" 🏙 − Generic だけど Specific な世界 −

https://fortee.jp/2026fp-matsuri/proposal/310a9a71-f65b-4ad1-a6d6-81878923cfb3

対象聴講者に「集合論の初歩的な記法を理解できる方」とあったので、流石になんとかなるだろと思って聞きに行きましたが、正直全然頭に入ってきませんでした（）
途中から数式ベースで話が進んでいき、正直リアルタイムでは全然理解できなかったので、資料が公開されたらAIに解説してもらおうと思います（）

<img width="400px" alt="Parametricityセッション関数関係図式スライド" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/77ecf5ec-2ce1-4533-ad87-044bddd9a8dc.jpeg"/>

### 壊れたパーサからはじめる関数型設計と構成的なパーサ

https://fortee.jp/2026fp-matsuri/proposal/8e81ee8e-df0e-4fa5-9cbc-f4fb797b81cb

LRパーサーの話から入り、壊れたパーサを直しながら関数型設計の考え方に踏み込んでいくセッションでした。

「関数型はhow to do ではなく what to do（どうするか、ではなく何をするか）」という言葉が確かになと思いながら聞いていました。

パーサーを勉強することは、関数型の設計思想を学ぶことにとても相性が良い、という締めも納得感がありました。

<img width="400px" alt="パーサセッション登壇風景" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/890032f5-b18a-4e52-aae3-166ff0ee1814.jpeg"/>

<img width="400px" alt="パーサセッションWhatToDoスライド" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/784e8c29-89a7-4583-b577-f08ef9a8278f.jpeg"/>

### パッケージマネージャー Nix はなぜ純粋関数型言語で設定を記述するのか

https://fortee.jp/2026fp-matsuri/proposal/22ce2709-f9c9-493a-8596-808b05620659

「関数型パッケージマネージャー」とかいう用語がまず面白かったんですが、出てくる話がマジでめちゃくちゃ関数型の利点を活かしてて面白かったです。（マジでスライド読んでほしい）

Nixは、同じ依存を持っていてもそれぞれを別で管理する仕組みになっていて、ビルドの段階で使うツールを全て事前に定義するという話が印象的でした。「何を使って、どう処理するか」を宣言的に定義するというアプローチは、まさに関数型だなぁと考えていました。

<img width="400px" alt="NixセッションzlibDerivationスライド" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/d151dcdd-3d0d-404d-a6e2-e0fca1d18546.jpeg"/>

<img width="400px" alt="Nixセッション参照透過性スライド" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/40ed1baf-48e9-40a8-89b2-669a8dec5780.jpeg"/>

### 暗号実装における辛さを関数型によって解決してみよう

https://fortee.jp/2026fp-matsuri/proposal/bcfb568b-11bc-43f4-91b0-7218c347df93

「そもそも脆弱になっているのは、脆弱に使えてしまうAPI設計が悪い」という主張から入り、暗号処理を型で堅牢化していく話でした。

現在の値がバリデーション済みか、認証済みか、といった状態に合わせて型そのものを変えていき、代数的データ型で処理する。「状態のチェックを増やすのではなく、そもそも呼び出しの可能性自体を型で拒否する」という考え方は、暗号領域に限らず全ての実装で適用できる内容だなと感じました。

<img width="400px" alt="暗号実装セッション登壇風景" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/37822f74-5e17-4fe3-bdaa-a2522b0f2828.jpeg"/>

<img width="400px" alt="暗号実装セッション3事例比較スライド" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/863130bb-ea54-49b6-beec-54317ef9e985.jpeg"/>

## その他

会場が中野セントラルパーク カンファレンスで、TSKaigi 2024ぶりだなと思って懐かしい気持ちでした。

<img width="400px" alt="関数型まつり2026会場入口サイネージ" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/7440f062-7535-429b-86bd-bc5616754348.jpeg"/>

会場では、スポンサーの[WonderSoftさん](https://coffee.wonder-soft.com/) さんによるコーヒーが提供されており、めちゃくちゃ美味しかったです。（なぜか併せて提供されていたメロンソーダの写真しか撮ってなかった）

ブースにお伺いした時にエンジニアの方がみえなかったので、コーヒーの会社じゃなくてー...という説明を受けました（）

<img width="400px" alt="会場のWSCOFFEEドリンク" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/57c755b5-a9c7-4281-9fc4-11795340ecae.jpeg"/>

## 最後に

Day2のみの参加でしたが、全然知らない世界が広がっていてほんとに面白かったです！！
開催してくださった運営の皆さん、素敵な発表をしてくださった登壇者の皆さん、スポンサーの皆さん、ありがとうございました！！！

## 資料

https://2026.fp-matsuri.org/

https://fortee.jp/2026fp-matsuri/
