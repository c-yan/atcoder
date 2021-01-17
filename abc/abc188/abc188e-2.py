from sys import setrecursionlimit, stdin
from functools import lru_cache

setrecursionlimit(10 ** 6)
readline = stdin.readline

N, M = map(int, readline().split())
A = list(map(int, readline().split()))

links = [[] for _ in range(N)]
for _ in range(M):
    X, Y = map(lambda x: int(x) - 1, readline().split())
    links[X].append(Y)


@lru_cache(maxsize=None)
def dfs(x):
    result = A[x]
    for y in links[x]:
        result = max(result, dfs(y))
    return result


result = -(10 ** 18)
for i in range(N):
    if len(links[i]) == 0:
        continue
    result = max(result, max(dfs(j) for j in links[i]) - A[i])
print(result)
