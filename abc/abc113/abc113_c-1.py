# 二分探索
from sys import stdin
from bisect import bisect_left

readline = stdin.readline

N, M = map(int, readline().split())
PY = [tuple(map(int, readline().split())) for _ in range(M)]

t = [[] for _ in range(N)]
for P, Y in PY:
    t[P - 1].append(Y)

for i in range(N):
    t[i].sort()

result = []
for P, Y in PY:
    result.append('%06d%06d' % (P, bisect_left(t[P - 1], Y) + 1))
print(*result, sep='\n')
