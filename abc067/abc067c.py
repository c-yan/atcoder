N = int(input())
a = list(map(int, input().split()))
t = [0] * N
t[0] = a[0]
for i in range(1, N):
  t[i] = t[i - 1] + a[i]
result = float('inf')
for i in range(0, N - 1):
  result = min(result, abs(t[i] - (t[N - 1] - t[i])))
print(result)
