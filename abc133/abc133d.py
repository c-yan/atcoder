n = int(input())
a = [int(e) for e in input().split()]
result = [sum(a[::2])-sum(a[1::2])]
for i in range(len(a) - 1):
  result.append(2*a[i]-result[i])
print(' '.join(map(str, result)))
