n, x = map(int, input().split())
a = [int(e) for e in input().split()]
a.sort()
result = 0
for i in a:
  x -= i
  if x < 0:
    break
  result += 1
if x != 0 and result == n:
  result -= 1
print(result)
