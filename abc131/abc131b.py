N, L = map(int, input().split())

if L < 0 and N + L - 1 > 0:
    print(sum(range(L, N + L)))
else:
    if abs(L) > abs(N + L - 1):
        print(sum(range(L, N + L)) - (N + L - 1))
    else:
        print(sum(range(L, N + L)) - L)
