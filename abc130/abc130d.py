n, k = [int(e) for e in input().split()]
data = [int(e) for e in input().split()]
result = 0
i = 0
j = 0
v = 0
while True:
  v += data[j]
  if v < k:
    j += 1
  else:
    result += len(data) - j
    v -= data[i]
    if j > i:
      v -= data[j]
    i += 1
    if j < i:
      j += 1
  if j == len(data):
    print(result)
    break
