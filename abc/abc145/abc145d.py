# フェルマーの小定理
p = 1000000007

X, Y = map(int, input().split())

if (X + Y) % 3 != 0:
    print(0)
    exit()

a = (2 * Y - X) // 3
b = (2 * X - Y) // 3

if a < 0 or b < 0:
    print(0)
    exit()

n = a + b
fac = [0] * (n + 1)
fac[0] = 1
for i in range(n):
    fac[i + 1] = fac[i] * (i + 1) % p


def mcomb(n, k):
    if n == 0 and k == 0:
        return 1
    if n < k or k < 0:
        return 0
    return fac[n] * pow(fac[n - k], p - 2, p) * pow(fac[k], p - 2, p) % p


print(mcomb(n, a))
