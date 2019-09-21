n = int(input())
a = list(map(int, input().split()))
mc = 0
s = 0
m = float('inf')
for i in a:
  if i < 0:
    mc += 1
  s += abs(i)
  m = min(m, abs(i))
if mc % 2 == 0:
  print(s)
else:
  print(s -2 * m)
