N, T = map(int, input().split())
X = 0
start = 0
stop = 0
for t in map(int, input().split()):
  if t > stop:
    X += stop - start
    start = t
  stop = t + T
X += stop - start
print(X)
