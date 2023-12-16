n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

x.sort()
a = 0
for i in range(n):
  a += x[i] * (i - (n - 1 - i))
  a %= 1000000007

y.sort()
b = 0
for i in range(m):
  b += y[i] * (i - (m - 1 - i))
  b %= 1000000007

print(a * b % 1000000007)
