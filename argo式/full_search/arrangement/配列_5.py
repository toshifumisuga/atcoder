import random
"""
N は 1 以上 100 以下の整数
"""
num = random.randint(1, 100)
# num = map(int, input().split())
# print(f"numは{num}です")
"""
V は 1 以上 100 以下の整数
"""
value = random.randint(1, 100)
# value = map(int, input().split())
# print(f"valueは{value}です")

"""
Ai は 1 以上 100 以下の整数 (0≤i≤N−1)
"""
arrangement = [random.randint(1, 100) for p in range(0, num)]
# arrangement = list(map(int, input().split()))
# print(arrangement)

"""
arrangementの内部で、ある要素とその隣にある値が大きい場合は条件を満たす
例：
N=5
arrangement= [31, 41, 59, 26, 53]

条件を満たす i は 1,2,4 の 3 つです。
"""

count =0
for i in range(1, len(arrangement)):
    if arrangement[i-1] < arrangement[i]:
        # print(i-1)
        # print(arrangement[i-1])
        # print(arrangement[i])
        count += 1
print(count)
