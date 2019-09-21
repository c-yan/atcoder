from functools import reduce
n, m = map(int, input().split())
s = [[int(e) for e in input().split()[1:]] for _ in range(m)]
p = [int(e) for e in input().split()]
t = [reduce(lambda x, y: x | (1 << (y - 1)), e, 0) for e in s]
result = 0
for i in range(2 ** n):
  for j in range(m):
    if (bin(i & t[j]).count('1') & 1) != p[j]:
      break
  else:
    result += 1
print(result)
