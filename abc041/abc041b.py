A, B, C = map(int, input().split())

result = A * B
result %= 1000000007
result *= C
result %= 1000000007
print(result)
