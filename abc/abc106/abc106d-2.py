# 累積和
# PyPy なら通る
N, M, Q = map(int, input().split())

t = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    L, R = map(int, input().split())
    t[L][R] += 1

for i in range(N + 1):
    for j in range(N):
        t[i][j + 1] += t[i][j]

result = []
for _ in range(Q):
    p, q = map(int, input().split())
    result.append(sum(t[i][q] - t[i][i - 1] for i in range(p, q + 1)))
print('\n'.join(str(v) for v in result))
