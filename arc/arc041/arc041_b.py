N, M = map(int, input().split())
b = [list(map(int, input())) for _ in range(N)]

a = [[0] * M for _ in range(N)]
for y in range(N - 1):
    for x in range(M):
        t = b[y][x]
        if t == 0:
            continue
        a[y + 1][x] += t
        b[y + 1][x - 1] -= t
        b[y + 1][x + 1] -= t
        b[y + 2][x] -= t

for y in range(N):
    print(*a[y], sep='')
