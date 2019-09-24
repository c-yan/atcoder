# imos 法
N, M = map(int, input().split())

cs = [0] * N
for _ in range(M):
    L, R = map(int, input().split())
    cs[L - 1] += 1
    if R != N:
        cs[R] -= 1

for i in range(1, N):
    cs[i] += cs[i - 1]

print(cs.count(M))
