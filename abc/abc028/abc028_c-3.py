A, B, C, D, E = map(int, input().split())

if B - A < D - C:
  print(A + D + E)
else:
  print(B + C + E)
