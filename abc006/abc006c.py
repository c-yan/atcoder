N, M = map(int, input().split())
if M > 4 * N or M < 2 * N:
    print("-1 -1 -1")
    exit()
t = (M - 2 * N) // 2
a = N - t
c = t
t = M - 2 * a - 4 * c
a -= t
b = t
print(*[a, b, c])
