n = int(input())
a = list(map(int, input().split()))
c = [0] * (n + 1)
for i in range(n):
  c[i + 1] = c[i] + a[i]
d = {}
for i in range(1, n + 1):
  if c[i] not in d:
    d[c[i]] = 0
  d[c[i]] += 1
result = 0
if 0 in d:
  result += d[0]
for k in d:
  if d[k] != 1:
    result += d[k] * (d[k] - 1) // 2
print(result)
