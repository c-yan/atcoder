from sys import stdin

readline = stdin.readline

H, W, N = map(int, readline().split())
rca = [tuple(map(int, readline().split())) for _ in range(N)]

my = [-1 for _ in range(H)]
mx = [-1 for _ in range(W)]
for r, c, a in rca:
    r, c = r - 1, c - 1
    my[r] = max(my[r], a)
    mx[c] = max(mx[c], a)

dpy = [0] * H
dpx = [0] * W
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
    t = 0
    if a < my[r]:
        t = dpy[r] + 1
    if a < mx[c]:
        t = max(dpx[c] + 1, t)
    result[i] = t
    if t != 0:
        qy.append((r, t))
        qx.append((c, t))
    prev = a
print(*result, sep='\n')
