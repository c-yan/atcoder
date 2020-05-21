# フェルマーの小定理
W, H = map(int, input().split())

n = (W - 1) + (H - 1)
fac = [0] * (n + 1)
fac[0] = 1
for i in range(1, n + 1):
    fac[i] = fac[i - 1] * i % 1000000007


def mcomb(n, k):
    if n == 0 and k == 0:
        return 1
    if n < k or k < 0:
        return 0
    return fac[n] * pow(fac[n - k], 1000000005, 1000000007) * pow(fac[k], 1000000005, 1000000007) % 1000000007


print(mcomb(n, W - 1))
