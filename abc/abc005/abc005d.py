from sys import stdin

readline = stdin.readline

N = int(readline())
D = [list(map(int, readline().split())) for _ in range(N)]
Q = int(readline())

t = [[0] * (N + 1) for _ in range(N + 1)]
for y in range(1, N + 1):
    for x in range(1, N + 1):
        t[y][x] = t[y - 1][x] + t[y][x - 1] - t[y - 1][x - 1] + D[y - 1][x - 1]

u = [0] * (N * N + 1)
for y1 in range(N + 1):
    for y2 in range(y1 + 1, N + 1):
        for x1 in range(N + 1):
            for x2 in range(x1 + 1, N + 1):
                u[(y2 - y1) * (x2 - x1)] = max(u[(y2 - y1) * (x2 - x1)], t[y2][x2] - t[y1][x2] - t[y2][x1] + t[y1][x1])
for i in range(1, N * N + 1):
    u[i] = max(u[i], u[i - 1])

result = []
for _ in range(Q):
    P = int(readline())
    result.append(u[P])
print(*result, sep='\n')
