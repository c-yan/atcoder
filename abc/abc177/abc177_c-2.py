m = 1000000007

N, *A = map(int, open(0).read().split())

result = 0
c = 0
for i in range(1, N + 1):
    result += A[N - i] * c
    result %= m
    c += A[N - i]
    c %= m
print(result)
