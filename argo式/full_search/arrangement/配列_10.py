import random
"""
N は 1 以上 100 以下の整数
"""
# num = random.randint(1, 100)
num = int(input())
# print(f"numは{num}です")

"""
Ai は 1 以上 9 以下の整数 (0≤i≤N−1)
"""
# arrangement = [random.randint(1, 9) for p in range(1, num)]
arrangement = list(map(int, input().split()))
# print(arrangement)

"""
N 個の整数の中に一番多く出てくる数字を求めるプログラムを作成してください。 
ただし、答えは一つに定まることが保証されているものとします。
例：
N=5
arrangement= [1, 2, 1, 4, 5]
上記の場合は1が2回登場していて、最大なので1
"""

list = []
for i in range(1, 10):
    count = 0
    for x in arrangement:
        if x == i:
            count += 1
    list.append(count)
# print(list)
# print(max(list))
print(list.index(max(list))+1)
