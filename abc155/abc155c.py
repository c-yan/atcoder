N = int(input())

d = {}
for _ in range(N):
    S = input()
    if S in d:
        d[S] += 1
    else:
        d[S] = 1

m = max(d.values())
l = []
for k in d:
    v = d[k]
    if v != m:
        continue
    l.append(k)

for s in sorted(l):
    print(s)
