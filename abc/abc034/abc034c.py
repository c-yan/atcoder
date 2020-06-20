# フェルマーの小定理
W, H = map(int, input().split())

m = 1000000007

n = (W - 1) + (H - 1)
fac = [0] * (n + 1)
fac[0] = 1
for i in range(1, n + 1):
    fac[i] = fac[i - 1] * i % m


def mcomb(n, k):
    if n == 0 and k == 0:
        return 1
    if n < k or k < 0:
        return 0
    return fac[n] * pow(fac[n - k], m - 2, m) * pow(fac[k], m - 2, m) % m


print(mcomb(n, W - 1))
