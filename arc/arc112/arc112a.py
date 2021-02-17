from sys import stdin

readline = stdin.readline


def f(l, r):
    if r < 2 * l:
        return 0
    t = r - 2 * l + 1
    return t * (t + 1) // 2


T = int(readline())

result = []
for _ in range(T):
    L, R = map(int, readline().split())
    result.append(f(L, R))
print(*result, sep='\n')
