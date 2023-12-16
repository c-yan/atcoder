N, K = map(int, input().split())

m = 1000000007

result = 0
for i in range(K, N + 2):
    # max: N, N -1, ..., N - i + 1
    a = (N + (N - i + 1)) * i // 2
    # min: 0, 1, .., i - 1
    b = (0 + (i - 1)) * i // 2
    result += a - b + 1
    result %= m
print(result)
