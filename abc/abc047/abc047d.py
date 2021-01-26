N, T, *A = map(int, open(0).read().split())

t = 10 ** 9 + 1
d = {}
for a in A:
    t = min(t, a)
    d.setdefault(a - t, 0)
    d[a - t] += 1
print(d[max(d)])
