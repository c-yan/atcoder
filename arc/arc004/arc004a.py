N = int(input())
xy = [tuple(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(N):
    for j in range(i + 1, N):
        x0, y0 = xy[i]
        x1, y1 = xy[j]
        result = max(result, ((x0 - x1) * (x0 - x1) + (y0 - y1) * (y0 - y1)) ** 0.5)
print(result)
