a, b = map(int, input().split())
result = 0
if a  > b:
  result += a
  a -= 1
else:
  result += b
  b -= 1
if a  > b:
  result += a
else:
  result += b
print(result)
