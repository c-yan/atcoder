N, M = map(int, input().split())

x = 0
y = N - 1
for _ in range(M):
    L, R = map(int, input().split())
    x = max(x, L - 1)
    y = min(y, R - 1)
print(max(y - x + 1, 0))
