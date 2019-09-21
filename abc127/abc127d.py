n, m = map(int, input().split())
a = list(map(int, input().split()))
bc = [list(map(int, input().split())) for _ in range(m)]
bc.sort(key = lambda x: x[1], reverse = True)
t = 0
for b, c in bc:
  a.extend([c] * b)
  t += b
  if t > n:
    break
a.sort(reverse = True)
print(sum(a[:n]))
