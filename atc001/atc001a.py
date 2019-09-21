from sys import exit, stdin
from collections import deque

h, w = map(int, stdin.readline().split())
q = None
data = [None] * h
for i in range(h):
    data[i] = stdin.readline()[:-1]
    if q is None:
        t = data[i].find('s')
        if t != -1:
            q = deque([(i, t)])

never = [[True] * w for _ in range(h)]
while len(q) != 0:
    i, j = q.popleft()
    if data[i][j] == 'g':
        print('Yes')
        exit()
    never[i][j] = False
    if i > 0 and data[i - 1][j] != '#' and never[i - 1][j]:
        q.append((i - 1, j))
    if i < h - 1 and data[i + 1][j] != '#' and never[i + 1][j]:
        q.append((i + 1, j))
    if j > 0 and data[i][j - 1] != '#' and never[i][j - 1]:
        q.append((i, j - 1))
    if j < w - 1 and data[i][j + 1] != '#' and never[i][j + 1]:
        q.append((i, j + 1))

print('No')
