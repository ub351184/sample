type就活説明会のための事前課題
 
## 簡単な説明
- 解答必須問題
    1. FizzBuzz問題
    2. 探索アルゴリズムの実装
- チャレンジ問題
    3.ソートアルゴリズムの実装

使用言語 : python
 
## 課題1
 
FizzBuzz問題 ([課題1のコード](https://github.com/ub351184/sample/blob/main/FizzBuzz.py))

- 1から100までの数字を出力してください
- 3の倍数のときは数字の代わりにFizzと出力してください
- 5の倍数のときは数字の代わりにBuzzと出力してください
- 15の倍数のときは数字の代わりにFizzBuzzと出力してください
 
## 課題2

探索アルゴリズムの実装 ([課題2のコード](https://github.com/ub351184/sample/blob/main/Search.py))

- 探索対象の配列から、探索する数値のindexを返却するメソッドを実装してください
- 探索対象の配列は「1つ以上の要素を持つ、昇順にソートされた重複のない整数の配列」です
- ただし、以下の条件を満たすアルゴリズムを用いて実装してください
    - 「配列の中間の値」と「探索対象の数値」の大小を比較し、中間から前後のどちらかに探索範囲を絞りながら探索を繰り返してください
    一探索毎に探索範囲が半分になるので、データ個数がnの時の計算量がO(log2n)となります
    - 探索対象の配列に探索する数値が存在しない場合は、-1 を出力してください
    - 再帰を使用せず記述してください
 
## 課題3
 
ソートアルゴリズムの実装 ([課題3のコード](https://github.com/ub351184/sample/blob/main/Sort.py))

- 整数の配列を昇順にソートするアルゴリズムを実装してください
- ソート対象の配列は「1つ以上の要素を持つ、ランダムに並べられた重複のない整数の配列」です
- ただし、以下の条件を満たすアルゴリズムを用いて実装してください
    - 配列の先頭を基準値とします
    - 先頭から末端に向かって、基準値以上の値の探索、逆方向から基準値の値未満の探索をし、見つかったらそれらの値同士を交換します
    - 先頭からの探索と、末端からの探索がぶつかった時点で探索を終了し、データを二つ（基準値以上のグループ、基準値未満のグループ）に分けます
    - 分けられたそれぞれのグループで、同様の処理を再帰的に繰り返し、交換する部分がなくなるまで処理を続けます
