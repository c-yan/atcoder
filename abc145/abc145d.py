def mpow(x, n):
    result = 1
    while n != 0:
        if n & 1 == 1:
            result *= x
            result %= 1000000007
        x *= x
        x %= 1000000007
        n >>= 1
    return result


def mcomb(n, k):
    if n == 0 and k == 0:
        return 1
    if n < k or k < 0:
        return 0

    fac = [0] * (n + 1)
    fac[0] = 1
    for i in range(n):
        fac[i + 1] = fac[i] * (i + 1) % p
    return fac[n] * mpow(fac[n - k], p - 2) * mpow(fac[k], p - 2) % p


p = 1000000007

X, Y = map(int, input().split())

if (X+Y) % 3 != 0:
    print(0)
    exit()

a = (2 * Y - X) // 3
b = (2 * X - Y) // 3

if a < 0 or b < 0:
    print(0)
    exit()

print(mcomb(a + b, min(a, b)))
