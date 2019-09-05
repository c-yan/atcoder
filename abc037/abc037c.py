N, K = map(int, input().split())
a = list(map(int, input().split()))
t = sum(a[:K])
result = t
for i in range(1, N - K + 1):
  t += a[i + K - 1] - a[i - 1]
  result += t
print(result)
