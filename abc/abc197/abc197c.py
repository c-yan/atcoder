from itertools import product
from functools import reduce

N, *A = map(int, open(0).read().split())

result = 10 ** 18
for p in product([True, False], N - 1)
    t = []
    x = 0
    for i in range(N):
        x |= A[i]
        if i == N - 1 or p[i]:
            t.append(x)
            x = 0
    result = min(result, reduce(lambda x, y: x ^y, t))
print(result)
