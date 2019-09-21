INF = float('inf')
n, ma, mb = map(int, input().split())
cmax = n * 10
t = [[INF] * (cmax + 1) for _ in range(cmax + 1)]
for _ in range(n):
  a, b, c = map(int, input().split())
  for aa in range(cmax, 0, -1):
    for bb in range(cmax, 0, -1):
      if t[aa][bb] == INF:
        continue
      t[aa + a][bb + b] = min(t[aa + a][bb + b], t[aa][bb] + c)
  t[a][b] = min(t[a][b], c)
result = INF
for a in range(1, cmax):
  for b in range(1, cmax):
    if a * mb == b * ma:
      result = min(result, t[a][b])
if result == INF:
  result = -1
print(result)
