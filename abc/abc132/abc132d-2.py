# フェルマーの小定理
N, K = map(int, input().split())

n = max(K, N - K + 1)
fac = [0] * (n + 1)
fac[0] = 1
for i in range(n):
    fac[i + 1] = fac[i] * (i + 1) % 1000000007


def mcomb(n, k):
    if n == 0 and k == 0:
        return 1
    if n < k or k < 0:
        return 0
    return fac[n] * pow(fac[n - k], 1000000005, 1000000007) * pow(fac[k], 1000000005, 1000000007) % 1000000007


result = []
for i in range(1, K + 1):
    result.append(mcomb(K - 1, i - 1) * mcomb(N - K + 1, i) % 1000000007)
print('\n'.join(str(i) for i in result))
