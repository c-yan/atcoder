# DP(配るメモ化再帰)
from sys import setrecursionlimit


def cost(i):
    if t[i] != -1:
        return t[i]
    if i == N - 1:
        result = 0
    elif i == N - 2:
        result = abs(a[N - 2] - a[N - 1]) + cost(i)
    else:
        result = min(cost(i + 1) + abs(a[i + 1] - a[i]),
                     cost(i + 2) + abs(a[i + 2] - a[i]))
    t[i] = result
    return result


setrecursionlimit(1000000)

N = int(input())
a = list(map(int, input().split()))

t = [-1] * N
print(cost(0))
