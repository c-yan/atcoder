n = int(input())
result = 0
for i in range(1, n + 1):
  if len(str(i)) % 2 == 1:
    result += 1
print(result)
