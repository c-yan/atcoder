from sys import stdin

readline = stdin.readline

H, W, N = map(int, readline().split())
rca = [tuple(map(int, readline().split())) for _ in range(N)]

dpy = [-1] * H
dpx = [-1] * W
result = [0] * N
prev = -1
qy = []
qx = []
for i in sorted(range(N), key=lambda x: rca[x][2], reverse=True):
    r, c, a = rca[i][0] - 1, rca[i][1] - 1, rca[i][2]
    if prev != a:
        for y, t in qy:
            dpy[y] = max(dpy[y], t)
        for x, t in qx:
            dpx[x] = max(dpx[x], t)
        qy.clear()
        qx.clear()
    t = max(dpy[r] + 1, dpx[c] + 1)
    result[i] = t
    if t != 0:
        qy.append((r, t))
        qx.append((c, t))
    prev = a
print(*result, sep='\n')
