n = int(input())
a = list(map(int, input().split()))
c = abs(0 - a[0])
for i in range(1, n):
  c += abs(a[i - 1] - a[i])
c += abs(a[n - 1] - 0)
print(c - abs(0 - a[0]) - abs(a[0] - a[1]) + abs(0 - a[1]))
for i in range(1, n - 1):
  print(c - abs(a[i - 1] - a[i]) - abs(a[i] - a[i + 1]) + abs(a[i - 1] - a[i + 1]))
print(c - abs(a[n - 2] - a[n - 1]) - abs(a[n - 1] - 0) + abs(a[n - 2] - 0))
