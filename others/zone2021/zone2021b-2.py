N, D, H = map(int, input().split())
dh = [tuple(map(int, input().split())) for _ in range(N)]


def is_ok(n):
    for d, h in dh:
        if (H - n) / D * d + n >= h:
            continue
        return False
    else:
        return True


ng = 0
ok = 10 ** 3
for _ in range(10000):
    m = (ok + ng) / 2
    if is_ok(m):
        ok = m
    else:
        ng = m
print(ok)
