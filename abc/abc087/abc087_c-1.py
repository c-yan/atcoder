# 累積和
N = int(input())
A = [list(map(int, input().split())) for _ in range(2)]

b = [[0] * N for _ in range(2)]
b[0][0] = A[0][0]
for i in range(1, N):
    b[0][i] = b[0][i - 1] + A[0][i]
b[1][N - 1] = A[1][N - 1]
for i in range(1, N):
    b[1][N - 1 - i] = b[1][N - i] + A[1][N - 1 - i]

print(max(b[0][i] + b[1][i] for i in range(N)))
