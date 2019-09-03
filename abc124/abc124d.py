n, k = map(int, input().split())
s = list(map(int, input()))
j = 1
r = 0
t = []
for i in range(n):
  if s[i] == j:
    r += 1
  else:
    t.append(r)
    r = 1
    j ^= 1
t.append(r)
if j == 0:
  t.append(0)
if k >= (len(t) - 1) // 2:
  print(sum(t))
else:
  result = sum(t[:2 * k + 1])
  j = sum(t[:2 * k + 1])
  i = 2
  while i + 2 * k < len(t):
    j += t[i + 2 * k - 1] + t[i + 2 * k] - (t[i - 2] + t[i - 1])
    result = max(result, j)
    i += 2
  print(result)
