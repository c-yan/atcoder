# Union Find 木
from sys import stdin

def main():
  def find(parent, i):
    t = parent[i]
    if t == -1:
      return i
    t = find(parent, t)
    parent[i] = t
    return t

  def unite(parent, i, j):
    i = find(parent, i)
    j = find(parent, j)
    if i == j:
      return
    parent[i] = j

  from builtins import int, map, range
  readline = stdin.readline

  n, k, l = map(int, readline().split())

  roads = [-1] * n
  rails = [-1] * n

  for i in range(k):
    p, q = map(int, readline().split())
    unite(roads, p - 1, q - 1)

  for i in range(l):
    p, q = map(int, readline().split())
    unite(rails, p - 1, q - 1)

  d = {}
  for i in range(n):
    t = (find(roads, i), find(rails, i))
    if t in d:
      d[t] += 1
    else:
      d[t] = 1

  print(*[d[(find(roads, i), find(rails, i))] for i in range(n)])

main()
