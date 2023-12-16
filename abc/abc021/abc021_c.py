from sys import stdin
from collections import deque
from functools import lru_cache

readline = stdin.readline
m = 1000000007

N = int(readline())
a, b = map(int, readline().split())
M = int(readline())

links = {}
for _ in range(M):
    x, y = map(int, readline().split())
    links.setdefault(x, [])
    links[x].append(y)
    links.setdefault(y, [])
    links[y].append(x)

dist = {a: 0}
q = deque([a])
while q:
    x = q.popleft()
    for y in links[x]:
        if y in dist:
            continue
        dist[y] = dist[x] + 1
        q.append(y)


@lru_cache(maxsize=None)
def f(p):
    if p == a:
        return 1
    d = dist[p]
    result = 0
    for x in links[p]:
        if dist[x] != d - 1:
            continue
        result += f(x)
        result %= m
    return result


print(f(b))
