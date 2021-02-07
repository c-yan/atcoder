from decimal import Decimal
from math import sqrt

m = 10000

X, Y, R = map(lambda x: int(Decimal(x) * m), input().split())


def is_inside_circle(x, y):
    return (x - X) * (x - X) + (y - Y) * (y - Y) <= R * R


result = 0
for y in range((Y - R) // m * m, (Y + R) // m * m + 1, m):
    a = 1
    b = -2 * X
    c = X * X + (y - Y) * (y - Y) - R * R
    d = b * b - 4 * a * c
    if d < 0:
        continue
    x0 = int((-b - sqrt(d)) / (2 * a)) // m * m
    x1 = int((-b + sqrt(d)) / (2 * a)) // m * m
    for x in range(x0 - m, x0 + m + 1, m):
        if not is_inside_circle(x, y):
            continue
        x0 = x
        break
    else:
        continue
    for x in range(x1 + m, x1 - m - 1, -m):
        if not is_inside_circle(x, y):
            continue
        x1 = x
        break
    else:
        continue
    result += (x1 - x0) // m + 1
print(result)
