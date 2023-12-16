N, *a = map(int, open(0).read().split())

d = {}
for i, j in enumerate(sorted(set(a))):
    d[j] = i

for e in a:
    print(d[e])
