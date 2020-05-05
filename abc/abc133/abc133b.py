from math import ceil, sqrt

N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        t = sqrt(sum((X[i][k] - X[j][k]) * (X[i][k] - X[j][k])
                     for k in range(D)))
        if t == ceil(t):
            result += 1
print(result)
