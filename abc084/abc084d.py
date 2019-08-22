from sys import stdin
def main():
  from math import sqrt
  readline = stdin.readline
  p = [True] * (10 ** 5 + 1)
  p[0] = False
  p[1] = False
  n = int(sqrt(10 ** 5)) + 1
  for j in range(4, 10 ** 5 + 1, 2):
    p[j] = False
  for i in range(3, n + 1, 2):
    if p[i]:
      for j in range(i + i, 10 ** 5 + 1, i):
        p[j] = False
  c = [0] * (10 ** 5 + 2)
  for i in range(2, 10 ** 5 + 2):
    c[i] = c[i - 1]
    if p[i - 2] and p[(i - 1) // 2]:
      c[i] += 1
  q = int(readline())
  for _ in range(q):
    l, r = map(int, readline().split())
    print(c[r + 2] - c[l + 1])
main()
