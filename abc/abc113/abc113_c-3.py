from sys import stdin

readline = stdin.readline


def shrink(a):
    inv = sorted(set(a))
    n = len(inv)
    fwd = {}
    for i in range(n):
        fwd[inv[i]] = i
    return n, fwd, inv


N, M = map(int, readline().split())
PY = [tuple(map(int, readline().split())) for _ in range(M)]

t = [[] for _ in range(N)]
for P, Y in PY:
    t[P - 1].append(Y)

fwds = []
for i in range(N):
    fwds.append(shrink(t[i])[1])

result = []
for P, Y in PY:
    result.append('%06d%06d' % (P, fwds[P - 1][Y] + 1))
print(*result, sep='\n')
