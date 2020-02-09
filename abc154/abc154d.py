N, K = map(int, input().split())
p = list(map(int, input().split()))

m = [(e + 1) / 2 for e in p]

t = sum(m[0:K])
result = t
for i in range(N - K):
    t -= m[i]
    t += m[i + K]
    if t > result:
        result = t
print(result)
