from itertools import accumulate

m = 1000000007

N, *A = map(int, open(0).read().split())

result = 0
b = list(accumulate(A))
for i in range(N):
    result += A[i] * (b[N - 1] - b[i])
    result %= m
print(result)
