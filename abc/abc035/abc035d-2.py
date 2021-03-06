from sys import stdin
from collections import deque

readline = stdin.readline
INF = 10 ** 20

N, M, T = map(int, input().split())
A = list(map(int, input().split()))

links = [[] for _ in range(N)]
revlinks = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    links[a - 1].append((b - 1, c))
    revlinks[b - 1].append((a - 1, c))

from0 = [INF] * N
from0[0] = 0
q = deque([0])
while q:
    a = q.popleft()
    for b, c in links[a]:
        nc = from0[a] + c
        if from0[b] > nc:
            from0[b] = nc
            q.append(b)

to0 = [INF] * N
to0[0] = 0
q = deque([0])
while q:
    a = q.popleft()
    for b, c in revlinks[a]:
        nc = to0[a] + c
        if to0[b] > nc:
            to0[b] = nc
            q.append(b)

result = 0
for i in range(N):
    result = max(result, A[i] * (T - from0[i] - to0[i]))
print(result)
