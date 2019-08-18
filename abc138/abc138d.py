def main():
  _map, _range, _int = map, range, int
  n, q = _map(_int, input().split())
  values = [0] * (n + 1)
  parents = [0] * (n + 1)
  for _ in _range(n - 1):
    a, b = _map(_int, input().split())
    parents[b] = a
  for _ in _range(q):
    p, x = _map(_int, input().split())
    values[p] += x
  for i in _range(1, n + 1):
    values[i] += values[parents[i]]
  print(*values[1:])
main()
