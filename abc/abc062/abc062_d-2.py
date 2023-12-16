from heapq import heapify, heappop, heappush

N, *a = map(int, open(0).read().split())

q = a[:N]
heapify(q)
b = [0] * (N + 1)
b[0] = sum(q)
for i in range(N):
    x = q[0]
    y = max(heappop(q), a[N + i])
    heappush(q, y)
    b[i + 1] = b[i] - x + y

q = [-x for x in a[2 * N:]]
heapify(q)
c = [0] * (N + 1)
c[N] = -sum(q)
for i in range(N):
    x = -q[0]
    y = min(-heappop(q), a[2 * N - 1 - i])
    heappush(q, -y)
    c[N - i - 1] = c[N - i] - x + y

print(max(b[i] - c[i] for i in range(N + 1)))
