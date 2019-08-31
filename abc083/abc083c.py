x, y = map(int, input().split())
result = 0
while x <= y:
  result += 1
  x *= 2
print(result)
