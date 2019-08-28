n = int(input())
h = [int(e) for e in input().split()]
m = -1
result = 0
for i in h:
  if i >= m:
    result += 1
    m = i
print(result)
