# 幅優先探索
R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
c = [input() for _ in range(R)]

sy, sx, gy, gx = sy - 1, sx - 1, gy - 1, gx - 1
moves = [[-1] * C for _ in range(R)]
moves[sy][sx] = 0
q = [(sy, sx)]
while True:
    y, x = q.pop(0)
    if y == gy and x == gx:
        print(moves[y][x])
        break
    if c[y - 1][x] != '#' and moves[y - 1][x] == -1:
        moves[y - 1][x] = moves[y][x] + 1
        q.append((y - 1, x))
    if c[y + 1][x] != '#' and moves[y + 1][x] == -1:
        moves[y + 1][x] = moves[y][x] + 1
        q.append((y + 1, x))
    if c[y][x - 1] != '#' and moves[y][x - 1] == -1:
        moves[y][x - 1] = moves[y][x] + 1
        q.append((y, x - 1))
    if c[y][x + 1] != '#' and moves[y][x + 1] == -1:
        moves[y][x + 1] = moves[y][x] + 1
        q.append((y, x + 1))
