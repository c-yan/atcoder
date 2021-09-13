from heapq import heappop, heappush

N, K, *A = map(int, open(0).read().split())


def is_ok(n):
    result = 0
    for a in A:
        if a <= n:
            continue
        result += a - n
    return result <= K


ok = 10 ** 10
ng = 0
while ok - ng > 1:
    m = ng + (ok - ng) // 2
    if is_ok(m):
        ok = m
    else:
        ng = m

result = 0
n = 0
t = []
for a in A:
    if a <= ok:
        heappush(t, -a)
        continue
    heappush(t, -ok)
    result += a * (a + 1) // 2 - ok * (ok + 1) // 2
    n += a - ok
for _ in range(K - n):
    x = -heappop(t)
    if x < 0:
        break
    result += x
    heappush(t, -(x - 1))
print(result)
