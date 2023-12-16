# DP(貰うメモ化再帰)
from sys import setrecursionlimit


def cost(i):
    if t[i] != -1:
        return t[i]
    if i == 0:
        result = 0
    elif i == 1:
        result = cost(i - 1) + abs(a[i] - a[i - 1])
    else:
        result = min(cost(i - 1) + abs(a[i] - a[i - 1]),
                     cost(i - 2) + abs(a[i] - a[i - 2]))
    t[i] = result
    return result


setrecursionlimit(10 ** 6)

N = int(input())
a = list(map(int, input().split()))

t = [-1] * N
print(cost(N - 1))
