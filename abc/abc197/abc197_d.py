from math import sqrt, pi, atan2, cos, sin

N = int(input())
x0, y0 = map(int, input().split())
xN2, yN2 = map(int, input().split())

x, y = (x0 + xN2) / 2, (y0 + yN2) / 2
r = sqrt((x0 - x) * (x0 - x) + (y0 - y) * (y0 - y))

t = atan2(y0 - y, x0 - x) + (2 * pi) / N
x1 = cos(t) * r + x
y1 = sin(t) * r + y
print(x1, y1)
