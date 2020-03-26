H, W = map(int, input().split())
A = [input() for _ in range(H)]

y, x = 0, 0
c = 0
while True:
    c += 1
    if y == H - 1 and x == W - 1:
        break
    if y < H - 1 and A[y + 1][x] == '#':
        y += 1
    elif x < W - 1 and A[y][x + 1] == '#':
        x += 1
    else:
        break

if c == sum(a.count('#') for a in A):
    print('Possible')
else:
    print('Impossible')
