n = int(input())
h = list(map(int, input().split()))
result = 0
while True:
  start = n
  for i in range(n):
    if h[i] != 0:
      start = i
      break
  if start == n:
    break
  end = n - 1
  count = 101
  for i in range(start, n):
    if h[i] == 0:
      end = i - 1
      break
    if h[i] < count:
      count = h[i]
  for i in range(start, end + 1):
    h[i] -= count
  result += count
print(result)
