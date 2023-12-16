N, K = map(int, input().split())

result = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        k = K - i - j
        if k < 1 or k > N:
            continue
        result += 1
print(result)
