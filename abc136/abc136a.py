a, b, c = [int(e) for e in input().split()]
if a - b > c:
  print(0)
else:
  print(c - (a - b))
