A, B, C, D = list(map(int, input()))
for i in range(8):
  if i & 1 == 0:
    tb = B
  else:
    tb = -B
  if i & 2 == 0:
    tc = C
  else:
    tc = -C
  if i & 4 == 0:
    td = D
  else:
    td = -D
  if sum([A, tb, tc, td]) == 7:
    break
print("%d%+d%+d%+d=7" % (A, tb, tc, td))
