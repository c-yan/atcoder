A, B, C = map(int, input().split())

m = 1000000007

result = A * B
result %= m
result *= C
result %= m
print(result)
