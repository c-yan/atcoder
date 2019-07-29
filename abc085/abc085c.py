import sys
n, y = [int(e) for e in raw_input().split()]
for i in range(n + 1):
  for j in range(n + 1 - i):
    k = n - i - j
    if 10000 * i + 5000 * j + 1000 * k == y:
      print "%d %d %d" % (i, j, k)
      sys.exit()
print "-1 -1 -1"
