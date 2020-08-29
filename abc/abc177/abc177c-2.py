m = 1000000007

N, *A = map(int, open(0).read().split())

result = 0
a = 0
for i in range(1, N + 1):
    result += a * A[N - i]
    a += A[N - i]
    result %= m
print(result)
