from sys import stdin

readline = stdin.readline

N, M = map(int, readline().split())
A = list(map(int, readline().split()))
XY = [tuple(map(lambda x: int(x) - 1, readline().split())) for _ in range(M)]

links = [[] for _ in range(N)]
for x, y in XY:
    links[x].append(y)

maxvs = [None] * N
result = -(10 ** 18)
for i in range(N - 1, -1, -1):
    maxv = 0
    for j in links[i]:
        maxv = max(maxv, maxvs[j])
    if len(links[i]) != 0:
        result = max(result, maxv - A[i])
    maxvs[i] = max(maxv, A[i])
print(result)
