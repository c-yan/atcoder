n = int(input())
p = [int(e) for e in input().split()]
result = 0
for i in range(1, n - 1):
  if p[i - 1] < p[i] < p[i + 1] or p[i + 1] < p[i] < p[i - 1]:
    result += 1
print(result)
