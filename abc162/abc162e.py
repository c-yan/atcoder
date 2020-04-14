N, K = map(int, input().split())

MOD = 10 ** 9 + 7

cache = {}
def f(k, n):
    if k == 1:
        return 1
    if k in cache:
        return cache[k]
    result = pow(k, n, MOD)
    for i in range(2, k + 1):
        result -= f(k // i, n)
        result %= MOD
    cache[k] = result
    return result


result = 0
for i in range(1, K + 1):
    result += f(K // i, N) * i
    result %= MOD
print(result)
