from sys import exit
c = [list(map(int, input().split())) for _ in range(3)]
a = [None] * 3
b = [None] * 3
a[0] = 0
for j in range(3):
  b[j] = c[0][j] - a[0]
for i in range(1, 3):
  a[i] = c[i][0] - b[0]
for i in range(3):
  for j in range(3):
    if c[i][j] != a[i] + b[j]:
      print('No')
      exit()
print('Yes')
