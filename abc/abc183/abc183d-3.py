N, W = map(int, input().split())

a = []
for _ in range(N):
    S, T, P = map(int, input().split())
    a.append((S, P))
    a.append((T, -P))

a.sort()
b = []
prev = -1
c = 0
for t, p in a:
    if prev != t:
        b.append(c)
    prev = t
    c += p
b.append(c)

if max(b) <= W:
    print('Yes')
else:
    print('No')
