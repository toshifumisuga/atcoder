# データを受け取る
num, value = map(int, input().split())
arrangement = list(map(int, input().split())) 

# 線形探索
pos = -1
for i in range(num):
    if arrangement[i] == value:
        pos = i

# 答えを出力する
print(pos)