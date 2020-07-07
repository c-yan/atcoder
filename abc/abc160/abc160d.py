N, X, Y = map(int, input().split())

result = [0] * (N - 1)
for i in range(1, N):
    for j in range(i + 1, N + 1):
        result[min(j - i, abs(X - i) + 1 + abs(Y - j)) - 1] += 1
print(*result, sep='\n')
