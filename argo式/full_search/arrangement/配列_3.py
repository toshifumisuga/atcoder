import random
"""
N は 1 以上 100 以下の整数
"""
num = random.randint(1, 100)
print(f"numは{num}です")

"""
Ai は -100 以上 100 以下の整数 (0≤i≤N−1)
"""
arrangement = [random.randint(-100, 100) for p in range(0, num)]

# 線形探索
count = 0
for x in arrangement:
    if x > 0 :
        count += 1

# 答えを出力する
print(count)