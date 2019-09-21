n, k = map(int, input().split())
alist = list(map(int, input().split()))
d = {}
for a in alist:
  if a in d:
    d[a] += 1
  else:
    d[a] = 1
print(sum(list(sorted(d[k] for k in d))[:-k]))
