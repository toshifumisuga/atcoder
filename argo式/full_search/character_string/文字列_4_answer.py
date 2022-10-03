# データを受け取る
N = int(input()) 
S = input()
T = input() 

# 線形探索
count = 0 
for i in range(N):
    if S[i] != T[i]: 
        count += 1 

# 答えを出力する
print(count) 