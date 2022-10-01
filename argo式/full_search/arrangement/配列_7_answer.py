# データを受け取る
N = int(input()) 
A = list(map(int, input().split())) 

# 線形探索
index = 0 
for i in range(N): 
    if A[i] > A[index]:  
        index = i 

# 答えを出力する
print(index) 