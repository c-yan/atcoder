R, B = map(int, input().split())
x, y = map(int, input().split())


def is_ok(n):
    r = R - n
    if r < 0:
        return False
    b = B - n
    if b < 0:
        return False
    return r // (x - 1) + b // (y - 1) >= n


ok = 0
ng = 10 ** 18 + 1
while ng - ok > 1:
    m = (ok + ng) // 2
    if is_ok(m):
        ok = m
    else:
        ng = m
print(ok)
