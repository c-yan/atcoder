from sys import stdin

readline = stdin.readline

N = int(readline())

a = []
maxe = {}
unique = {}

for _ in range(N):
    m = int(readline())
    d = {}
    for _ in range(m):
        p, e = map(int, readline().split())
        d[p] = e
        maxe.setdefault(p, 0)
        if e > maxe[p]:
            maxe[p] = e
            unique[p] = True
        elif e == maxe[p]:
            unique[p] = False
    a.append(d)

changes = 0
for d in a:
    for p in d:
        if d[p] == maxe[p] and unique[p]:
            changes += 1
            break
nochanges = N - changes
print(changes + min(1, nochanges))
