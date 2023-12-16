from math import ceil, sqrt

R, X, Y = map(int, input().split())

c = sqrt((X * X + Y * Y) / (R * R))
if c < 1:
    print(2)
else:
    print(ceil(c))
