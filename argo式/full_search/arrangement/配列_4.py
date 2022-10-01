import random
"""
N は 1 以上 100 以下の整数
"""
# num = random.randint(1, 100)
num = map(int, input().split())
# print(f"numは{num}です")
"""
V は 1 以上 100 以下の整数
"""
# value = random.randint(1, 100)
value = map(int, input().split())
# print(f"valueは{value}です")

"""
Ai は 1 以上 100 以下の整数 (0≤i≤N−1)
"""
# arrangement = [random.randint(1, 100) for p in range(0, num)]
arrangement = list(map(int, input().split())) 
# print(arrangement)

"""
arrangementの内部で、最も右にあるvalueが前から何番目にあるか
V が存在しない場合は -1 と出力する

リスト内包表記でリストを全て返してみた
https://note.nkmk.me/python-list-index/
"""

if [i for i, x in enumerate(arrangement) if x == value] == []:
    print(-1)
else:
    # print([i for i, x in enumerate(arrangement) if x == value])
    print(max([i for i, x in enumerate(arrangement) if x == value]))
