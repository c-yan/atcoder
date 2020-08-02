from math import ceil

N, K, *A = map(int, open(0).read().split())

def is_ok(n):
    t = 0
    for a in A:
        if a <= n:
            continue
        t += ceil(a / n) - 1
    return t <= K

ok = 1000000000
ng = 0.0000000001
while abs(ng - ok) > 1:
    m = (ok + ng) // 2
    if is_ok(m):
        ok = m
    else:
        ng = m

print(ceil(ok))
