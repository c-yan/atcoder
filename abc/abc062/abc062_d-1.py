from collections import Counter
from heapq import heapify, heappop, heappush

N, *a = map(int, open(0).read().split())

q1 = a[:N]
heapify(q1)

b = a[N:]
b.sort()
q2 = b[N:]
heapify(q2)
c = Counter(q2)

t = sum(q1) - sum(b[:N])
result = t
for i in range(N):
    if a[N + i] > q1[0]:
        t -= heappop(q1)
        heappush(q1, a[N + i])
        t += a[N + i]
    if a[N + i] in c:
        c[a[N + i]] -= 1
        if c[a[N + i]] == 0:
            del c[a[N + i]]
    else:
        t += a[N + i]
        x = heappop(q2)
        while x not in c:
            x = heappop(q2)
        t -= x
        c[x] -= 1
        if c[x] == 0:
            del c[x]
    result = max(result, t)
print(result)
