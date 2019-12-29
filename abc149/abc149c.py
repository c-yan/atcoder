from math import sqrt

N = 10 ** 6

p = [True] * (N + 1)
p[0] = False
p[1] = False
n = int(sqrt(N) + 1)
for j in range(4, N + 1, 2):
  p[j] = False
for i in range(3, n + 1, 2):
  if p[i]:
    for j in range(i + i, N + 1, i):
      p[j] = False


X = int(input())
for i in range(X, N + 1):
    if p[i]:
        print(i)
        break
