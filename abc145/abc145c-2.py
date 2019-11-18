from itertools import permutations
from math import sqrt

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

result = 0
d = 0
for p in permutations(xy):
    d += 1
    for i in range(N - 1):
        result += sqrt((p[i][0] - p[i + 1][0]) * (p[i][0] - p[i + 1][0]) + (p[i][1] - p[i + 1][1]) * (p[i][1] - p[i + 1][1]))
print(result / d)
