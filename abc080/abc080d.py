N, C = map(int, input().split())

tt = [[0] * (2 * 10 ** 5 + 1) for _ in range(30)]
for _ in range(N):
    s, t, c = map(int, input().split())
    ttc = tt[c - 1]
    for i in range(s * 2 - 1, t * 2):
        ttc[i] = 1

ct = [0] * (2 * 10 ** 5 + 1)
for i in range(30):
    tti = tt[i]
    for j in range(2 * 10 ** 5 + 1):
        ct[j] += tti[j]

print(max(ct))
