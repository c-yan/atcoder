# 二分探索
from bisect import bisect_left

N, M = map(int, input().split())
PY = [list(map(int, input().split())) for _ in range(M)]

t = [[] for _ in range(N)]
for P, Y in PY:
    t[P - 1].append(Y)

for i in range(N):
    t[i].sort()

for P, Y in PY:
    print("%06d%06d" % (P, bisect_left(t[P - 1], Y) + 1))
