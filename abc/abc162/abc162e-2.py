N, K = map(int, input().split())

MOD = 10 ** 9 + 7

c = [0] * (K + 1)
for i in range(K, 0, -1):
    t = pow(K // i, N, MOD)
    for j in range(2, K // i + 1):
        t -= c[i * j]
        t %= MOD
    c[i] = t

result = 0
for i in range(1, K + 1):
    result += c[K // i] * i
    result %= MOD
print(result)
