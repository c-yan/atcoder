# 累積和
N, K = map(int, input().split())
a = list(map(int, input().split()))

cs = [0] * N
cs[0] = a[0]
for i in range(1, N):
    cs[i] = a[i] + cs[i - 1]

result = cs[K -1]
for i in range(1, N - (K - 1)):
    result += cs[i + K - 1] - cs[i - 1]
print(result)
