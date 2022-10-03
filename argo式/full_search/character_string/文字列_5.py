"""
英小文字からなる文字列 S (長い) と T (短い) が与えられます。
文字列 S の中に、文字列 T が含まれるかどうかを判定してください。 

たとえば、次の通りです。
algomethod は go を含みます
algomethod は met を含みます
algomethod は ago を含みません (l が挟まっています)

S は英小文字からなる長さ 100 以下の文字列
T は英小文字からなる長さ 100 以下の文字列
S の長さは T の長さ以上である
"""
# 入力を受け取る
S = input()
T = input()

# S, T の長さを取得する
S_length = len(S)
T_length = len(T)

# print(S_length)
# print(T_length)

# 線形探索
flag = False
# 長い方の文字列と短い方の差分の回数+1回分ループさせる
for i in range(S_length-T_length+1):
    # 先頭から、短い方の文字数を順に抜き出して、それが短い方の文字列と一致するか検証する
    if S[i:i+T_length]==T:
        flag = True

# 答えを出力する
if flag: print("Yes")
else: print("No")