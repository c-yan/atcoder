n = input()
if int(n) % sum(map(int, n)) == 0:
  print('Yes')
else:
  print('No')
