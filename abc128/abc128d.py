n, k = map(int, input().split())
v = [int(e) for e in input().split()]
m = min(n, k)
result = 0
for i in range(m + 1):
  for j in range(i + 1):
    t = v[:j]
    t.extend(v[n - (i - j):])
    t.sort()
    l = k - i
    while len(t) > 0 and l > 0 and t[0] < 0:
      t.pop(0)
      l -= 1
    m = sum(t)
    if m > result:
      result = m
print(result)
