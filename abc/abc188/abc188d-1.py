from sys import stdin

readline = stdin .readline

N, C = map(int, readline().split())

d = {}
for _ in range(N):
    a, b, c = map(int, readline().split())
    d.setdefault(a, 0)
    d[a] += c
    d.setdefault(b + 1, 0)
    d[b + 1] -= c

skeys = sorted(d)
for i in range(1, len(skeys)):
    d[skeys[i]] += d[skeys[i - 1]]
for k in d:
    if d[k] > C:
        d[k] = C

result = 0
for i in range(len(skeys) - 1):
    result += d[skeys[i]] * (skeys[i + 1] - skeys[i])
print(result)
