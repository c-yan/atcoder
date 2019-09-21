# メモ化再帰(貰う)
import sys
sys.setrecursionlimit(1000000)
n = int(input())
a = list(map(int, input().split()))
t = [-1] * n
def cost(i):
  if t[i] != -1:
    return t[i]
  if i == 0:
    result = 0
  elif i == 1:
    result = cost(i - 1) + abs(a[i] - a[i - 1])
  else:
    result = min(cost(i - 1) + abs(a[i] - a[i - 1]), cost(i - 2) + abs(a[i] - a[i - 2]))
  t[i] = result
  return result
print(cost(n - 1))
