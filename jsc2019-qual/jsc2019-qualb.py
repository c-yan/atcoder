n, k = map(int, input().split())
a = list(map(int, input().split()))
v1 = 0
for i in range(n - 1):
  for j in range(i + 1, n):
    if a[i] > a[j]:
      v1 += 1
v2 = 0
for i in range(n):
  for j in range(n):
    if a[i] > a[j]:
      v2 += 1

t = v1 * k + v2 * k * (k - 1) // 2
print(t % (10 ** 9 + 7))
