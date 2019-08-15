h, w = map(int, input().split())
s = [input() + '#' for _ in range(h)]
s.append('#' * (w + 1))
t = [[-1] * w for _ in range(h + 1)]
tstart = [-1] * (w + 1)
for i in range(h + 1):
  ystart = -1
  for j in range(w + 1):
    if s[i][j] == '#':
      if ystart != -1:
        for k in range(ystart, j):
          t[i][k] += j - ystart
        ystart = -1
      if tstart[j] != -1:
        for k in range(tstart[j], i):
          t[k][j] += i - tstart[j]
        tstart[j] = -1
    else:
      if ystart == -1:
        ystart = j
      if tstart[j] == -1:
        tstart[j] = i
print(max(map(max, t)))
