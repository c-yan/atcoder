n, m = map(int, input().split())
x = 0
y = n - 1
for _ in range(m):
    l, r = map(int, input().split())
    x = max(x, l - 1)
    y = min(y, r - 1)
print(max(y - x + 1, 0))
