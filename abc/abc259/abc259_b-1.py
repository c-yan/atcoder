from math import hypot, atan2, radians, cos, sin

a, b, d = map(int, input().split())

r = hypot(a, b)
theta = atan2(b, a) + radians(d)
print(cos(theta) * r, sin(theta) * r)
