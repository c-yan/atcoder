# エラトステネスの篩, 累積和
from math import sqrt

N = 10 ** 5

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

cs = [0] * (N + 1)
for i in range(3, N + 1, 2):
  if p[i] and p[(i + 1) // 2]:
    cs[i] = 1
for i in range(1, N + 1):
  cs[i] += cs[i - 1]

Q = int(input())
for _ in range(Q):
  l, r = map(int, input().split())
  print(cs[r] - cs[l - 1])
