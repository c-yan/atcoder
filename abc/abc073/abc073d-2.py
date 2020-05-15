# PyPy なら通る
from itertools import permutations


def warshall_floyd(n, d):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                d[j][k] = min(d[j][k], d[j][i] + d[i][k])


N, M, R = map(int, input().split())
r = list(map(int, input().split()))

d = [[1000000000] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    d[A][B] = C
    d[B][A] = C
warshall_floyd(N + 1, d)

result = 1000000000
for p in permutations(r):
    t = 0
    for i in range(R - 1):
        t += d[p[i]][p[i + 1]]
    result = min(result, t)
print(result)
