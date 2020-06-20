# フェルマーの小定理
N, K = map(int, input().split())

m = 1000000007

n = max(K, N - K + 1)
fac = [0] * (n + 1)
fac[0] = 1
for i in range(n):
    fac[i + 1] = fac[i] * (i + 1) % m


def mcomb(n, k):
    if n == 0 and k == 0:
        return 1
    if n < k or k < 0:
        return 0
    return fac[n] * pow(fac[n - k], m - 2, m) * pow(fac[k], m - 2, m) % m


result = []
for i in range(1, K + 1):
    result.append(mcomb(K - 1, i - 1) * mcomb(N - K + 1, i) % m)
print('\n'.join(str(i) for i in result))
