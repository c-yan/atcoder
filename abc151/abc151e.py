N, K = map(int, input().split())
A = list(map(int, input().split()))

fac = [0] * (N + 1)
fac[0] = 1
for i in range(N):
    fac[i + 1] = fac[i] * (i + 1) % 1000000007


def mcomb(n, k):
    if n == 0 and k == 0:
        return 1
    if n < k or k < 0:
        return 0
    return fac[n] * pow(fac[n - k], 1000000005, 1000000007) * pow(fac[k], 1000000005, 1000000007) % 1000000007


A.sort(reverse=True)
result = 0
for i in range(N - K + 1):
    result += A[i] * mcomb(N - (i + 1), K - 1)
    result %= 1000000007

A.sort()
t = 0
for i in range(N - K + 1):
    t += A[i] * mcomb(N - (i + 1), K - 1)
    t %= 1000000007

result -= t
result += 1000000007
result %= 1000000007
print(result)
