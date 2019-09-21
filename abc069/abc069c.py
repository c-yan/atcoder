N = int(input())
odd_count = 0
mo4_count = 0 # multiple of 4
for i in map(int, input().split()):
  if i % 2 == 1:
    odd_count += 1
  elif i % 4 == 0:
    mo4_count += 1
if odd_count - N % 2 <= mo4_count:
  print('Yes')
else:
  print('No')
