N = int(input())
a = list(map(int, input().split()))
result = 0
i = 0
while i < N:
  j = i + 1
  while j < N:
    if a[j - 1] >= a[j]:
      break
    j += 1
  t = j - i
  result += t * (t + 1) // 2
  i = j
print(result)
