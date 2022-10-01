import random
"""
N は 1 以上 100 以下の整数
"""
num = random.randint(1, 100)

print(f"numは{num}です")
"""
V は 1 以上 100 以下の整数
"""
value = random.randint(1, 100)
print(f"valueは{value}です")

"""
Ai は 1 以上 100 以下の整数 (0≤i≤N−1)
"""
# arrangement = [3, 5, 1, 9, 2]
arrangement = [random.randint(1, 100) for p in range(0, num)]
print(f"arrangementの要素は{arrangement}です")
if value in arrangement:
    print('Yes')
else:
    print('No')


