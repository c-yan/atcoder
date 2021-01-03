# imos 法
from sys import stdin
from itertools import accumulate

readline = stdin.readline

N, Q = map(int, readline().split())

t = [0] * (N + 1)
for _ in range(Q):
    l, r = map(int, readline().split())
    t[l - 1] += 1
    t[r] -= 1
print(''.join(str(x % 2) for x in accumulate(t[:-1])))
