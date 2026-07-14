#!/usr/bin/env python3
"""
Qiitaエディタが自動生成した `![ファイル名](url)` 形式の行を受け取り、
記事内の `<!-- 画像アップロード待ち: ファイル名 -->` プレースホルダーを
実際の画像Markdownに置き換える。

使い方:
    python3 apply_image_urls.py <記事ファイルパス> <URL一覧を書いたファイルパス>

URL一覧ファイルの中身の例:
    ![GenServerアクター移行スライド.jpg](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/xxxx.jpeg)
    ![Nixパッケージマネージャースライド.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2740071/yyyy.png)

一致したプレースホルダーは `![ファイル名(拡張子なし)](url)` に置換される。
一致しなかった行・使われなかったプレースホルダーは標準出力に警告として出す。
"""
import re
import sys
from pathlib import Path

MARKDOWN_IMAGE_LINE = re.compile(r"!\[(?P<name>[^\]]+)\]\((?P<url>https?://\S+)\)")
PLACEHOLDER = re.compile(r"<!--\s*画像アップロード待ち:\s*(?P<name>[^-]+?)\s*-->")


def stem(filename: str) -> str:
    return Path(filename.strip()).stem


def main() -> int:
    if len(sys.argv) != 3:
        print("使い方: python3 apply_image_urls.py <記事ファイルパス> <URL一覧ファイルパス>")
        return 1

    article_path = Path(sys.argv[1])
    urls_path = Path(sys.argv[2])

    article_text = article_path.read_text(encoding="utf-8")
    urls_text = urls_path.read_text(encoding="utf-8")

    pairs = [(m.group("name"), m.group("url")) for m in MARKDOWN_IMAGE_LINE.finditer(urls_text)]
    if not pairs:
        print("URL一覧ファイルから ![ファイル名](url) 形式の行を検出できませんでした。")
        return 1

    placeholders = {m.group("name").strip(): m.group(0) for m in PLACEHOLDER.finditer(article_text)}

    matched = []
    unmatched_pairs = []

    for name, url in pairs:
        # 完全一致優先、なければ拡張子なしで一致を試みる
        placeholder_full = placeholders.get(name.strip())
        target_key = None
        if placeholder_full is not None:
            target_key = name.strip()
        else:
            for key in placeholders:
                if stem(key) == stem(name):
                    target_key = key
                    break

        if target_key is None:
            unmatched_pairs.append((name, url))
            continue

        replacement = f"![{stem(name)}]({url})"
        article_text = article_text.replace(placeholders[target_key], replacement, 1)
        matched.append((target_key, name, url))
        del placeholders[target_key]

    article_path.write_text(article_text, encoding="utf-8")

    print(f"置換完了: {len(matched)}件")
    for target_key, name, url in matched:
        print(f"  - プレースホルダー「{target_key}」 -> {name} ({url})")

    if unmatched_pairs:
        print(f"\n警告: 対応するプレースホルダーが見つからなかったURL: {len(unmatched_pairs)}件")
        for name, url in unmatched_pairs:
            print(f"  - {name} ({url})")

    if placeholders:
        print(f"\n警告: URLが提供されなかった未使用のプレースホルダー: {len(placeholders)}件")
        for key in placeholders:
            print(f"  - {key}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
