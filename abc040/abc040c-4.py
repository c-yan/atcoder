# メモ化再帰(配る)
import sys
sys.setrecursionlimit(1000000)
n = int(input())
a = list(map(int, input().split()))
t = [-1] * n
def cost(i):
  if t[i] != -1:
    return t[i]
  if i == n - 1:
    result = 0
  elif i == n - 2:
    result = abs(a[n - 2] - a[n - 1]) + cost(i)
  else:
    result = min(cost(i + 1) + abs(a[i + 1] - a[i]), cost(i + 2) + abs(a[i + 2] - a[i]))
  t[i] = result
  return result
print(cost(0))
