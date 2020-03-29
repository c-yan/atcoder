N = int(input())
A = list(map(int, input().split()))

result = [0] * N
result[0] = sum(A[::2]) - sum(A[1::2])
for i in range(1, N):
    result[i] = 2 * A[i - 1] - result[i - 1]
print(*result)
