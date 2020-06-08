from collections import deque

INF = float('inf')

N, X, Y = map(int, input().split())

t = [['.'] * 403 for _ in range(403)]
for _ in range(N):
    x, y = map(int, input().split())
    t[y + 201][x + 201] = '#'

d = [[INF] * 403 for _ in range(403)]
d[0 + 201][0 + 201] = 0
q = deque([(0, 0)])
while q:
    y, x = q.popleft()
    i, j = y + 201, x + 201
    if i + 1 < 403 and j - 1 >= 0 and t[i + 1][j - 1] != '#' and d[i + 1][j - 1] > d[i][j] + 1:
        d[i + 1][j - 1] = d[i][j] + 1
        q.append((y + 1, x - 1))
    if i + 1 < 403 and j + 1 < 403 and t[i + 1][j + 1] != '#' and d[i + 1][j + 1] > d[i][j] + 1:
        d[i + 1][j + 1] = d[i][j] + 1
        q.append((y + 1, x + 1))
    if i - 1 >= 0 and t[i - 1][j] != '#' and d[i - 1][j] > d[i][j] + 1:
        d[i - 1][j] = d[i][j] + 1
        q.append((y - 1, x))
    if i + 1 < 403 and t[i + 1][j] != '#' and d[i + 1][j] > d[i][j] + 1:
        d[i + 1][j] = d[i][j] + 1
        q.append((y + 1, x))
    if j - 1 >= 0 and t[i][j - 1] != '#' and d[i][j - 1] > d[i][j] + 1:
        d[i][j - 1] = d[i][j] + 1
        q.append((y, x - 1))
    if j + 1 < 403 and t[i][j + 1] != '#' and d[i][j + 1] > d[i][j] + 1:
        d[i][j + 1] = d[i][j] + 1
        q.append((y, x + 1))
if d[Y + 201][X + 201] == INF:
    print(-1)
else:
    print(d[Y + 201][X + 201])
