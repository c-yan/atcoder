m = 1000000007

N, K = map(int, input().split())

c = [0] * (K + 1)
for i in range(K, 0, -1):
    t = pow(K // i, N, m)
    for j in range(2, K // i + 1):
        t -= c[i * j]
        t %= m
    c[i] = t

result = 0
for i in range(1, K + 1):
    result += c[i] * i
    result %= m
print(result)
