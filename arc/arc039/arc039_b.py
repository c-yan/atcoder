N, K = map(int, open(0).read().split())

m = 1000000007


def f(n, k):
    a = 1
    b = 1
    for i in range(k):
        a *= n - i
        a %= m
        b *= i + 1
        b %= m
    return a * pow(b, m - 2, m) % m


if K >= N:
    print(f(N, K % N))
else:
    print(f(N + K - 1, K))
