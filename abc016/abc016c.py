def warshall_floyd(n, d):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                d[j][k] = min(d[j][k], d[j][i] + d[i][k])


N, M = map(int, input().split())

d = [[float('inf')] * N for _ in range(N)]
for i in range(N):
    d[i][i] = 0

for _ in range(M):
    A, B = map(int, input().split())
    d[A - 1][B - 1] = 1
    d[B - 1][A - 1] = 1

warshall_floyd(N, d)

for i in range(N):
    print(len([j for j in d[i] if j == 2]))
