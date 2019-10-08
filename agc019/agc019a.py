def f(n, l, price):
    if l == 0.25:
        return int(n / 0.25 * price[l])
    t = int(n / l)
    return min(f(n - l * t, l / 2, price) + t * price[l], f(n, l / 2, price))


Q, H, S, D = map(int, input().split())
N = int(input())

price = {0.25: Q, 0.5: H, 1.0: S, 2.0: D}
print(f(N, 2.0, price))
