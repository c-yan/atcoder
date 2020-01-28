# 深さ優先探索
from sys import exit

H, W = map(int, input().split())
c = [input() for _ in range(H)]
for i in range(H):
    t = c[i].find('s')
    if t != -1:
        q = [(i, t)]
        break

queued = [[False] * W for _ in range(H)]
while q:
    i, j = q.pop()
    if c[i][j] == 'g':
        print('Yes')
        exit()
    if i > 0 and c[i - 1][j] != '#' and not queued[i - 1][j]:
        q.append((i - 1, j))
        queued[i - 1][j] = True
    if i < H - 1 and c[i + 1][j] != '#' and not queued[i + 1][j]:
        q.append((i + 1, j))
        queued[i + 1][j] = True
    if j > 0 and c[i][j - 1] != '#' and not queued[i][j - 1]:
        q.append((i, j - 1))
        queued[i][j - 1] = True
    if j < W - 1 and c[i][j + 1] != '#' and not queued[i][j + 1]:
        q.append((i, j + 1))
        queued[i][j + 1] = True

print('No')
