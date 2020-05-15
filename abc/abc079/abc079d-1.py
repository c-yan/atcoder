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

result = 0
for _ in range(H):
    for i in map(int, input().split()):
        if i == -1:
            continue
        result += d[i][1]
print(result)
