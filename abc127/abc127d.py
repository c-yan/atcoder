from functools import cmp_to_key
n, m = map(int, input().split())
a = [int(e) for e in input().split()]
bc = [[int(e) for e in input().split()] for _ in range(m)]
bc.sort(key = cmp_to_key(lambda x, y: y[1] - x[1]))
t = 0
for b, c in bc:
  a.extend([c] * b)
  t += b
  if t > n:
    break
a.sort(reverse = True)
print(sum(a[:n]))
