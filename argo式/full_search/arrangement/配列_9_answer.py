# データを受け取る
N = int(input())
A = list(map(int, input().split())) 

print(A)
# 線形探索
count = [0] * 9 
for x in A: 
    count[x-1] += 1 

# 答えを出力する
for x in count:
    print(x)