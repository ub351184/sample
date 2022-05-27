def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述

    # 基準値以上の値のindex用変数
    idx_more = 0
    # 基準値未満の値のindex用変数
    idx_less = -1
    # 配列の長さ
    l = len(array)

    for i in range(l):
        # 配列の先頭から探索
        for j in range(l):
            # 基準値以上の値とindexを記録
            if array[j] >= pivot:
                idx_more = j
                value_more = array[j]
                break
        # 配列の末端から探索
        for k in range(l-1,-1,-1):
            # 基準値以下の値とndexを記録
            if array[k] < pivot:
                idx_less = k
                value_less = array[k]
                break
        # 先頭からの探索と末端からの探索がぶつかっていないとき -> ぶつかるまで繰り返し
        if idx_more < idx_less:
            # 値を交換
            array[idx_more] = value_less
            array[idx_less] = value_more
        # 基準値未満がいないとき
        elif idx_less == -1:
            # データを2つに分ける分かれ目を記録
            idx_slice = 1
            break
        # 先頭からの探索と末端からの探索がぶつかったとき
        else:
            # データを2つに分ける分かれ目を記録
            idx_slice = idx_more
            break

    # 分かれ目より配列をグループ1,2に分解
    array_1 = array[:idx_slice]
    array_2 = array[idx_slice:]

    # 再起関数
    # グループ1,2の要素が1つのとき
    if len(array_1) == 1 and len(array_2) == 1:
        # そのまま値を返す
        return array_1 + array_2
    # グループ1の要素が複数あるとき
    elif len(array_1) > 1:
        # グループ1の配列をsortし値を返す
        return sort(array_1) + array_2
    # グループ2の要素が複数あるとき
    elif len(array_2) > 1:
        # グループ2の配列をsortし値を返す
        return array_1 + sort(array_2)
    # グループ1,2どちらも要素が複数あるとき
    else:
        # グループ1,2どちらも配列をsortし値を返す
        return sort(array_1) + sort(array_2)

    # ここまで記述

if __name__ == '__main__':
    main()