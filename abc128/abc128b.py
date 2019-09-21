from functools import cmp_to_key
def cmp(x, y):
  if x[0] < y[0]:
    return -1
  elif x[0] > y[0]:
    return 1
  else:
    return int(y[1]) - int(x[1])
n = int(input())
d = [input().split() for _ in range(n)]
for i in range(n):
  d[i].append(i + 1)
d.sort(key = cmp_to_key(cmp))
for i in range(n):
  print(d[i][2])
