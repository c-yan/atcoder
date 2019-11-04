N, C = map(int, input().split())

tt = [[0] * (10 ** 5 + 1) for _ in range(C)]
for _ in range(N):
    s, t, c = map(int, input().split())
    for i in range(s - 1, t):
        tt[c - 1][i] = 1

ct = [0] * (10 ** 5 + 1)
for i in range(C):
    for j in range(10 ** 5 + 1):
        ct[j] += tt[i][j]

print(max(ct))
