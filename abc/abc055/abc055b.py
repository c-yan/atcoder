N = int(input())

result = 1
for i in range(1, N + 1):
    result *= i
    result %= 1000000007
print(result)
