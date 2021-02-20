def g1(x):
    return int(''.join(sorted(str(x), reverse=True)))


def g2(x):
    return int(''.join(sorted(str(x))))


def f(x):
    return g1(x) - g2(x)


N, K = map(int, input().split())

a = N
for i in range(K):
    a = f(a)
print(a)
