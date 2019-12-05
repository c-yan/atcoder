N = int(input())
S = input()

result = 0
for i in range(10):
  a = S.find(str(i))
  if a == -1:
    continue
  for j in range(10):
    b = S.find(str(j), a + 1)
    if b == -1:
      continue
    for k in range(10):
      if S.find(str(k), b + 1) != -1:
        result += 1
print(result)
