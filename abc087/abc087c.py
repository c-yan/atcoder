n = int(input())
a = [list(map(int, input().split())) for _ in range(2)]
b = [[0] * n for _ in range(2)]
b[0][0] = a[0][0]
for i in range(1, n):
  b[0][i] = b[0][i - 1] + a[0][i]
b[1][n - 1] = a[1][n - 1]
for i in range(1, n):
  b[1][n - 1 - i] = b[1][n - i] + a[1][n - 1 - i]
print(max(b[0][i] + b[1][i] for i in range(n)))
