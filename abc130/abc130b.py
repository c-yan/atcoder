n, x = map(int, input().split())
l = [int(e) for e in input().split()]
d = 0
result = 1
for i in range(len(l)):
  d += l[i]
  if d <= x:
    result += 1
  else:
    break
print(result)
