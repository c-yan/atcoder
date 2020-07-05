# ビット全探索
from itertools import product

N, M, X = map(int, input().split())

C = []
A = []
for i in range(N):
    t = list(map(int, input().split()))
    C.append(t[0])
    A.append(t[1:])

result = -1
for p in product([True, False], repeat = N):
    t = [0] * M
    c = 0
    for j in range(N):
        if not p[j]:
            continue
        c += C[j]
        for k in range(M):
            t[k] += A[j][k]
    if all(x >= X for x in t):
        if result == -1:
            result = c
        else:
            result = min(result, c)
print(result)
