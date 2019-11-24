A, B, X = map(int, input().split())


def is_ok(N):
    return A * N + B * len(str(N)) <= X


ok = 0
ng = 10 ** 9 + 1
while ng - ok > 1:
    m = (ok + ng) // 2
    if is_ok(m):
        ok = m
    else:
        ng = m
print(ok)
