from sys import setrecursionlimit
from functools import lru_cache


@lru_cache(maxsize=None)
def f(n):
    if n == 0:
        return 0
    if n == 1:
        return D
    t = []
    if n % 2 == 0:
        t.append(f(n // 2) + A)
    else:
        t.append(f((n - 1) // 2) + D + A)
        t.append(f((n + 1) // 2) + D + A)
    if n % 3 == 0:
        t.append(f(n // 3) + B)
    else:
        m = n % 3
        t.append(f((n - m) // 3) + m * D + B)
        t.append(f((n + (3 - m)) // 3) + (3 - m) * D + B)
    if n % 5 == 0:
        t.append(f(n // 5) + C)
    else:
        m = n % 5
        t.append(f((n - m) // 5) + m * D + C)
        t.append(f((n + (5 - m)) // 5) + (5 - m) * D + C)
    t.append(abs(n) * D)
    return min(t)


setrecursionlimit(10 ** 6)

T = int(input())

result = []
for _ in range(T):
    N, A, B, C, D = map(int, input().split())
    f.cache_clear()
    result.append(f(N))
print(*result, sep='\n')
