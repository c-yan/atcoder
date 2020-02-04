H, W = map(int, input().split())
N = int(input())
a = list(map(int, input().split()))

result = [[None] * W for _ in range(H)]
d = 1
x, y = 0, 0
for i in range(N):
    t = a[i]
    while t > 0:
        result[y][x] = i + 1
        x += d
        if x == -1 or x == W:
            x -= d
            d = -d
            y += 1
        t -= 1

for i in range(H):
    print(*result[i])
