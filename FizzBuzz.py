for num in range(1, 101):
    string = ''

    # ここから記述

    # 15の倍数か判定
    if num%15 == 0:
        string = 'FizzBuzz'

    # 3の倍数か判定
    elif num%3 == 0:
        string = 'Fizz'

    # 5の倍数か判定
    elif num%5 == 0:
        string = 'Buzz'

    # 3,5の倍数でない場合
    else:
        string = str(num)

    # ここまで記述

    print(string)