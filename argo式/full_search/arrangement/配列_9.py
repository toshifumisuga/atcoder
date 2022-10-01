import random
"""
N は 1 以上 100 以下の整数
"""
# num = random.randint(10, 15)
num = int(input())
# print(f"numは{num}です")

"""
Ai は 1 以上 9 以下の整数 (0≤i≤N−1)
"""
# arrangement = [random.randint(1, 9) for p in range(1, num)]
arrangement = list(map(int, input().split()))
# print(arrangement)

"""
i 行目には i の個数を出力
例：
N=5
arrangement= [1, 2, 1, 4, 5]
上記の場合は
2
1
0
1
1
"""

for i in range(1, 10):
    count = 0
    for x in arrangement:
        if x == i:
            count += 1
    print(count)
