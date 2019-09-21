from sys import exit
h, w = map(int, input().split())
s = [input() for _ in range(h)]
for i in range(h):
  for j in range(w):
    if s[i][j] == '.':
      continue
    if i > 0 and s[i - 1][j] == '#':
      continue
    if i < h - 1 and s[i + 1][j] == '#':
      continue
    if j > 0 and s[i][j - 1] == '#':
      continue
    if j < w - 1 and s[i][j + 1] == '#':
      continue
    print('No')
    exit()
print('Yes')
