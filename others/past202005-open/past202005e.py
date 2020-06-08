N, M, Q = map(int, input().split())

links = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    links[u].append(v)
    links[v].append(u)
c = [0] + list(map(int, input().split()))

for _ in range(Q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        x = s[1]
        print(c[x])
        for y in links[x]:
            c[y] = c[x]
    if s[0] == 2:
        x, y = s[1:]
        print(c[x])
        c[x] = y
