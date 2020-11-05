N, K = map(int, open(0).read().split())

result = 0
for i in range(2, 2 * N + 1):
    j = i - K
    if j < 2 or j > 2 * N:
        continue
    result += min(i - 1, 2 * N - i + 1) * min(j - 1, 2 * N - j + 1)
print(result)
