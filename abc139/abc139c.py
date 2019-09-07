n = int(input())
h = list(map(int, input().split()))
t = 0
result = 0
for i in range(n - 1):
  if h[i + 1] <= h[i]:
    t += 1
  else:
    result = max(t, result)
    t = 0
result = max(t, result)
print(result)
