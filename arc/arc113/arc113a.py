K = int(input())

result = 0
for A in range(1, K + 1):
    for B in range(1, K + 1):
        if A * B > K:
            break
        result += K // (A * B)
print(result)
