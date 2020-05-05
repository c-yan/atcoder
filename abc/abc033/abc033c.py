S = input()

result = 0
for s in S.split('+'):
  if s.count('0') == 0:
    result += 1
print(result)
