# imos 法
from operator import itemgetter

N, C = map(int, input().split())
stc = [list(map(int, input().split())) for _ in range(N)]
stc.sort(key=itemgetter(2, 0))

cs = [0] * (10 ** 5 * 2 + 1)
pc = -1
for s, t, c in stc:
    if pc != c:
        pt = -1
        pc = c
    if pt == s:
        cs[s * 2] += 1
    else:
        cs[s * 2 - 1] += 1
    cs[t * 2] -= 1
    pt = t

for i in range(1, 10 ** 5 * 2 + 1):
    cs[i] += cs[i - 1]

print(max(cs))
