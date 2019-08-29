n, k = map(int, input().split())
v = list(map(int, input().split()))
m = min(n, k)
result = 0
for i in range(m + 1):
  for j in range(i + 1):
    t = v[:j]
    t.extend(v[n - (i - j):])
    t.sort(reverse = True)
    l = k - i
    while len(t) > 0 and l > 0 and t[-1] < 0:
      t.pop()
      l -= 1
    result = max(result, sum(t))
print(result)
