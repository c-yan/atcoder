n, m = map(int, input().split())

a = 360 * (n % 12 + m / 60) / 12
b = 360 * m / 60
x = a - b
if x < 0:
    x += 360
y = b - a
if y < 0:
    y += 360
print(min(x, y))
