# imos 法
from sys import stdin
from itertools import accumulate

readlie = stdin.readline

N, M = map(int, readlie().split())

t = [0] * (N + 1)  # t はIDカードで通れるゲートの数
for _ in range(M):
    L, R = map(int, readlie().split())
    t[L - 1] += 1
    t[R] -= 1
print(list(accumulate(t[:-1])).count(M))
