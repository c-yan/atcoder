x1, y1, r = map(int, input().split())
x2, y2, x3, y3 = map(int, input().split())

if x2 <= x1 - r and x1 + r <= x3 and y2 <= y1 - r and y1 + r <= y3:
    print('NO')
else:
    print('YES')

if (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1) <= r * r and (x3 - x1) * (x3 - x1) + (y2 - y1) * (y2 - y1) <= r * r and (x2 - x1) * (x2 - x1) + (y3 - y1) * (y3 - y1) <= r * r and (x3 - x1) * (x3 - x1) + (y3 - y1) * (y3 - y1) <= r * r:
    print('NO')
else:
    print('YES')
