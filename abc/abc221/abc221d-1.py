from sys import stdin
from itertools import accumulate

readline = stdin.readline

N = int(readline())
AB = [list(map(int, readline().split())) for _ in range(N)]

s = set()
for a, b in AB:
    s.add(a)
    s.add(a + b)
s = sorted(s)

t = {}
for i in range(len(s)):
    t[s[i]] = i
u = [0] * len(s)
for a, b in AB:
    u[t[a]] += 1
    u[t[a + b]] -= 1
u = list(accumulate(u))

D = [0] * (N + 1)
for i in range(len(s) - 1):
    D[u[i]] += s[i + 1] - s[i]
print(*D[1:])
