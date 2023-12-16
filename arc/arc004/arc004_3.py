from math import gcd


def lcm(x, y):
    return x // gcd(x, y) * y


X, Y = map(int, input().split('/'))


def fmin(n):
    return (n * (n + 1) // 2 - n) / n


def solve(n):
    m = lcm(n, Y)
    a = n * (n + 1) // 2 * (m // n)
    b = X * (m // Y)
    c = a - b
    if c % (m // n) != 0:
        return None
    c //= (m // n)
    if 1 <= c <= n:
        return (n, c)
    else:
        return None


ok = 0
ng = 10 ** 18
while ng - ok > 1:
    m = ok + (ng - ok) // 2
    if X >= fmin(m) * Y:
        ok = m
    else:
        ng = m

result = []
for i in range(-1, 2):
    if ok + i <= 1:
        continue
    ret = solve(ok + i)
    if ret is not None:
        result.append(ret)
if len(result) == 0:
    print('Impossible')
else:
    for a in result:
        print(*a)
