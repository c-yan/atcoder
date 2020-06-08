N, M = map(int, input().split())
a = list(map(int, input().split()))

eater = [-1] * M
eater[0] = 1
t = [-1] * N
t[0] = a[0]
for i in range(1, M):
    ng = -1
    ok = N
    while abs(ng - ok) > 1:
        m = (ok + ng) // 2
        if a[i] > t[m]:
            ok = m
        else:
            ng = m
    if ok != N:
        t[ok] = a[i]
        eater[i] = ok + 1
print('\n'.join(str(i) for i in eater))
