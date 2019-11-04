N, C = map(int, input().split())

tt = [[0] * (10 ** 5 + 1) for _ in range(C)]
for _ in range(N):
    s, t, c = map(int, input().split())
    ttc = tt[c - 1]
    for i in range(s - 1, t):
        ttc[i] = 1

ct = [0] * (10 ** 5 + 1)
for i in range(C):
    tti = tt[i]
    for j in range(10 ** 5 + 1):
        ct[j] += tti[j]

print(max(ct))
