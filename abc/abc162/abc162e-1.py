from functools import lru_cache

m = 1000000007

N, K = map(int, input().split())


@lru_cache(maxsize=None)
def f(k):
    if k == 1:
        return 1
    result = pow(k, N, m)
    for i in range(2, k + 1):
        result -= f(k // i)
        result %= m
    return result


result = 0
for i in range(1, K + 1):
    result += f(K // i) * i
    result %= m
print(result)
