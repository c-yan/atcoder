x1, y1, x2, y2 = map(int, input().split())

for dx, dy in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]:
    x3, y3 = x1 + dx, y1 + dy
    if (x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2) == 5:
        print('Yes')
        exit()
print('No')
