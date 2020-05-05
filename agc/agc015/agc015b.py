S = input()

result = 0
for i in range(len(S)):
  if S[i] == 'U':
    result += i * 2
    result += len(S) - (i + 1)
  else:
    result += i
    result += (len(S) - (i + 1)) * 2
print(result)
