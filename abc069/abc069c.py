N = int(input())
oddCount = 0
mo4Count = 0
for i in map(int, input().split()):
  if i % 2 == 1:
    oddCount += 1
  elif i % 4 == 0:
    mo4Count += 1
if oddCount - N % 2 <= mo4Count:
  print('Yes')
else:
  print('No')
