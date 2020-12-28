N, X, *w = map(int, open(0).read().split())

w0 = w[:N //2]
w1 = w[N //2:]

d0 = {0: 1}
for x in w0:
    for k in sorted(d0.keys(), reverse=True):
        t = k + x
        if t > X:
            continue
        d0.setdefault(t, 0)
        d0[t] += d0[k]

d1 = {0: 1}
for x in w1:
    for k in sorted(d1.keys(), reverse=True):
        t = k + x
        if t > X:
            continue
        d1.setdefault(t, 0)
        d1[t] += d1[k]

result = 0
for k in d0:
    if X - k in d1:
        result += d0[k] * d1[X -k]
print(result)
