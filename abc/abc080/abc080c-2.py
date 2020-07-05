# ビット全探索
from itertools import product

N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]

result = -float('inf')
for i in product([True, False], repeat=10):
    if i.count(False) == 10:
        continue
    t = 0
    for j in range(N):
        t += P[j][sum(1 & F[j][k] for k in range(10) if i[k])]
    result = max(result, t)
print(result)
