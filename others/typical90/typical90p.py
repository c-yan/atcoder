N, A, B, C = map(int, open(0).read().split())

A, B, C = sorted([A, B, C], reverse=True)

result = 10000
for i in range(N // A + 1):
    x = N - A * i
    for j in range(x // B + 1):
        y = x - B * j
        if y % C != 0:
            continue
        result = min(result, i + j + y // C)
print(result)
