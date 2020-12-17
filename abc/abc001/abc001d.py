from sys import stdin

readline = stdin.readline

N = int(readline())
SE = [readline()[:-1] for _ in range(N)]

SE.sort()

def f(s):
    S, E = s.split('-')
    h = int(S[:2])
    m = int(S[2:])
    m = m // 5 * 5
    S = '%02d%02d' % (h, m)
    h = int(E[:2])
    m = int(E[2:])
    m = (m + 4) // 5 * 5
    if m == 60:
        h += 1
        m = 0
    E = '%02d%02d' % (h, m)
    return S + '-' + E

result = []
for s in SE:
    s = f(s)
    if len(result) == 0 or result[-1][5:] < s[:4]:
        result.append(s)
        continue
    if result[-1][5:] < s[5:]:
        result[-1] = result[-1][:5] + s[5:]
print(*result, sep='\n')
