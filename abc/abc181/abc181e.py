from itertools import accumulate
from bisect import bisect_left
from collections import Counter

INF = float('inf')

N, M = map(int, input().split())
H = list(map(int, input().split()))
W = list(map(int, input().split()))

W.sort()

c = Counter(H)
h = sorted(k for k in c if c[k] % 2 == 1)
n = len(h)

l = list(accumulate(h[i + 1] - h[i] for i in range(0, n - 1, 2)))
r = list(accumulate(h[i] - h[i - 1] for i in range(n - 1, 0, -2)))

result = INF
for i in range(n):
    t = 0
    a = i // 2 - 1
    if a != -1:
        t += l[a]
    a = (n - 1 - i) // 2 - 1
    if a != -1:
        t += r[a]
    j = bisect_left(W, h[i])
    u = INF
    if j != M:
        u = min(u, W[j] - h[i])
    if j != 0:
        u = min(u, h[i] - W[j - 1])
    t += u
    if i % 2 == 1:
        t += h[i + 1] - h[i - 1]
    result = min(result, t)
print(result)
