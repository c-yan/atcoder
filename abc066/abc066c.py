n = int(input())
a = list(map(int, input().split()))
result = []
i = n - 1
while i >= 0:
  result.append(a[i])
  i -= 2
i += 1
if i < 0:
  i += 2
while i < n:
  result.append(a[i])
  i += 2
print(*result)
