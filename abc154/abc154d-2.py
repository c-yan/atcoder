# 累積和
N, K = map(int, input().split())
p = list(map(int, input().split()))

m = [(e + 1) / 2 for e in p]
for i in range(1, N):
    m[i] += m[i - 1]

result = 0
for i in range(N - K):
    t = m[K - 1 + i] - m[i]
    if t > result:
        result = t
print(result)
