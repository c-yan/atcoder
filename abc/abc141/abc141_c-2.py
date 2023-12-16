# imos 法
from itertools import accumulate

N, K, Q, *A = map(int, open(0).read().split())

t = [0] * N
t[0] = K
for a in A:
    t[0] -= 1
    t[a - 1] += 1
    if a < N:
        t[a] += 1

result = []
for x in accumulate(t):
    if x > 0:
        result.append('Yes')
    else:
        result.append('No')
print(*result, sep='\n')
