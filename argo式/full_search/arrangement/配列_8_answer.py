# データを受け取る
N = int(input()) 
A = list(map(int, input().split())) 

# 線形探索
minnum = A[0] 
for x in A:  
    if x < minnum:  
        minnum = x 

# 答えを出力する
print(minnum) 