from sys import stdin

readline = stdin.readline

H, W, N, M = map(int, readline().split())
AB = [tuple(map(lambda x: int(x) - 1, readline().split())) for _ in range(N)]
CD = [tuple(map(lambda x: int(x) - 1, readline().split())) for _ in range(M)]

t = [[0] * W for _ in range(H)]

ly = [[] for _ in range(H)]
lt = [[] for _ in range(W)]
for a, b in AB:
    ly[a].append(b)
    lt[b].append(a)
for i in range(H):
    ly[i].sort()
for i in range(W):
    lt[i].sort()

by = [[] for _ in range(H)]
bt = [[] for _ in range(W)]
for c, d in CD:
    by[c].append(d)
    bt[d].append(c)
for i in range(H):
    by[i].append(W)
    by[i].sort()
for i in range(W):
    bt[i].append(H)
    bt[i].sort()

result = 0
for h in range(H):
    lyh = ly[h]
    i = 0
    pd = -1
    for d in by[h]:
        j = i
        while j < len(lyh) and lyh[j] < d:
            j += 1
        if i != j:
            for w in range(pd + 1, d):
                t[h][w] = 1
            i = j
        pd = d
for w in range(W):
    ltw = lt[w]
    i = 0
    pc = -1
    for c in bt[w]:
        j = i
        while j < len(ltw) and ltw[j] < c:
            j += 1
        if i != j:
            for h in range(pc + 1, c):
                t[h][w] = 1
            i = j
        pc = c
print(sum(sum(x) for x in t))
