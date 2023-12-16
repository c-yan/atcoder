from sys import stdin

readlie = stdin.readline

N, M = map(int, readlie().split())

x = 0
y = N - 1
for _ in range(M):
    L, R = map(int, readlie().split())
    x = max(x, L - 1)
    y = min(y, R - 1)
print(max(y - x + 1, 0))
