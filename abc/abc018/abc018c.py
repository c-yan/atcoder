from itertools import accumulate


def f(cy, cx, K, t):
    for y in range(cy - (K - 1), cy + K):
        l = cx - (K - 1) + abs(y - cy)
        r = cx + (K - 1) - abs(y - cy)
        if l == 0:
            if t[y][r] != 0:
                return False
        else:
            if t[y][r]-t[y][l-1] != 0:
                return False
    return True


R, C, K = map(int, input().split())
s = [input() for _ in range(R)]

t = [[0] * C for _ in range(R)]
for y in range(R):
    for x in range(C):
        if s[y][x] == 'x':
            t[y][x] = 1
    t[y] = list(accumulate(t[y]))

result = 0
for y in range(K - 1, R - (K - 1)):
    for x in range(K - 1, C - (K - 1)):
        if f(y, x, K, t):
            result += 1
print(result)
