H, W = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(H)]

result = []
y = 0
while y < H:
    x = 0
    while x < W:
        if a[y][x] % 2 == 1:
            if x == W - 1:
                if y == H - 1:
                    break
                else:
                    result.append('%d %d %d %d' % (y + 1, x + 1, y + 2, x + 1))
                    a[y + 1][x] += 1
            else:
                result.append('%d %d %d %d' % (y + 1, x + 1, y + 1, x + 2))
                a[y][x + 1] += 1
        x += 1
    if y == H - 1:
        break
    y += 1
    x = W - 1
    while x >= 0:
        if a[y][x] % 2 == 1:
            if x == 0:
                if y == H - 1:
                    break
                else:
                    result.append('%d %d %d %d' % (y + 1, x + 1, y + 2, x + 1))
                    a[y + 1][x] += 1
            else:
                result.append('%d %d %d %d' % (y + 1, x + 1, y + 1, x))
                a[y][x - 1] += 1
        x -= 1
    y += 1

print(len(result))
print('\n'.join(result))
