from collections import deque
def main():
  _map, _input, _int = map, input, int
  n, q = _map(_int, _input().split())
  values = [0] * n
  links = [[] for _ in range(n)]
  for _ in range(n - 1):
    a, b = _map(_int, _input().split())
    links[a - 1].append(b - 1)
    links[b - 1].append(a - 1)
  for _ in range(q):
    p, x = _map(_int, _input().split())
    values[p - 1] += x
  d = deque()
  d.append((0, -1))
  while len(d) != 0:
    i, p = d.popleft()
    for j in links[i]:
      if j == p:
        continue
      values[j] += values[i]
      d.append((j, i))
  print(*values)
main()
