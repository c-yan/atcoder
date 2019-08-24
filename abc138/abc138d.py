from sys import stdin
def main():
  from builtins import int, map, range
  readline = stdin.readline
  n, q = map(int, readline().split())
  values = [0] * n
  links = [[] for _ in range(n)]
  for _ in range(n - 1):
    a, b = map(int, readline().split())
    links[a - 1].append(b - 1)
    links[b - 1].append(a - 1)
  for _ in range(q):
    p, x = map(int, readline().split())
    values[p - 1] += x
  s = [(0, -1)]
  while s:
    i, p = s.pop()
    for j in links[i]:
      if j == p:
        continue
      values[j] += values[i]
      s.append((j, i))
  print(*values)
main()
