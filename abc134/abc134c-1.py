n = int(input())
a = [int(input()) for i in range(n)]
b = [i for i in a]
b.sort()
b.reverse()
b = b[:2]
for i in range(n):
  if a[i] != b[0]:
    print(b[0])
  else:
    print(b[1])
