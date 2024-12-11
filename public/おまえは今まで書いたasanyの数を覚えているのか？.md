---
title: 【TS初学者向け】おまえは今まで書いた as ◯◯ の数を覚えているのか？
tags:
  - TypeScript
-  - 初学者向け
  - アドベントカレンダー2024
  - 型システム
private: true
updated_at: '2024-12-11T16:55:14+09:00'
id: d56ecd79f2cbf26c0222
organization_url_name: null
slide: false
ignorePublish: false
---

:::note
[これは何]
TypeScriptを使う上で、as ◯◯ を少しだけ使わなくてもよくなるTips集
:::

:::note
[対象者]
 TS で今まで書いた as ◯◯ の数を覚えていない人（TypeScriptを書き始めた初学者向け）
:::

## 自己紹介

### Yuma Satake

普段は ~~フロントエンド~~ Webアプリケーション開発をしている車好きの学生。
イベント運営が好き過ぎて、１回もカンファレンスに参加者として参加したことがないのに、TSKaigi の運営に去年から飛び込みました。

- 名前：佐竹友真
- 所属：名古屋工学院専門学校(3年)
- 領域：Web 開発
- 趣味：車・旅行
- Twitter：[Yuma Satake | Matsuriba🏮](https://x.com/yuma_satake22)

 <img width="200px" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/aaf685a0-0af0-5e5b-92e9-a6f0275812fc.jpeg">

## 改めて as ◯◯ とは

`as ◯◯`とは、TypeScript において型をキャストするための記述です。

- 値が特定の型だと分かっているが、上手く型が推論されない時
- 型が合わない場合に、型チェックをねじ伏せる時
- ライブラリの帰り値がanyで、その型を明示する時

など、様々なケースで`as ◯◯`という記述をすることがあるかと思います。

▼ 型アサーションについて（サバイバルTypeScript）

https://typescriptbook.jp/reference/values-types-variables/type-assertion-as

### 使用例

以下の例では、`unknown`型として宣言をした変数`num`を`as`を使ってそれぞれの型にキャストしています。

```ts
// unknown 型の変数として宣言 
const num: unknown = 1.1;

// num が number 型であることを示す 
const num2 = num as number;
num2.toFixed(); // 成功

// num が string 型であることを示す 
const num3 = num as string;
num3.toFixed(); // エラー：Property 'toFixed' does not exist on type 'string'
```

### 型アサーションの問題

型アサーションは足りない型推論を補うのに大変便利ですが、一方でTypeScriptの型推論を意図的に破壊しているため、思わぬバグを生む要因になってしまいます。


## お前は今まで書いた as ◯◯ の数を覚えているのか？

型アサーションがバグを生む要因になってしまうことは先述のとおりですが、何も全ての`as ◯◯`が無理やり型チェックをねじ伏せるために使われているわけではないと思います。

例えば、以下のような場合に`as`を使用しているケースがあるかもしれません。

### 例：nullをフィルターして、numberの配列にするケース

#### asを使った場合

```ts
const numbers: (number | null)[] = [1, 2, null, 4, null, 5];

// as を使って明示的にnumberの配列にする 
const filteredNumbers = numbers.filter((num) => num !== null) as number[];
```

ですが、実はこのようなケースは、`is`演算子を用いることで、`as`を使わずに書くことができます。

#### is演算子を使った場合

```ts
const numbers: (number | null)[] = [1, 2, null, 4, null, 5];

// is を使って明示的にnumberの配列にする 
const filteredNumbers = numbers.filter((num): num is number => num !== null);
```

この記事では、このような`as ◯◯`少しだけ使わなくてもよくなる方法を紹介します。

:::note
TypeScript5.5 よりこの記述をしなくても、勝手にnullを除外してくれるようになりました。
:::

## Tipsを見る前に

TypeScriptにはコンパイルオプションとして、型推論を厳格にする`strict`モードや、それによって自動で有効になる`noImplicitAny` `strictNullChecks`などがあります。

基本的にデフォルトで有効になっているため、あまり意識することはないかもしれませんが、これらのオプションを有効にすることで、より型安全なコードを書くことができます。

▼ StrictModeについて（サバイバルTypeScript）

https://typescriptbook.jp/reference/tsconfig/strict

### StrictMode
以下のようなコンパイルオプションを一括で有効にし、型の安全性を高めるコンパイルオプションです。

- noImplicitAny：暗黙的なany型を許可しない
- strictNullChecks：nullとundefinedの型チェックを厳密に行う
- strictFunctionTypes：関数の引数と戻り値の型チェックを厳密に行う

など

`tsconfig.json`に以下のように記述することで有効になります。

```tsconfig.json
{
  "compilerOptions": {
    "strict": true,
  }
}
```

これにより、曖昧な型が推論される状況が減り、そもそも無駄に型ガードなどを書く機会が減ります。

## Tips集

以下に、９つのTips（基本的と思われる文法も含む）を紹介します。

### 型アノテーション（関数）

本来、変数定義や、関数の帰り値における`: string`のような記述（型アノテーション）は必須ではなく、TypeScriptが推論を行い、型を自動で割り当ててくれます。

しかし、関数のパラメータや返り値、変数宣言時に明示的な型アノテーションを行うことで、TypeScriptが推論に迷わず、as を使わない適切な記述を行えます。

```ts
type CatFood = ['fish', 'milk'];
type DogFood = ['bones'];
type AnimalFood = CatFood | DogFood;

// 型アノテーション無し
function createAnimal(isDog: boolean) {
  if (isDog) {
    return ['bones'];
  }
  return ['fish', 'milk'];
}

const rover: AnimalFood = createAnimal(true); // Error：string[] として推論されてしまい代入できない

// 型アノテーション有り
function createAnimalWithAnnotation(isDog: boolean): AnimalFood {
  if (isDog) {
    return ['bones'];
  }
  return ['fish', 'milk'];
}

const whiskers: AnimalFood = createAnimalWithAnnotation(false); // OK：AnimalFood として推論される
```

### 型アノテーション（テンプレートリテラル）

テンプレートリテラル型に対しても、型アノテーションを使うことで、as を使わずに型安全な文字列リテラルを生成できます。

```ts
type PixelSize = `${number}px`;

const getPixelSize = (size: number) => `${size}px`;
const height: PixelSize = getPixelSize(10); // エラー：string として推論されてしまう

const getPixelSizeWithAnnotation = (size: number): PixelSize => `${size}px`;
const width: PixelSize = getPixelSizeWithAnnotation(10); // OK
```

### ユニオン型と型ガード

ユニオン型とは`string | number`のように複数の型を組み合わせた型のことです。

ユニオン型を扱う際には、`in` 演算子や `typeof` `instanceof`、ユーザー定義型ガード関数を使用して型を特定することができます。
これにより、as を使わずともコンパイラが条件分岐内で変数の型を絞り込むことができます。

```ts
type Animal = { type: 'cat'; meow: () => void } | { type: 'dog'; bark: () => void };

function handleAnimal(animal: Animal) {
  if ('meow' in animal) {
    // ここで animal は meow を含む cat 型として推論される 
    animal.meow();
    return;
  }
  // ここでは dog 型として推論される 
  animal.bark();
}
```

型ガードにより、animal の型が条件分岐内で確実に絞り込まれるため、as を使わずにメソッド呼び出しが可能です。

### ユーザー定義型ガード関数

本来、TypeScriptの型の絞り込みは関数のスコープ内に閉じてしまいますが、`is`を使ったユーザー定義型ガード関数を使うことで、関数外に型情報を持ち出すことができます。

以下のコードでは、`isCat`型ガードにより、関数内で animal が Cat 型であることを明示的に示しています。

```ts
type Cat = { type: 'cat'; meow: () => void };
type Dog = { type: 'dog'; bark: () => void };
type Animal = Cat | Dog;

function isCat(animal: Animal): animal is Cat {
  return animal.type === 'cat';
}

function makeSound(animal: Animal) {
  if (isCat(animal)) {
    // isCat により、このブロック内では animal は Cat と推論される 
    animal.meow();
    return
  } 
  // ここでは animal は Dog と推論 
  animal.bark();  
}
```

ユーザー定義型ガードを活用することで、複雑なユニオン型の判別でも as を使わずに安全な型判定が可能になります。

### as const

as const は型アサーションの一つですが、値をリテラル型に変換することができる、特別な型アサーションです。

定数の値やオブジェクトに as const を使用することで、後の推論においてリテラル型として扱われ、多くの場合でより上手く推論が行われるようになります。

```ts
const directions = ['north', 'east', 'south', 'west']; // string[] と推論される
const strictDirections = ['north', 'east', 'south', 'west'] as const; // readonly ["north", "east", "south", "west"] と推論される

function move(direction: 'north' | 'east' | 'south' | 'west') {
  console.log(`You move to the ${direction}.`);
}

move(directions[0]); // エラー：Argument of type 'string' is not assignable to parameter of type '"north" | "east" | "south" | "west"'.
move(strictDirections[0]); // OK
```

### オーバーロード

関数が引数によって返り値が異なる型を返す場合、関数シグネチャのオーバーロードを使うことで、呼び出し時点で適切な型を推論させられます。これにより、呼び出し側で as を使う必要がなくなります。

```ts
function fetchData(id: number): string;
function fetchData(ids: number[]): string[];

function fetchData(param: number | number[]): string | string[] {
  if (Array.isArray(param)) {
    return param.map((id) => `data_${id}`);
  } else {
    return `data_${param}`;
  }
}

// 呼び出し側
const singleData = fetchData(42);    // string と推論
const multipleData = fetchData([1,2,3]); // string[] と推論
```

オーバーロードを行うことで、返り値に対する as string や as string[] といったアサーションが不要になります。

### ジェネリクス

ジェネリクスを活用することで、型推論が自然に働き、呼び出し時点で最適な型を確定できます。

```ts
function identity<T>(value: T): T {
  return value;
}

const strValue = identity("hello"); // T は自動的に string と推論
const numValue = identity(42);      // T は number と推論
```

このようにジェネリックスを使えば、戻り値に as を付けずとも適切な型が割り当てられます。

### テンプレートリテラル・ジェネリック

ジェネリック型パラメータを活用した関数を導入することで、テンプレートリテラルでもasを回避できます。

```ts
type AnimalType = 'cat' | 'dog' | 'bird';
type EnvironmentType = 'forest' | 'desert' | 'ocean';

function makeAnimalEnvironmentKey<A extends AnimalType, E extends EnvironmentType>(
  animal: A,
  environment: E
): `${A}_${E}` {
  return `${animal}_${environment}`;
}

// 生成されたkeyは string にならず、"cat_forest" という文字列リテラル型になる
const key = makeAnimalEnvironmentKey('cat', 'forest');
```

文字列結合は型推論が上手くいかないがちですが、このようにジェネリック型パラメータを使うことで、as を使わずに型安全な文字列リテラルを生成できます。

## 最後に

今回の記事では、まだ学び始めの皆さんに向けて、as を使わずに型を安全に扱うためのTipsを紹介しました。

私自身本当にお気持ちでTypeScriptの深淵を覗いている側ですが、より深くTSの型の柔軟性に沈みたい方は`Type Challenges`という型パズルの問題があるので、ぜひ挑戦してみてください。

▼ Type Challenges

https://github.com/type-challenges/type-challenges

## TSKaigiについて

**2025年5月23日/24日** にTSKaigi 2025が開催されます！
TSKaigiは日本最大級のTypeScriptをテーマとした技術カンファレンスです(前回の参加者2000人以上)
TypeScriptに興味のある方は、ぜひ公式サイトやXを確認してみてください。

▼ TSKaigi 2025 ティザーサイト/公式X

https://2025.tskaigi.org/

https://x.com/tskaigi

## 資料

https://typescriptbook.jp

https://www.typescriptlang.org
