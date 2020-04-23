n = int(input())

result = float('inf')
for i in range(1, int(n ** 0.5) + 1):
    j = n // i
    result = min(result, abs(i - j) + (n - i * j))
print(result)
