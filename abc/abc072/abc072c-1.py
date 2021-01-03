# imos 法
from itertools import accumulate

N, *a = map(int, open(0).read().split())

t = [0] * (10 ** 5 + 3)  # t[X + 1] は操作により ai = X となりうる i の個数
for x in a:
    t[x] += 1
    t[x + 3] -= 1
print(max(accumulate(t[:-1])))
