from itertools import combinations

N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]

result = 0
for i, j, k in combinations(range(N), 3):
    x0, y0 = XY[i]
    x1, y1 = XY[j]
    x2, y2 = XY[k]
    x1, x2 = x1 - x0, x2 - x0
    y1, y2 = y1 - y0, y2 - y0
    if x1 * y2 - x2 * y1 == 0:
        continue
    result += 1
print(result)
