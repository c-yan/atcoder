n = int(input())
v = [int(e) for e in input().split()]
c = [int(e) for e in input().split()]
result = 0
for i in range(n):
  if v[i] > c[i]:
    result += v[i] - c[i]
print(result)
