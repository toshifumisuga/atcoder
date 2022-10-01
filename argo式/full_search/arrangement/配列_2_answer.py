# データを受け取る
N, V = map(int, input().split())
A = list(map(int, input().split())) 

# 線形探索
count = 0
for x in A: 
    if x == V: 
        count += 1

# 答えを出力する
print(count) 