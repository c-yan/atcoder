from collections import Counter

N, K, *c = map(int, open(0).read().split())

ct = Counter(c[:K])
t = len(ct)
result = t
for i in range(0, N - K):
    a = c[i]
    ct[a] -= 1
    if ct[a] == 0:
        t -= 1
    b = c[i + K]
    ct.setdefault(b, 0)
    if ct[b] == 0:
        t += 1
    ct[b] += 1
    result = max(result, t)
print(result)
