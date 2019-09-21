a, b = [int(e) for e in input().split()]
if (a + b) % 2 != 0:
  print('IMPOSSIBLE')
else:
  print((a + b) // 2)
