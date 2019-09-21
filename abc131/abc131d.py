import sys
from functools import cmp_to_key
n = int(input())
data = [[int(j) for j in input().split()] for i in range(n)]
t = 0
data.sort(key = cmp_to_key(lambda x, y: x[1] - y[1]))
for d in data:
  t += d[0]
  if t > d[1]:
    print('No')
    sys.exit()
print('Yes')
