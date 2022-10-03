"""
英小文字からなる文字列 S が与えられます。

文字列 S が回文かどうかを判定するプログラムを作成してください。 
なお文字列 S が回文であるとは、S を逆から読んでも S になることを言います。

S は英小文字からなる長さ 1 以上 100 以下の文字列
"""
# 入力を受け取る
S = input()

# S の長さを取得する
N = len(S)

# 中央の文字列の値を取得する
center_number = (N+1)//2 -1

# 線形探索
count = 0
for i in range(0,center_number):
    # そもそも文字列の文字数が偶数の場合は回文にならない
    # サンプルとして、abbaという文字列は回文と判定したいので、上記の法則は成り立たない
    # if (N+1)%2==1:
    #     count += 0
    # 回文の場合、先頭と一番最後、先頭から2番目と最後から2番目・・が一致する
    if S[i]==S[-(i+1)]:
        count += 1

# print(count)
# print(center_number)
# print(N)

# 答えを出力する
if count==center_number: print("Yes")
else: print("No")