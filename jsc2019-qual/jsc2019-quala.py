m, d = map(int, input().split())
result = 0
for i in range(4, m + 1):
  for j in range(22, d + 1):
    d10 = j // 10
    d1 = j % 10
    if d1 >= 2 and d10 >= 2 and d1 * d10 == i:
      result += 1
print(result)
