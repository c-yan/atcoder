H, W, K = map(int, input().split())
s = [input() for _ in range(H)]

a = [[-1] * W for _ in range(H)]

sbs = []
n = 1
for i in range(H):
    si = s[i]
    for j in range(W):
        if si[j] == '#':
            a[i][j] = n
            n += 1
            sbs.append((i, j))

for sb in sbs:
    i, j = sb
    n = a[i][j]
    t, l = i - 1, j - 1
    r = j + 1
    while t > -1:
        if a[t][j] != -1:
            break
        t -= 1
    t += 1
    while l > -1:
        if a[i][l] != -1:
            break
        l -= 1
    l += 1
    while r < W:
        if a[i][r] != -1:
            break
        r += 1
    r -= 1
    for y in range(t, i + 1):
        ay = a[y]
        for x in range(l, r + 1):
            ay[x] = n

for h in range(H - 1, -1, -1):
    if a[h][0] != -1:
        break
h += 1

for i in range(h, H):
    ai1 = a[i - 1]
    ai = a[i]
    for j in range(W):
        ai[j] = ai1[j]

for i in range(H):
    print(*a[i])
