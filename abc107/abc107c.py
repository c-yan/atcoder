n, k = map(int, input().split())
x = list(map(int, input().split()))
p = n
for i in range(n):
  if x[i] > 0:
    p = i
    break
result = float('inf')
for i in range(k + 1):
  if p - i < 0 or p + k - i > n:
    continue
  if i == 0:
    result = min(result, x[p + k - 1])
  elif i == k:
    result = min(result, -x[p - k])
  else:
    l = x[p - i]
    r = x[p + (k - i) - 1]
    result = min(result, r - 2 * l, r * 2 - l)
print(result)
