n = int(input())
a = list(map(int, input().split()))
while True:
  a.sort()
  t = sum(a)
  for i in range(1, len(a)):
    if a[i] % a[0] == 0:
      a[i] = a[0]
    else:
      a[i] = a[i] % a[0]
  if sum(a) == t:
    break
print(a[0])
