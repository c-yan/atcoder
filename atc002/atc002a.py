from sys import exit, stdin

r, c = map(int, stdin.readline().split())
sy, sx = map(int, stdin.readline().split())
sy, sx = sy -1, sx -1
gy, gx =  map(int, stdin.readline().split())
gy, gx = gy - 1, gx - 1
maze = [stdin.readline()[:-1] for _ in range(r)]

distance = [[-1] * c for _ in range(r)]
distance[sy][sx] = 0
q = [(sy, sx)]
while True:
  y, x = q[0]
  q = q[1:]
  if y == gy and x == gx:
    print(distance[y][x])
    exit()
  if maze[y - 1][x] != '#' and distance[y - 1][x] == -1:
    distance[y - 1][x] = distance[y][x] + 1
    q.append((y - 1, x))
  if maze[y + 1][x] != '#' and distance[y + 1][x] == -1:
    distance[y + 1][x] = distance[y][x] + 1
    q.append((y + 1, x))
  if maze[y][x - 1] != '#' and distance[y][x - 1] == -1:
    distance[y][x - 1] = distance[y][x] + 1
    q.append((y, x - 1))
  if maze[y][x + 1] != '#' and distance[y][x + 1] == -1:
    distance[y][x + 1] = distance[y][x] + 1
    q.append((y, x + 1))
