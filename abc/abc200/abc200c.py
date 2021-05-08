N, *A = map(int, open(0).read().split())

d = {}
for a in A:
    t = a % 200
    d.setdefault(t, 0)
    d[t] += 1

result = 0
for k in d:
    result += d[k] * (d[k] - 1) // 2
print(result)
