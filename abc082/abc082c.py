n = int(input())
a = list(map(int, input().split()))
d = {}
for i in range(n):
  if a[i] in d:
    d[a[i]] += 1
  else:
    d[a[i]] = 1
result = 0
for k in d:
  if d[k] < k:
    result += d[k]
  elif d[k] > k:
    result += d[k] - k
print(result)
