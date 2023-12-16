# 優先度付きキュー
from heapq import heappush, heappop

N, M = map(int, input().split())

jobs = {}
for _ in range(N):
    A, B = map(int, input().split())
    if A in jobs:
        jobs[A].append(B)
    else:
        jobs[A] = [B]

result = 0
candidates = []
for a in range(1, M + 1):
    if a in jobs:
        for b in jobs[a]:
            heappush(candidates, -b)
    else:
        if len(candidates) == 0:
            continue
    result += -heappop(candidates)
print(result)
