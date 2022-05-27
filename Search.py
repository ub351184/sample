def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述

    # 探索対象のindex値用変数
    index = 0
    # 探索対象となる配列
    object_array = sorted_array
    # 中間値のindex用変数
    middle_index = 2

    # 探索対象配列の要素数が1つになるまで
    while len(object_array) > 0:

        # 中間値のindexを求める
        middle_index = len(object_array)//2

        # 中間値が探索対象の番号のとき
        if object_array[middle_index] == target_number:
            index += middle_index   # indexの更新
            return index
        
        # 中間値が探索対象の番号より大きいとき
        elif object_array[middle_index] > target_number:
            object_array = object_array[:(middle_index)]   # 探索対象配列の更新
            index += 0   # indexの更新

        # 中間値が探索対象の番号より小さいとき
        elif object_array[middle_index] < target_number:
            object_array = object_array[(middle_index+1):]   # 探索対象配列の更新
            index += middle_index + 1   # indexの更新
    
    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()