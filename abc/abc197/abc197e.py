from sys import stdin

readline = stdin.readline

N = int(readline())

d = {}
for _ in range(N):
    X, C = map(int, readline().split())
    d.setdefault(C, [])
    d[C].append(X)

for k in d:
    d[k].sort()

q = {0: 0}
for k in sorted(d):
    balls = d[k]
    nq = {}
    for x in q:
        t = q[x]
        if x <= balls[0]:
            a, b = x, t
            b += balls[-1] - a
            a = balls[-1]
            nq.setdefault(a, 10 ** 18)
            nq[a] = min(nq[a], b)
        elif x >= balls[-1]:
            a, b = x, t
            b += a - balls[0]
            a = balls[0]
            nq.setdefault(a, 10 ** 18)
            nq[a] = min(nq[a], b)
        else:
            a, b = x, t
            b += balls[-1] - a
            a = balls[-1]
            b += a - balls[0]
            a = balls[0]
            nq.setdefault(a, 10 ** 18)
            nq[a] = min(nq[a], b)

            a, b = x, t
            b += a - balls[0]
            a = balls[0]
            b += balls[-1] - a
            a = balls[-1]
            nq.setdefault(a, 10 ** 18)
            nq[a] = min(nq[a], b)
    q = nq
print(min(abs(k) + q[k] for k in q))
