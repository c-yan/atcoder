# imos 法
from sys import stdin
from itertools import accumulate
from operator import itemgetter

readline = stdin.readline

N, C = map(int, readline().split())
stc = [tuple(map(int, readline().split())) for _ in range(N)]
stc.sort(key=itemgetter(2, 0))

a = [0] * (10 ** 5 + 1)
pt, pc = -1, -1
for s, t, c in stc:
    if pt == s and pc == c:
        a[s] += 1
    else:
        a[s - 1] += 1
    a[t] -= 1
    pt, pc = t, c
print(max(accumulate(a[:-1])))
