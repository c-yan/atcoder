from heapq import heappop, heappush

N, K, *X = map(int, open(0).read().split())

d = {}
for i in range(N):
    d[X[i]] = i + 1

q = []
result = []
for x in X:
    heappush(q, -x)
    if len(q) == K + 1:
        _ = heappop(q)
    if len(q) == K:
        result.append(d[-q[0]])
print(*result, sep='\n')
