# imos 法
from operator import itemgetter

N, C = map(int, input().split())
stc = [list(map(int, input().split())) for _ in range(N)]
stc.sort(key=itemgetter(2, 0))

cs = [0] * (10 ** 5 + 1)
pt, pc = -1, -1
for s, t, c in stc:
    if pt == s and pc == c:
        cs[s] += 1
    else:
        cs[s - 1] += 1
    cs[t] -= 1
    pt, pc = t, c

for i in range(1, 10 ** 5 + 1):
    cs[i] += cs[i - 1]

print(max(cs))
