from sys import setrecursionlimit
setrecursionlimit(10000)

A, B = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dp = [[[None] * (B + 1) for _ in range(A + 1)] for _ in range(2)]

def f(u, i, j):
  if i == A and j == B:
    return (0, 0)
  t = dp[u][i][j]
  if t is not None:
    return t
  t0 = None
  t1 = None
  if i < A:
    x, y = f(u ^ 1, i + 1, j)
    if u == 0:
      t0 = (x + a[i], y)
    else:
      t0 = (x, y + a[i])
  if j < B:
    x, y = f(u ^ 1, i, j + 1)
    if u == 0:
      t1 = (x + b[j], y)
    else:
      t1 = (x, y + b[j])
  if t0 is None:
    result = t1
  elif t1 is None:
    result = t0
  else:
    if t0[u] > t1[u]:
      result = t0
    elif t0[u] < t1[u]:
      result = t1
    else:
      if t0[u ^ 1] > t1[u ^ 1]:
        result = t1
      else:
        result = t0
  dp[u][i][j] = result
  return result

print(f(0, 0, 0)[0])
