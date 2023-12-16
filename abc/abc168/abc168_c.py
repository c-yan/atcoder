from math import pi, sin, cos, sqrt

A, B, H, M = map(int, input().split())

x1 = A * cos(2 * pi * (H + M / 60) / 12)
y1 = A * sin(2 * pi * (H + M / 60) / 12)
x2 = B * cos(2 * pi * M / 60)
y2 = B * sin(2 * pi * M / 60)

print(sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)))
