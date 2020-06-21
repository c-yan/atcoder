# フェルマーの小定理
X, Y = map(int, input().split())

m = 1000000007


def make_factorial_table(n):
    result = [0] * (n + 1)
    result[0] = 1
    for i in range(1, n + 1):
        result[i] = result[i - 1] * i % m
    return result


def mcomb(n, k):
    if n == 0 and k == 0:
        return 1
    if n < k or k < 0:
        return 0
    return fac[n] * pow(fac[n - k], m - 2, m) * pow(fac[k], m - 2, m) % m


if (X + Y) % 3 != 0:
    print(0)
    exit()

a = (2 * Y - X) // 3
b = (2 * X - Y) // 3

if a < 0 or b < 0:
    print(0)
    exit()

n = a + b
fac = make_factorial_table(n)
print(mcomb(n, a))
