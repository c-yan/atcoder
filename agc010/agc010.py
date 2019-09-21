N = int(input())
a = list(map(int, input().split()))
if sum(1 for i in a if i % 2 == 1) % 2 == 1:
  print('NO')
else:
  print('YES')
