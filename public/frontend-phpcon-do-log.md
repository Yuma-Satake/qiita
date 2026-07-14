---
title: 【フロペチ北海道2026】参加レポート
tags:
  - カンファレンス
private: false
updated_at: '2026-06-14T22:08:34+09:00'
id: 030f2b973ec321abe07a
organization_url_name: null
slide: false
ignorePublish: false
posting_campaign_uuid: null
agreed_posting_campaign_term: false
---

:::note
[これは何]
フロントエンド・PHPカンファレンス北海道 2026への参加レポート<br />（これ以上遅くなると公開しないと思ったので内容はペラペラです）
:::

:::note
[対象読者]
フロペチ北海道の様子を知りたい人
:::

## 自己紹介

### Yuma Satake

プロフィールに「Webフロントやめます」って書いて3年が経ちました
普段はWebフロントエンドエンジニアをしています

- 名前：佐竹友真
- 所属：DMM.com
- 職種：Webフロントエンドエンジニア
- 趣味：車・イベント運営
- Twitter：[@yuma_satake22](https://x.com/yuma_satake22)

<img width="200px" alt="Yuma Satakeのアイコンのサボテンでできた鳥の画像" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/aaf685a0-0af0-5e5b-92e9-a6f0275812fc.jpeg"/>

## フロペチ北海道2026に参加しました

2026年6月6日（土）に札幌コンベンションセンターで開催された「フロントエンド・PHPカンファレンス北海道2026」に参加してきました。（気づいたら1週間経っててビビる定期）

https://frontend-php-con.hokkaido.jp/

今までペチコンにもフロカンにも参加をしたことはありましたが、双方全然雰囲気が違うよなぁと思っていたので、合同開催だとどんな雰囲気になるのか楽しみにして行きました。
4月から社会人になったので、会社がカンファレンス参加費用をサポートしてくれるようになったのがありがたいところでした。

## 会場・オープニング

会場の札幌コンベンションセンターはかなり札幌の中心から近く、アクセスが良かったです。

<img width="400px" alt="曇り空の下、広場に面した札幌コンベンションセンターのガラス張り外観" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/37d92fc2-7d2f-4300-b30c-a1e265cba5a8.jpeg"/>

最初はことみんの開催挨拶から始まりました。一緒に行ったカンファレンス初の友人が「カンファレンスって結構緩い感じなん？」って言い出して、アットホームさは敷居を下げるのに大事だなと思いました。

<img width="400px" alt="FE×PHP CONFERENCE HOKKAIDO 2026の開幕セレモニーでピンク髪の司会者がマイクを持ちスクリーンに開幕と表示されている" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/6ff1a71d-d8f3-4dde-b6aa-5050a1201b66.jpeg"/>

## 視聴したセッション

### 103 Early Hintsで始める、サーバー・フロントの協調最適化

https://fortee.jp/frontend-phpcon-do-2026/proposal/24a72c4c-49d3-4a02-a8c0-769eeab48e7e

103のステータスコード自体は認知していたものの、全く実用の経験がなかったため、面白いセッションでした。

そもそも現在の103に至っている歴史の話から、SPAに対しては初期HTMLが薄いためサーバー側の待ち時間がほとんどなく、103 Early Hintsの効果が薄いという話などを頷きながら聞いていました。

個人的には、Next.jsなどの最適化された分厚いフレームワークにおいては内部的に利用されて、開発者が個別に意識せずとも裏側で恩恵に預かる形になるのかなと思いました。

### 代数的データ型って何が嬉しいの？

https://fortee.jp/frontend-phpcon-do-2026/proposal/f85e1c42-0592-4f5f-a493-e0757412e0a5

<img width="400px" alt="フロントエンド・PHPカンファレンスで積ANDと和ORのTypeScript型の表現を解説するセッションスライド" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/03d11969-ef28-461c-abef-42f3428f1de9.jpeg"/>

代数的データ型や、Result型の概念がとてもわかりやすく説明されているセッションで感動しました。

この辺りの考え方については、普段使っているTSでも重要な概念だとは理解していますが、中々人に説明するのが難しいなぁと思っていたので、非常に勉強になるセッションでした。

### TypeScript Compiler APIとPHP-Parserを活用し、TypeScriptとPHPで型を共有する

https://fortee.jp/frontend-phpcon-do-2026/proposal/d7c6d509-cd29-4afa-abbd-c9fa6818960a

<img width="400px" alt="JSONの型をPHPとフロントエンドで共有するために生成されたPHPDoc Typesを紹介するセッションスライド" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/ede75d00-b612-4827-a8e8-daf78c6f6d36.jpeg"/>

TSのコードからPHPDoc Typesを生成するというものでしたが、実際に生成された型を見て他言語間での型共有ってやっぱ大変だなぁって思いました。（セッション中でも言及されていた対応する型が無いという表現の問題についても同様）

もちろんそういう話では無いのは分かりつつ、ここまで型を同期させる仕組みを作り込むコストを考えると、別アプリケーションとしてOpenAPIのSchemaぐらいで型を共有した方がシンプルだよなぁと思いました。

このセッション自体は、フロントエンドとPHPの合同カンファレンスだからこそ生まれたセッションだと思ったので、面白いセッションでした。

### 「おすすめ」 はなぜ信用されないのか 〜 信頼を築くUI／UX設計 〜

https://fortee.jp/frontend-phpcon-do-2026/proposal/6cd24c56-8f89-4df0-a4f6-83f8be3ec255

レコメンドシステムにおいてユーザーに押し付け感や不気味さを与えないためにはどうすれば良いか？というセッションでした

ユーザーに納得感を持って機能を受け入れてもらうためには、「学習元をユーザー自身で制御できること」や「推薦理由を明示すること」が重要であり、バックエンドの複雑なロジックをいかにフロントエンドがユーザー視点の体験へと翻訳して提示できるかが、プロダクトの信頼に繋がるという話で、なるほどなぁと思いながら聞いていました。

技術的に優れたレコメンドエンジンと、ユーザーがそれを信頼して使ってくれることは別問題であるというのは、大事な視点だなと思いました。

### Sync と Async ─ useSyncExternalStore を使う者の岐路

https://fortee.jp/frontend-phpcon-do-2026/proposal/8be40e84-6fca-4660-b6dd-b25a31d59a45

Async Reactのパラダイムと、Zustandのような同期的状態管理ライブラリが抱えるアーキテクチャ上の問題について、実例ベースで理解できたセッションでした。

Zustandが内部で`useSyncExternalStore`に依存しているがゆえの制約があり、回避策として`use-zustand`を利用するアプローチなどを知ることができました。

### AI時代のUIはどこへ行く？その2！

https://fortee.jp/frontend-phpcon-do-2026/proposal/3435cc2a-90b6-4f28-8394-1d0665001020

<img width="400px" alt="登壇者がLLMによるUI生成のControlled・Declarative・Open-Endedの3パターン比較表をスクリーンで解説しているセッション" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/b6eb778d-646d-4e4d-b377-9be344d64447.jpeg"/>

AIが生成するUIの3パターン（Controlled / Declarative / Open-Ended）における再現性、トークン消費、レイアウト自由度などのトレードオフが綺麗に整理されており、分かりやすかったです。

また、第4の方向性として、LLMに直接Reactコードを書かせて動的にUIをレンダリングするアプローチが紹介されていました。「でもセキュリティがなぁ...」とか思っていたら Cloudflare の機能が滑らかに出てきて思わず契約しそうになりました（適当）

### LT

1日の最後には怒涛のLTレーンがありました（写真撮ってあったやつだけ）

### 実践！春の上川空知駆動開発

https://fortee.jp/frontend-phpcon-do-2026/proposal/ece8e38b-20ff-4857-9e4d-a0fe75d93af8

西原さんの詠唱がマジで良すぎて、俺ももっとLT上手くなりてぇなって思いました

<img width="400px" alt="Shota Nishiharaによる実践・春の上川空知駆動開発で旭川・東川・美瑛・富良野などを巡るドライブ旅行のセッション" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/3dd27ba5-26f5-4be8-acf2-a4f93eea2646.jpeg"/>

### 「👍」と「👎」の押しミスに震えない世界を作りませんか?

https://fortee.jp/frontend-phpcon-do-2026/proposal/1ac2af7f-e99f-48e7-a2ae-ba45d6178037

リアクションUIの並び順にあんまり違和感を感じたことなかったので、確かに文字コードで並べただけやろな...って思いました

<img width="400px" alt="FE×PHPカンファレンスHOKKAIDOでリアクションボタンのUIを変えていく提案をするセッションスライド" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/04ffdb18-2ba7-45fc-bce4-932bbec4ca68.jpeg"/>

### 作って学ぶ、 JSX (TSX) ランタイムの基本

https://fortee.jp/frontend-phpcon-do-2026/proposal/9702d654-e233-4608-bffb-0fa04cff75c1

私は今までJSXランタイムを作ったことがないのでフロントエンドエンジニアではないことが発覚しました（！？）

<img width="400px" alt="JSXがTranspilerによってh関数の呼び出しに変換される仕組みを解説するFE×PHPカンファレンスHOKKAIDOのセッションスライド" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/7b964e7f-54c3-413f-97ba-17c0d8da7f09.jpeg"/>

### PHPで使える日時の表現と、その知り方

https://fortee.jp/frontend-phpcon-do-2026/proposal/77172968-2ab4-419b-a9eb-95080beabd75

JSこそがいろんな言語の中で一番やばいDateの実装をしていると信じていましたが、そんなことはありませんでした

<img width="400px" alt="PHPのDateTimeImmutableの自然言語日付文字列とタイムゾーンオフセット計算を解説するFE×PHPカンファレンスHOKKAIDOのセッションスライド" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/9e1b1eaa-1c0c-4dd8-acb9-f12773e9e7c8.jpeg"/>

## その他

久しぶりにカンファレンスに一般参加者で楽しそうな成人男性

<img width="400px" alt="花柄シャツを着た男性がFE×PHP CONFERENCE HOKKAIDO 2026のスポンサーボードの前でポーズを取っている" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/a5c25aa6-2909-44ca-95b8-730d72c25a5b.jpeg"/>

PR TIMESさんのブースのチャレンジでいい感じのスコアを出して、ノベルティをもらいました（感謝）

<img width="400px" alt="PR TIMESブースのノベルティとして配布されたバスソルト入りの黒いポーチ" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/3578fadd-bcd3-44b5-92c2-3ef0898af15e.jpeg"/>

ランダムマッチランチという企画があり、ランダムに組まれたグループでランチに行きました（PHPの人とフロントエンドの人が半々になるように組まれていて面白かった）

<img width="400px" alt="飲食店でジンギスカン鍋を前に笑顔でVサインをする4人" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/6b2dae0e-355d-4395-9e83-43d536e0590e.jpeg"/>

会場近くのラソラ札幌に入っている「らぁめん銀波露」で味噌ラーメンを食べました。
札幌気分を出すためにコーンを入れたものの、ベースのラーメンがマジで重くて食べきれないかと思いました（）

<img width="400px" alt="コーン・チャーシュー・メンマ・ネギ・ゴマがトッピングされた味噌ラーメン" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/8ae48a34-cb86-46fa-9aef-d9cfea64266c.jpeg"/>

懇親会で[うひょさん](https://x.com/uhyo_)の隣になったはいいものの、席の関係で肉を焼いてもらうことになり、恐ろしく単価の高い焼肉を食べることになりました

https://x.com/yuma_satake22/status/2063252971920695666?s=20

ツナギメエフエムのアカセさんから登壇者キーホルダーをもらいました。初めて実体のアカセさんと会えて嬉しかった。

https://x.com/yuma_satake22/status/2063223401708429316?s=20

## 北海道旅行の様子

これは初めての機外カメラではしゃぐ子どもの図

<img width="400px" alt="JAL機内のモニターに表示された夜間に滑走路を走行する機体上部からの離陸カメラ映像" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/f294e2e2-c273-4f48-9b24-517b9ec08b12.jpeg"/>

関東がクソ暑いからといって、北海道に半袖で行くのはやめましょう、死にかけました

https://x.com/yuma_satake22/status/2062888459334025596?s=20

ことみんの聖地巡礼をすべく、苫小牧に行きました

<img width="400px" alt="苫小牧港PORT OF TOMAKOMAIの大型モニュメントの文字の上に立ってポーズを取る男性" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/00c8058d-6384-46fb-a9ed-4c23e97c378b.jpeg"/>

道民に運転をしてもらうことで、海鮮丼をサッポロクラシックで流すことができ感動しました

https://x.com/yuma_satake22/status/2063499533158641891?s=20

## 感想

初めてフロントエンドとPHPの合同カンファレンスに参加しましたが、流石に合同ならではのセッションも多く、面白いセッションが多いカンファレンスでした。（登壇手慣れた人が多くて最高だった）

会場自体も、フロントエンド人の若さと、PHP人の皆さんのアットホームさが混ざっており、過ごしやすい（？）雰囲気でした。

あと北海道最高！！来年も行くぞー！！！

運営の皆さん、運営お疲れ様でした！最高！！！
