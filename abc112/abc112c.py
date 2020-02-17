N = int(input())
xyh = [tuple(map(int, input().split())) for _ in range(N)]

for e in xyh:
    if e[2] != 0:
        t = e

candidates = []
for cy in range(101):
    for cx in range(101):
        candidates.append((cx, cy, t[2] + abs(t[0] - cx) + abs(t[1] - cy)))

for e in xyh:
    nc = []
    for c in candidates:
        if e[2] == max(c[2] - abs(e[0] - c[0]) - abs(e[1] - c[1]), 0):
            nc.append(c)
    candidates = nc

print(*candidates[0])
