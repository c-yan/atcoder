N, H = map(int, input().split())
A, B, C, D, E = map(int, input().split())

result = 10 ** 20
for i in range(N):
    ok = N - i
    ng = -1
    while ok - ng > 1:
        m = ng + (ok - ng) // 2
        if H - E * (N - i - m) + B * i + D * m > 0:
            ok = m
        else:
            ng = m
    result = min(result, A * i + C * ok)
print(result)
