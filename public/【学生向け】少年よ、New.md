---
title: 【学生向け】少年よ、New Relicを抱け
tags:
  - "NewRelic オブザーバービリティ 初心者向け 学生"
private: false
updated_at: ""
id: null
organization_url_name: null
slide: false
ignorePublish: false
---

:::note
[これは何] 
まだオブザーバビリティに触れた事の無い学生が、New Relic を使ってみるべき理由と、その簡単な実例を紹介します。
:::

:::note warn
[注意]
この記事は、オブザーバビリティやモニタリングを初めて知る/あまり触れたことのない学生向けに書かれています。
:::

:::note 
[略語]
記事中では、`New Relic`を`NR`と略して表記します。
:::


## 自己紹介

### Yuma Satake

普段は ~~フロントおじさん~~ Webアプリケーション開発をしている車好きの学生。
9月に相方のむらさめと、NRUG Nagoya を立ち上げました。

- 名前：佐竹友真
- 所属：名古屋工学院専門学校(3 年)
- 領域：Web 開発
- 趣味：車・旅行
- Twitter：[Yuma-Satake | Matsuriba🏮](https://x.com/yuma_satake22)

 <img width="200px" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/aaf685a0-0af0-5e5b-92e9-a6f0275812fc.jpeg">

なんか一通り書いたら、めちゃくちゃAI生成みたいな文章になってしまった。


## 学生よ、New Relic を使え

`New Relic`や`Data Dog`といったツールを使ったことはありますか？
これらのツールは、アプリケーションやインフラのログやパフォーマンスを監視する、**オブザーバビリティツール**です。

### 何が嬉しいか

- **エラー時のトレース**
  エラーが発生した際に、どの処理で、どんな内容でエラーが発生したかをトレースできる
- **ユーザ体験を可視化**
  ページロードが遅い・APIエラーが多発してる などユーザーの体験を損ねてる問題を簡単に発見できる
- **パフォチューのお供**
  スロークエリや、時間がかかってる処理が可視化できる

このようにオブザーバビリティツールを使うことで、より快適に開発ができるようになります！
しかし、周囲でこれらのツールを使っている学生を私はほぼ知りません😇

### なぜ学生が触れる機会が少ないか（n=2）

- そもそも運用フェーズを踏まないので、ツールに触れる機会が少ない
- 利用料が高いイメージがある
- 導入が難しそうなので、手を出しにくい

ですが、実際に大きな企業の開発現場では、これらのツールが導入されていることが多いです。
インターン等でなら触れる機会があった...という学生も多いのではないでしょうか？

#### しかし、NRには、開発中も便利に使える機能や、学生向けの無料プランがあります！！

この記事では、そんなNRの登録方法や、Goにおける簡単な導入方法を紹介します。

## New Relic とは？

>[NR公式サイトより] 
New Relic は、モバイルやブラウザのエンドユーザーモニタリングや、外形監視、バックエンドのアプリケーションとインフラモニタリングなど、オンプレやクラウド、コンテナからサーバレスまであらゆるシステム環境での性能管理を実現するプラットフォームです

NRとは何か、を一言で説明するのはとても難しいですが、フロント→バックエンド→インフラまで、サービスの全てを可視化する事ができるツール（プラットフォーム）です。

## 学生に優しい New Relic

NRは、学生向けの無料プランや、初めてオブザーバビリティを学ぶためのコンテンツを提供しています。

- **学生向け無料プラン**：Github Education 経由で無料で利用できます
- **全ての機能が使える**：無料プランでも、全ての機能+500GB/月のデータ書き込みが可能
- **学習コンテンツ**：オブザーバビリティとは？から、実際のアプリケーションに導入する方法まで

https://newrelic.com/jp/students

## New Relic の始め方

実際に、Github Student Developer Pack 経由で NR を始める手順を紹介していきます。

### 1. アカウントの作成

まず、正面からアカウントを作成します。

▼ サインアップ

https://newrelic.com/jp/sign-up-japan

一通り入力して、仮登録

<img width="400px" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/d72773e7-fea0-2e83-9a69-e28245cf3eb2.png" />

仮登録のメールが届くので、リンクから本登録

<img width="400px" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/912d7cc3-6790-e652-11cb-d727f2750138.png" />

今回は後で Github との連携を行うので、GithubのOAuthで登録します

<img width="400px" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/141de260-7294-98b3-2b75-686a1b9bd42c.png" />

Githubとの連携画面が出るので許可

<img width="400px" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/016c3b6c-f1d8-349c-310a-999a5e1e71a9.png" />

ダッシュボードが表示されれば完了です！

<img width="400px" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/a9c17b2b-97f6-7106-9fc6-5aa45f6705ab.png" />


### 2. GitHub Education との連携

次に、GitHub Education と NR を連携し、学生アカウントとして認証します。

#### ① Github アカウントを GitHub Education で認証

まず、Github アカウントを Github Education で学生であることを証明し、GitHub Student Developer Pack の特典を利用できるようにします。

:::note warn
日本語の証明書を使った場合に必要な対応がコロコロ変わるため、完全に保証はできませんが、2024年8月に以下の記事の内容で認証が通りました。
:::

▼ Github Education の申請方法

https://qiita.com/Kobayashi2019/items/5adb9bde57691a770419

#### ② New Relic アカウントへの特典追加

[New Relic for Students](https://one.newrelic.com/nr1-core/students-edition/home?account=6216488&state=508da9d2-ca41-3319-c1cc-b5c48783a42f)もしくは
サイドバーの`Help > Resources > New Relic for Students`を開きます

<img width="400px" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/043d65a9-5224-e49a-283f-28c2feae1a79.png" />

`GitHub Education`を選択
※ DarkThemeだとGithubが闇堕ちして見づらかったのでここだけ、LightTheme

<img width="400px" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/e4b9afd7-3b78-2192-4582-d5d0b91e8850.png" />

`Student`を選択し、`Authorize with GitHub`をクリック

<img width="400px" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/0bff3b79-4dad-dda7-4414-93127b3a74ed.png" />

Githubとの連携画面が出るので許可

<img width="400px" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/05e5c228-763b-db9a-128e-c9bbf749c4f9.png" />

これで、学生アカウントとして認証が完了しました！


## Go BE アプリへの New Relic の導入

一通り準備ができたので、以下の公式のDocsを参考に、Goのバックエンドアプリケーションに NR を導入してみます。

▼ [公式]Go アプリへの New Relic の導入

https://docs.newrelic.com/jp/docs/apm/agents/go-agent/installation/install-new-relic-go/

### 環境について
筆者の環境は以下の通りです。
使用しているOSや言語バージョンに沿った対応が必要です。

- OS：MacOS Sequoia 15.1.1
- Go：1.23.1


### 1. ライセンスキーの発行

[API KEYの管理画面](https://one.newrelic.com/admin-portal/api-keys/home?account=6216488&state=f658032c-81bc-9d67-94b2-646db8c06606)でライセンスキーを発行します。

右上の`Create a Key`をクリック

それぞれ入力して Key を作成。
（今回はバックエンドアプリケーションのため、`Key type`に`Ingest - License`を選択）

▼ KEY Typeについてはこちら

https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/

### 2. 簡単なGoのプロジェクトの作成

#### ① プロジェクトの作成

※`Go`についての記載は本筋ではないため、`Cloud Run`のサンプルを利用します。

▼ クイックスタート: Cloud Run に Go サービスをデプロイする

https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-go-service?hl=ja

テンプレート通り`main.go`を作成
```go
package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
)

func main() {
	log.Print("starting server...")
	http.HandleFunc("/", handler)

	// Determine port for HTTP service.
	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
		log.Printf("defaulting to port %s", port)
	}

	// Start HTTP server.
	log.Printf("listening on port %s", port)
	if err := http.ListenAndServe(":"+port, nil); err != nil {
		log.Fatal(err)
	}
}

func handler(w http.ResponseWriter, r *http.Request) {
	name := os.Getenv("NAME")
	if name == "" {
		name = "World"
	}
	fmt.Fprintf(w, "Hello %s!\n", name)
}
```

#### ② NRの導入

envファイルを作成し、ライセンスキーを設定

```
NEW_RELIC_LICENSE_KEY=YOUR_LICENSE_KEY
```

パッケージをインストール

```zsh
go get github.com/newrelic/go-agent/v3/newrelic
```

インストールしたパッケージを`import`するために、`main.go`に以下を追記

```go
import "github.com/newrelic/go-agent/v3/newrelic"
```

`main関数`に以下を追記し、NRを初期化

```go
app, err := newrelic.NewApplication(
    newrelic.ConfigAppName("go-nr-test-app")
    newrelic.ConfigLicense(os.Getenv("NEW_RELIC_LICENSE_KEY"))
		newrelic.ConfigDistributedTracerEnabled(true),
)
if err != nil {
	log.Fatal(err)
}
```

NRでラップするため、`handler関数`を以下のように変更

```go
http.HandleFunc(newrelic.WrapHandleFunc(app, "/", handler))
```

最終的な`main.go`は以下のようになります

```go
package main

import (
	"fmt"
	"log"
	"net/http"
	"os"

	"github.com/newrelic/go-agent/v3/newrelic"
)

func main() {
	log.Print("starting server...")
  app, err := newrelic.NewApplication(
      newrelic.ConfigAppName("go-nr-test-app"),
      newrelic.ConfigLicense(os.Getenv("NEW_RELIC_LICENSE_KEY")),
  		newrelic.ConfigDistributedTracerEnabled(true),
  )
  if err != nil {
  	log.Fatal(err)
  }

  http.HandleFunc(newrelic.WrapHandleFunc(app, "/", handler))

	// Determine port for HTTP service.
	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
		log.Printf("defaulting to port %s", port)
	}

	// Start HTTP server.
	log.Printf("listening on port %s", port)
	if err := http.ListenAndServe(":"+port, nil); err != nil {
		log.Fatal(err)
	}
}

func handler(w http.ResponseWriter, r *http.Request) {
	name := os.Getenv("NAME")
	if name == "" {
		name = "World"
	}
	fmt.Fprintf(w, "Hello %s!\n", name)
}
```
