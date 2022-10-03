"""
英小文字からなる文字列 S と、英小文字 c が与えられます。
文字列 S の中に c が含まれるかどうかを答えるプログラムを作成してください。

S は英小文字からなる長さ 100 以下の文字列
c は英小文字
"""
# 入力を受け取る
S = input()
c = input()

# S の長さを取得する
N = len(S)

# 線形探索
flag = False
for i in range(N):
    if S[i] == c:
        flag = True

# 答えを出力する
if flag: print("Yes")
else: print("No")