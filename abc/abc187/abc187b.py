N = int(input())
xy = [tuple(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(N):
    x1, y1 = xy[i]
    for j in range(i + 1, N):
        x2, y2 = xy[j]
        if abs((y2 - y1) / (x2 - x1)) <= 1:
            result += 1
print(result)
