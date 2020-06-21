# フェルマーの小定理
X, Y = map(int, input().split())

m = 1000000007
def mcomb(n, k):
    a = 1
    b = 1
    for i in range(k):
        a *= n - i
        a %= m
        b *= i + 1
        b %= m
    return a * pow(b, m - 2, m) % m
if (X + Y) % 3 != 0:
    print(0)
    exit()

a = (2 * Y - X) // 3
b = (2 * X - Y) // 3

if a < 0 or b < 0:
    print(0)
    exit()

n = a + b
print(mcomb(n, a))
