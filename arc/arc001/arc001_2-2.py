# ワーシャルフロイド
def warshall_floyd(n, d):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                d[j][k] = min(d[j][k], d[j][i] + d[i][k])


A, B = map(int, input().split())

N = 41
d = [[float('inf')] * N for _ in range(N)]
for i in range(N):
    d[i][i] = 0

for i in range(N):
    for j in [1, 5, 10]:
        if 0 <= i + j <= 40:
            d[i][i + j] = 1
            d[i+j][i] = 1
        if 0 <= i - j <= 40:
            d[i][i - j] = 1
            d[i-j][i] = 1

warshall_floyd(N, d)

print(d[A][B])
