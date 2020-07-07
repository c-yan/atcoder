# 累積和(2次元)
N, M, Q = map(int, input().split())

t = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    L, R = map(int, input().split())
    t[L][R] += 1

for i in range(N + 1):
    for j in range(N):
        t[i][j + 1] += t[i][j]

for i in range(N):
    for j in range(N + 1):
        t[i + 1][j] += t[i][j]

result = []
for _ in range(Q):
    p, q = map(int, input().split())
    result.append(t[q][q] + t[p - 1][p - 1] - t[p - 1][q] - t[q][p - 1])
print(*result, sep='\n')
