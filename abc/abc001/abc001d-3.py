from sys import stdin

readline = stdin.readline

N = int(readline())

t = [0] * (24 * 60 // 5 + 1)
for _ in range(N):
    S, E = readline()[:-1].split('-')
    h = int(S[:2])
    m = int(S[2:])
    m = m // 5 * 5
    a = (h * 60 + m) // 5
    h = int(E[:2])
    m = int(E[2:])
    m = (m + 4) // 5 * 5
    if m == 60:
        h += 1
        m = 0
    b = (h * 60 + m) // 5
    for i in range(a, b):
        t[i] = 1

s = -1
result = []
for i in range(24 * 60 // 5 + 1):
    if t[i] == 0 and s != -1:
        result.append('%02d%02d-%02d%02d' % (s * 5 // 60 , s * 5 % 60, i * 5 // 60, i * 5 % 60))
        s = -1
    elif t[i] != 0 and s == -1:
        s = i
print(*result, sep='\n')
