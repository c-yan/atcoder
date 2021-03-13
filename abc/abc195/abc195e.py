from sys import setrecursionlimit
from functools import lru_cache


@lru_cache(maxsize=None)
def f(i, r):
    if i == N:
        return r == 0

    if X[i] == 'A':
        if not f(i + 1, r * 10 % 7):
            return False
        return f(i + 1, (r * 10 + int(S[i])) % 7)
    elif X[i] == 'T':
        if f(i + 1, r * 10 % 7):
            return True
        return f(i + 1, (r * 10 + int(S[i])) % 7)


setrecursionlimit(10 ** 6)

N = int(input())
S = input()
X = input()

if f(0, 0):
    print("Takahashi")
else:
    print("Aoki")
