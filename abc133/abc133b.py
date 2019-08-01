l, r = [int(e) for e in input().split()]
m = 2019
for i in range(l, r):
  ir = i % 2019
  for j in range(i + 1, r + 1):
    t = (ir * j) % 2019
    if t < m:
      m = t
    if m == 0:
      break
  if m == 0:
    break
print(m)
