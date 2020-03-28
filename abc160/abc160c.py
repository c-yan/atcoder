K, N = map(int, input().split())
A = list(map(int, input().split()))

result = A[0] - A[N - 1] + K
for i in range(N - 1):
    result = max(result, A[i + 1] - A[i])
print(K - result)
