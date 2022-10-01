"""
整数 N が素数かどうかを判定するプログラムを作成してください。

ただし次の条件を満たすとき「 N は素数である」と言います。

N は 2 以上の整数である
N を割り切ることのできる 1 より大きい整数は N のみである

N は 1 以上 100 以下の整数
"""
# 入力を受け取る
N = int(input())
# count に 0 を代入する
count = 0

# i に 2 から N までの数を順番に代入する
for i in range(2,N+1):
    # N が iで割り切れる場合に1を足す
    if  N%i==0:
        count +=1

# 素数の場合、割り切れるのが自身の値のみなので、countが1になる
if count == 1:
    print('Yes')
else:
    print('No')
