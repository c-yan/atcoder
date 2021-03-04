N = int(input())
xyc = [tuple(map(int, input().split())) for _ in range(N)]


def intersect(x1, x2, x3, x4):
    if x1 > x3:
        x1, x2, x3, x4 = x3, x4, x1, x2
    if x3 > x2:
        return None, None
    return x3, min(x2, x4)


def is_ok(n):
    x1, x2 = -10 ** 19, 10 ** 19
    y1, y2 = -10 ** 19, 10 ** 19
    for x, y, c in xyc:
        x3, x4 = x - n / c, x + n / c
        x1, x2 = intersect(x1, x2, x3, x4)
        if x1 is None:
            return False
        y3, y4 = y - n / c, y + n / c
        y1, y2 = intersect(y1, y2, y3, y4)
        if y1 is None:
            return False
    return True


ok = 10 ** 19
ng = 0
for _ in range(100):
    m = (ok + ng) / 2
    if is_ok(m):
        ok = m
    else:
        ng = m
print(ok)
