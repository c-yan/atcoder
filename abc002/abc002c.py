xa, ya, xb, yb, xc, yc = map(int, input().split())

a, b, c, d = xb - xa, yb - ya, xc - xa, yc - ya
print(abs(a * d - b * c) / 2)
