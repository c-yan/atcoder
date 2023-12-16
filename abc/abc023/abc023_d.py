from sys import stdin

readline = stdin.readline

N = int(readline())
HS = [tuple(map(int, readline().split())) for _ in range(N)]

def is_ok(m):
    t = sorted((m - h) // s for h, s in HS)
    for i in range(N):
        if t[i] < i:
            return False
    return True

ok = 10 ** 18
ng = -1
while ok - ng > 1:
    m = ng + (ok - ng) // 2
    if is_ok(m):
        ok = m
    else:
        ng = m
print(ok)
