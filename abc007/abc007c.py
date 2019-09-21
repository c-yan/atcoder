from sys import exit
R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
sy, sx, gy, gx = sy - 1, sx - 1, gy -1, gx - 1
c = [input() for _ in range(R)]
t = [[-1] * C for _ in range(R)]
t[sy][sx] = 0
q = [(sy, sx)]
while True:
  y, x = q.pop(0)
  if x == gx and y == gy:
    print(t[y][x])
    exit()
  for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    if c[y + dy][x + dx] != '#' and t[y + dy][x + dx] == -1:
      t[y + dy][x + dx] = t[y][x] + 1
      q.append((y + dy, x + dx))
