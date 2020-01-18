N, K, S = map(int, input().split())

result = [S % 10 ** 9 + 1] * N
for i in range(K):
    result[i] = S
print(*result)
