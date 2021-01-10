from sys import stdin

readline = stdin.readline

N, M = map(int, readline().split())
A = list(map(int, readline().split()))

links = [[] for _ in range(N)]
for _ in range(M):
    X, Y = map(lambda x: int(x) - 1, readline().split())
    links[X].append(Y)

maxvs = [None] * N
result = -(10 ** 18)
for i in range(N - 1, -1, -1):
    if len(links[i]) == 0:
        maxvs[i] = A[i]
        continue
    maxv = max(maxvs[j] for j in links[i])
    result = max(result, maxv - A[i])
    maxvs[i] = max(maxv, A[i])
print(result)
