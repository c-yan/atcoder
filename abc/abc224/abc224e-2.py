from sys import stdin

readline = stdin.readline

H, W, N = map(int, readline().split())
rca = [tuple(map(int, readline().split())) for _ in range(N)]

q = {}
for i in range(N):
    _, _, a = rca[i]
    q.setdefault(a, [])
    q[a].append(i)

dpy = [-1] * (H + 1)
dpx = [-1] * (W + 1)
result = [0] * N
for a in sorted(q, reverse=True):
    for i in q[a]:
        r, c, _ = rca[i]
        result[i] = max(dpy[r] + 1, dpx[c] + 1)
    for i in q[a]:
        r, c, _ = rca[i]
        dpy[r] = max(dpy[r], result[i])
        dpx[c] = max(dpx[c], result[i])
print(*result, sep='\n')
