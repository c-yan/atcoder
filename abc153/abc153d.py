from sys import setrecursionlimit

setrecursionlimit(1000000)

H = int(input())


def f(n):
    if n == 1:
        return 1
    else:
        return 1 + (n // 2) * 2


print(f(H))
