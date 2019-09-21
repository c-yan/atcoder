from sys import stdout

H, W = map(int, input().split())
a = [input() for _ in range(H)]

h = [all(c == '.' for c in a[i]) for i in range(H)]

w = [True] * W
for i in range(H):
  for j in range(W):
    w[j] = w[j] and a[i][j] == '.'

for i in range(H):
  if h[i]:
    continue
  for j in range(W):
    if w[j]:
      continue
    stdout.write(a[i][j])
  stdout.write('\n')
