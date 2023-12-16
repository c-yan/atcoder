from sys import stdin
from itertools import accumulate

readline = stdin .readline


def shrink(a):
    inv = sorted(set(a))
    n = len(inv)
    fwd = {}
    for i in range(n):
        fwd[inv[i]] = i
    return n, fwd, inv


N, C = map(int, readline().split())
abc = [tuple(map(int, readline().split())) for _ in range(N)]

p = []
for a, b, _ in abc:
    p.append(a)
    p.append(b)
    p.append(b + 1)
n, fwd, inv = shrink(p)

t = [0] * n
for a, b, c in abc:
    t[fwd[a]] += c
    t[fwd[b + 1]] -= c
t = list(accumulate(t))

result = 0
for i in range(n - 1):
    result += min(t[i], C) * (inv[i + 1] - inv[i])
print(result)
