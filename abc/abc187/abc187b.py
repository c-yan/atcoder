N = int(input())
xy = [tuple(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(N):
    for j in range(i + 1, N):
        x1, y1 = xy[i]
        x2, y2 = xy[j]
        if x1 == x2:
            continue
        a = (y2 - y1) / (x2 - x1)
        if abs(a) <= 1:
            result += 1
print(result)
