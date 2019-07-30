def count_rewrite(v):
  ct = {}
  for x in v:
    if x in ct:
      ct[x] += 1
    else:
      ct[x] = 1
  total = 0
  for x in ct:
    total += ct[x]
  best = 0
  for x in ct:
    if ct[x] > best:
      best = ct[x]
      maxv = x
  del ct[maxv]
  second = 0
  for x in ct:
    if ct[x] > second:
      second = ct[x]
  return maxv, total - best, total - second
n = int(input())
v = [int(e) for e in input().split()]
r1 = count_rewrite(v[::2])
r2 = count_rewrite(v[1::2])
if r1[0] != r2[0]:
  print(r1[1] + r2[1])
else:
  if r1[2] >= r2[2]:
    print(r1[1] + r2[2])
  else:
    print(r1[2] + r2[1])
