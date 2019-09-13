Q, H, S, D = map(int, input().split())
price = { 0.25: Q, 0.5: H, 1.0: S, 2.0: D }
N = int(input())
def f(n, l):
  if l == 0.25:
    return int(n / 0.25) * price[l]
  t = int(n / l)
  return min(f(n - l * t, l / 2) + t * price[l], f(n, l / 2))
print(int(f(N, 2.0)))
