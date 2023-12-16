from functools import lru_cache

X, Y = map(int, input().split())


@lru_cache(maxsize=None)
def f(y):
    if X >= y:
        return abs(X - y)
    if y % 2 == 0:
        return min(abs(y - X), f(y // 2) + 1)
    else:
        return min(abs(y - X), f((y - 1) // 2) + 2, f((y + 1) // 2) + 2)


print(f(Y))
