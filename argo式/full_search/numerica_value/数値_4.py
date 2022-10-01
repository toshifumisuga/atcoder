"""
整数 A と B の最大公約数を出力するプログラムを作成してください。
ただし次の条件を満たすとき「 X は A と B の最大公約数である」と言います。
条件：X は A も B も割り切る 1 以上の整数の中で最大のものである

A,Bは 1 以上 100 以下の整数
"""
# 入力を受け取る
A, B = map(int, input().split())

# 約数を入れるためのリストを作る
A_divisor = []
B_divisor = []
# i に 1 から A までの数を順番に代入する
for i in range(1,A+1):
    # A が iで割り切れる場合、約数のリストに追加
    if  A%i==0:
        A_divisor.append(i)

# j に 1 から B までの数を順番に代入する
for j in range(1,B+1):
    # B が jで割り切れる場合、約数のリストに追加
    if  B%j==0:
        B_divisor.append(j)

# print(A_divisor)
# print(B_divisor)

conjugate_number = set(A_divisor) & set(B_divisor)
# print(conjugate_number)
print(max(conjugate_number))
