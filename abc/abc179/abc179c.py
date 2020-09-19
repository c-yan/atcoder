N = int(input())

result = 0
for A in range(1, N + 1):
    for B in range(1, (N // A) + 1):
        C = N - A * B
        if C == 0:
            continue
        result += 1
print(result)
