from collections import deque

H, W = map(int, input().split())
c = [input() for _ in range(H)]

INF = 10 ** 12

for y in range(H):
    for x in range(W):
        if c[y][x] == 's':
            s = (y, x)
        if c[y][x] == 'g':
            g = (y, x)

t = [[INF] * W for _ in range(H)]
t[s[0]][s[1]] = 0
q = deque([s])
while q:
    y, x = q.popleft()
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny = y + dy
        nx = x + dx
        if ny < 0 or ny >= H or nx < 0 or nx >= W:
            continue
        if c[ny][nx] in 'sg.':
            if t[ny][nx] > t[y][x]:
                t[ny][nx] = t[y][x]
                q.appendleft((ny, nx))
        elif c[ny][nx] == '#':
            if t[ny][nx] > t[y][x] + 1:
                t[ny][nx] = t[y][x] + 1
                q.append((ny, nx))
if t[g[0]][g[1]] <= 2:
    print('YES')
else:
    print('NO')
