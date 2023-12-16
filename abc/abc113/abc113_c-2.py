from sys import stdin

readline = stdin.readline

N, M = map(int, readline().split())
PY = [tuple(map(int, readline().split())) for _ in range(M)]

d = {}
for P, Y, i in sorted((PY[i][0], PY[i][1], i) for i in range(M)):
    d.setdefault(P, [])
    d[P].append(i)

result = [None] * M
for P in d:
    for x in range(len(d[P])):
        result[d[P][x]] = '%06d%06d' % (P, x + 1)
print(*result, sep='\n')
