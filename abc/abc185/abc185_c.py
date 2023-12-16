L = int(input())

result = 1
for i in range(11):
    result *= (L - 1) - i
for i in range(1, 12):
    result //= i
print(result)
