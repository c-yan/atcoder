from itertools import combinations

N = int(input())
ABCDE = [tuple(map(int, input().split())) for _ in range(N)]


def f(n, t):
    result = 0
    for i in range(5):
        if t[i] < n:
            continue
        result |= 1 << i
    return result


def is_ok(n):
    s = set()
    for i in range(N):
        s.add(f(n, ABCDE[i]))
    t = list(s)
    if len(t) == 1:
        return t[0] == 31
    elif len(t) == 2:
        return t[0] | t[1] == 31
    for c in combinations(t, 3):
        if c[0] | c[1] | c[2] != 31:
            continue
        return True
    else:
        return False


ok = 0
ng = 10 ** 9 + 1
while ng - ok > 1:
    m = ok + (ng - ok) // 2
    if is_ok(m):
        ok = m
    else:
        ng = m
print(ok)
