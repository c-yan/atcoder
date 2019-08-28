n = int(input())
a = list(map(int, input().split()))
result = 0
for i in range(n):
  while True:
    if a[i] % 2 == 1:
      break
    a[i] //= 2
    result += 1
print(result)
