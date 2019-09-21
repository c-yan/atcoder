n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]
used = [False] * n
a.sort(key = lambda x: x[0], reverse = True)
b.sort(key = lambda x: x[0], reverse = True)
result = 0
for i in range(n):
  pj = -1
  miny = float('inf')
  for j in range(n):
    if used[j]:
      continue
    if a[i][0] < b[j][0] and a[i][1] < b[j][1]:
      if b[j][1] < miny:
        pj = j
        miny = b[j][1]
  if pj != -1:
    used[pj] = True
    result += 1
print(result)
