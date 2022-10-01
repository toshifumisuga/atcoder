import random
"""
N は 1 以上 100 以下の整数
"""
# N = random.randint(1, 100)
# 入力を受け取る
N = int(input())
# count に 0 を代入する
count = 0

# i に 1 から N までの数を順番に代入する
for i in range(1,N+1):
    # i が 2でも3でも5でも割り切れないときに、1を足す
    if not i%2==0:
        if not i%3==0:
            if not i%5==0:
                count += 1

# count の値を出力する
print(count)