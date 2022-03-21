from sys import stdin

readline = stdin.readline

def warshall_floyd(n, d):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                d[j][k] = min(d[j][k], d[j][i] + d[i][k])

INF = 10 ** 15

N, M = map(int, readline().split())
ABC = [tuple(map(int, readline().split())) for _ in range(M)]

d = [[INF] * (N + 1) for _ in range(N + 1)]
for k in range(N):
    d[k][k] = 0
for a, b, c in ABC:
    d[a][b] = c
    d[b][a] = c
warshall_floyd(N + 1, d)

result = 0
for a, b, c in ABC:
    for x in range(1, N + 1):
        if x in [a, b]:
            continue
        if c >= d[a][x] + d[x][b]:
            result += 1
            break
print(result)
