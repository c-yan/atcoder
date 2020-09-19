N = int(input())

result = 0
for A in range(1, N + 1):
    result += (N - 1) // A
print(result)
