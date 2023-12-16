from sys import setrecursionlimit
from functools import lru_cache

setrecursionlimit(10 ** 6)

N, X, Y = map(int, input().split())

@lru_cache(maxsize=None)
def red(level, count):
    if level == 1:
        return 0
    return (red(level - 1, 1) + blue(level, X)) * count

@lru_cache(maxsize=None)
def blue(level, count):
    if level == 1:
        return count
    return (red(level - 1, 1) + blue(level - 1, Y)) * count

print(red(N, 1))
