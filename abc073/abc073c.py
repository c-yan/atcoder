N = int(input())
d = {}
for _ in range(N):
  t = int(input())
  if t in d:
    d[t] += 1
  else:
    d[t] = 1
print(sum(i % 2 for i in d.values()))
