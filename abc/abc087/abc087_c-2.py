# DP
N = int(input())
A = [list(map(int, input().split())) for _ in range(2)]

b = [[0] * N for _ in range(2)]
b[0][0] = A[0][0]
for i in range(1, N):
    b[0][i] = b[0][i - 1] + A[0][i]
b[1][0] = b[0][0] + A[1][0]
for i in range(1, N):
    b[1][i] = max(b[1][i - 1], b[0][i]) + A[1][i]
print(b[1][N - 1])
