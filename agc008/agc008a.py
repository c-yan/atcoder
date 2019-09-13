x, y = map(int, input().split())
if abs(y) > abs(x):
  result = abs(y) - abs(x)
  if x < 0:
    result += 1
  if y < 0:
    result += 1
if abs(y) < abs(x):
  result = abs(x) - abs(y)
  if x > 0:
    result += 1
  if y > 0:
    result += 1
if abs(y) == abs(x):
  result = 0
  if x != y:
    result += 1
print(result)
