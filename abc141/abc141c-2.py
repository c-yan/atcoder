# imos 法
N, K, Q = map(int, input().split())
cs = [0] * N
cs[0] = K
for _ in range(Q):
  A = int(input())
  if A == 1:
    cs[1] -= 1
  elif A == N:
    cs[0] -= 1
    cs[N - 1] += 1
  else:
    cs[0] -= 1
    cs[A - 1] += 1
    cs[A] -= 1
for i in range(1, N):
  cs[i] += cs[i - 1]
for i in cs:
  if i > 0:
    print('Yes')
  else:
    print('No')
