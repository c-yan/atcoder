B, C = map(int, input().split())

if B == 0:
    minv = -(C // 2)
    maxv = (C - 1) // 2
    print(maxv - minv + 1)
    exit()

if C == 1:
    y = 0
else:
    y = (C - 2) // 2

if B > 0:
    ml = -B - (C - 1) // 2
    mr = -(B - (C - 1) // 2)
    pl = B - C // 2
    pr = B + y
elif B < 0:
    ml = B - C // 2
    mr = B + y
    pl = -(B + (C - 1) // 2)
    pr = -B + (C - 1) // 2

if pl <= mr:
    print(pr - ml + 1)
else:
    print((pr - pl + 1) + (mr - ml + 1))
