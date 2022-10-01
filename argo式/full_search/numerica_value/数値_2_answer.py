# データを受け取る
N = int(input())

# 線形探索 (1 から N まで)
ans = 0
for i in range(1, N + 1):
    if N % i == 0: 
        ans += 1

# 答えを出力する
print(ans)