from sys import stdin
from collections import deque

readline = stdin.readline

m = 1000000007
INF = 10 ** 18

N, M = map(int, readline().split())

links = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, readline().split())
    links[A - 1].append(B - 1)
    links[B - 1].append(A - 1)

costs = [INF] * N
counts = [0] * N

costs[0] = 0
counts[0] = 1
q = deque([0])
while q:
    i = q.popleft()
    c = costs[i]
    for j in links[i]:
        if c + 1 > costs[j]:
            continue
        elif c + 1 == costs[j]:
            counts[j] += counts[i]
            counts[j] %= m
        elif c + 1 < costs[j]:
            costs[j] = c + 1
            counts[j] = counts[i]
            q.append(j)
print(counts[N - 1])
