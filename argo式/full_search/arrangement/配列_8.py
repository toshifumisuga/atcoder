import random
"""
N は 1 以上 100 以下の整数
"""
# num = random.randint(1, 100)
num = int(input())
# print(f"numは{num}です")

"""
Ai は -100 以上 100 以下の整数 (0≤i≤N−1)
"""
# arrangement = [random.randint(-100, 100) for p in range(0, num)]
arrangement = list(map(int, input().split()))
# print(arrangement)

"""
arrangementの内部で、最も小さい値を返す
例：
N=5
arrangement= [31, 41, 59, 26, 53]
上記の場合は、26を返す
"""

print(min(arrangement))
