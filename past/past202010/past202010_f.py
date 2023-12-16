from sys import stdin

readline = stdin.readline

N, K = map(int, readline().split())

c = {}
for _ in range(N):
    S = readline()[:-1]
    c.setdefault(S, 0)
    c[S] += 1

d = {}
for k in c:
    a = c[k]
    d.setdefault(a, [])
    d[a].append(k)

c = 0
for a in sorted(d, reverse=True):
    l = len(d[a])
    if c + l < K:
        c += l
        continue
    if l == 1:
        print(d[a][0])
    else:
        print('AMBIGUOUS')
    break
