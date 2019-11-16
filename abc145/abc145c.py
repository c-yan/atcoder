from math import sqrt

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(N):
    for j in range(N):
        if i != j:
            result += sqrt((xy[i][0] - xy[j][0]) * (xy[i][0] - xy[j][0]) + (xy[i][1] - xy[j][1]) * (xy[i][1] - xy[j][1]))
print(result / N)
