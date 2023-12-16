A, B, C, D = map(int, input().split())

INF = 10 ** 20

ok = INF
ng = 0
while ok - ng > 1:
    m = ng + (ok - ng) // 2
    if A + B * m <= C * m * D:
        ok = m
    else:
        ng = m

if ok == INF:
    print(-1)
else:
    print(ok)
