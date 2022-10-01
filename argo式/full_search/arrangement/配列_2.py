import random
"""
N は 1 以上 100 以下の整数
"""
num = random.randint(1, 100)
# num = 44
print(f"numは{num}です")
"""
V は 1 以上 100 以下の整数
"""
value = random.randint(1, 100)
# value = 11
print(f"valueは{value}です")

"""
Ai は 1 以上 100 以下の整数 (0≤i≤N−1)
"""
# arrangement = [3, 5, 1, 9, 1]
# arrangement = [56,11,32,65,58,8,32,11,7,11,24,75,27,84,60,86,24,26,83,16,11,30,11,38,53,12,37,11,21,13,68,53,11,87,70,30,35,28,72,11,25,52,79,56]
# print(arrangement)
arrangement = [random.randint(1, 100) for p in range(0, num)]
# print(f"arrangementにvalueは{arrangement.count(value)}個 含まれます")
# print(arrangement)
# print(arrangement.count(value))

# 線形探索
count = 0
for x in arrangement:
    if x == value:
        count += 1

# 答えを出力する
print(count)


