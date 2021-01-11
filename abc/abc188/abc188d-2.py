from sys import stdin
from itertools import accumulate

readline = stdin .readline

N, C = map(int, readline().split())
abc = [tuple(map(int, readline().split())) for _ in range(N)]

p = set()
for a, b, _ in abc:
    p.add(a)
    p.add(b)
    p.add(b + 1)
inv = sorted(p)
fwd = {}
for i in range(len(inv)):
    fwd[inv[i]] = i

t = [0] * len(inv)
for a, b, c in abc:
    t[fwd[a]] += c
    t[fwd[b + 1]] -= c
t = list(accumulate(t))

result = 0
for i in range(len(t) - 1):
    result += min(t[i], C) * (inv[i + 1] - inv[i])
print(result)
