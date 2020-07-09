L, R = map(int, input().split())
l = list(map(int, input().split()))
r = list(map(int, input().split()))

d1 = {}
for e in l:
    d1.setdefault(e, 0)
    d1[e] += 1

d2 = {}
for e in r:
    d2.setdefault(e, 0)
    d2[e] += 1

for k in d1:
    d2.setdefault(k, 0)

print(sum(min(d1[k], d2[k]) for k in d1))
