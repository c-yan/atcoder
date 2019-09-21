n = int(input())
result = 0
q = list('753')
while q:
  s = q.pop()
  if int(s) > n:
    continue
  if all(s.count(c) > 0 for c in '753'):
    result += 1
  q.extend([s + c for c in '753'])
print(result)
