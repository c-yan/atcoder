n = int(input())
a = [int(e) for e in input().split()]
v = 0
for i in range(n):
  v += 1 / a[i]
print(1 / v)
