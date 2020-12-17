from sys import stdin
from itertools import accumulate

readline = stdin.readline

N = int(readline())

t = [0] * 24 * 60 + 1
for _ in range(N):
    S, E = readline()[:-1].split('-')
    h = int(S[:2])
    m = int(S[2:])
    m = m // 5 * 5
    t[h * 60 + m] += 1
    h = int(E[:2])
    m = int(E[2:])
    m = (m + 4) // 5 * 5
    if m == 60:
        h += 1
        m = 0
    t[h * 60 + m] -= 1

t = list(accumulate(t))
s = -1
result = []
for i in range(24 * 60 + 1):
    if t[i] == 0 and s != -1:
        result.append('%02d%02d-%02d%02d' % (s // 60, s % 60, i // 60, i % 60))
    elif t[i] != 0 and s == -1:
        s = i
print(*result, sep='\n')
