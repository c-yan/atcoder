# フェルマーの小定理
W, H = map(int, input().split())

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


n = (W - 1) + (H - 1)
k = min(W - 1, H - 1)
print(mcomb(n, k))
