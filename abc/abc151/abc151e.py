# フェルマーの小定理
N, K = map(int, input().split())
A = list(map(int, input().split()))

m = 1000000007

fac = [0] * (N + 1)
fac[0] = 1
for i in range(N):
    fac[i + 1] = fac[i] * (i + 1) % m


def mcomb(n, k):
    if n == 0 and k == 0:
        return 1
    if n < k or k < 0:
        return 0
    return fac[n] * pow(fac[n - k], m - 2, m) * pow(fac[k], m - 2, m) % m


A.sort(reverse=True)
result = 0
for i in range(N - K + 1):
    result += A[i] * mcomb(N - (i + 1), K - 1)
    result %= m

A.sort()
t = 0
for i in range(N - K + 1):
    t += A[i] * mcomb(N - (i + 1), K - 1)
    t %= m

result -= t
result %= m
print(result)
