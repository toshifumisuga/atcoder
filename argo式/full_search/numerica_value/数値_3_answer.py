# データを受け取る
N = int(input())

# N = 1 の場合
if N == 1: 
    print("No")
else:
    # 線形探索 (2 から N-1 まで) 
    is_prime = True 
    for i in range(2, N):
        if N % i == 0: 
            is_prime = False 

    # 答えを出力する
    print("Yes" if is_prime else "No")