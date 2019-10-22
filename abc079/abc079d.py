# ワーシャルフロイド
def warshall_floyd(n, d):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                d[j][k] = min(d[j][k], d[j][i] + d[i][k])


H, W = map(int, input().split())

N = 10
d = [None] * N
for i in range(N):
    d[i] = list(map(int, input().split()))

warshall_floyd(N, d)

c = {i: 0 for i in range(N)}
for i in range(H):
    for j in map(int, input().split()):
        if j == -1:
            continue
        c[j] += 1

print(sum(c[i] * d[i][1] for i in range(N)))
