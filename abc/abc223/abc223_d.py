from sys import stdin
from heapq import heappop, heappush, heapify

readline = stdin.readline

N, M = map(int, readline().split())
AB = [tuple(map(int, readline().split())) for _ in range(M)]

fronts = [set() for _ in range(N + 1)]
rears = [set() for _ in range(N + 1)]

availables = set(range(1, N + 1))
for a, b in AB:
    if b in availables:
        availables.remove(b)
    fronts[b].add(a)
    rears[a].add(b)
availables = list(availables)
heapify(availables)

result = []
while availables:
    x = heappop(availables)
    result.append(x)
    for y in rears[x]:
        fronts[y].remove(x)
        if len(fronts[y]) == 0:
            heappush(availables, y)
if len(result) != N:
    print(-1)
else:
    print(*result)
