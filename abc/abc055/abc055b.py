N = int(input())

m = 1000000007

result = 1
for i in range(1, N + 1):
    result *= i
    result %= m
print(result)
