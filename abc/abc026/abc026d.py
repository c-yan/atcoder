from math import pi, sin

A, B, C = map(int, input().split())


def f(t):
    return A * t + B * sin(C * t * pi)


ok = 0
ng = (100 + B) / A + 1e-6
for _ in range(1000):
    m = (ok + ng) / 2
    if f(m) <= 100:
        ok = m
    else:
        ng = m
print(ok)
