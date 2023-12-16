from functools import lru_cache

N = int(input())


def print_pascal(d):
    for i in range(d):
        t = []
        for j in range(i + 1):
            t.append(choice(i, j))
        print(*t)


@lru_cache(maxsize=None)
def choice(n, r):
    if r < 0 or r > n:
        return 0
    elif r == 0:
        return 1
    else:
        return choice(n - 1, r - 1) + choice(n - 1, r)


print_pascal(N)
