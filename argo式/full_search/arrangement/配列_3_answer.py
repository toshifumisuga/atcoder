# データを受け取る
N = int(input())
A = list(map(int, input().split()))

# 線形探索
count = 0
for x in A:
    if x > 0:
        count += 1

# 答えを出力する
print(count)