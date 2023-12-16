m = 1000000007

N, *C = map(int, open(0).read().split())

C.sort()
result = 1
for i in range(N):
    result *= (C[i] - i)
    result %= m
print(result)
