from bisect import bisect_left

N, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


def is_ok(n):
    t = 0
    for x in a:
        t += bisect_left(b, n // x + 1)
    return t < K


b.sort()
ok = 0
ng = 10 ** 18
while ng - ok > 1:
    m = ok + (ng - ok) // 2
    if is_ok(m):
        ok = m
    else:
        ng = m
print(ok + 1)
