# データを受け取る
N, V = map(int, input().split())
A = list(map(int, input().split())) 

# 線形探索
flag = False
for x in A: 
    if x == V: 
        flag = True

# 答えを出力する
if flag:
    print("Yes")
else:
    print("No")