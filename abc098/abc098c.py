n = int(input())
s = input()
was = [0] * n
if s[0] == 'W':
  was[0] = 1
for i in range(1, n):
  if s[i] == 'W':
    was[i] = was[i - 1] + 1
  else:
    was[i] = was[i - 1]
result = (n - 1) - (was[n - 1] - was[0])
for i in range(1, n):
  result = min(result, was[i - 1] + ((n - (i + 1)) - (was[n - 1] - was[i])))
print(result)
