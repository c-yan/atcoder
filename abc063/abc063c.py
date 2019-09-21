from sys import exit
N = int(input())
s = [int(input()) for _ in range(N)]
result = sum(s)
if result % 10 != 0:
  print(result)
  exit()
t = [i for i in s if i % 10 != 0]
if len(t) == 0:
  print(0)
else:
  result -= min(t)
  print(result)
