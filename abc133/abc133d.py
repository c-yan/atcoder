N = int(input())
A = list(map(int, input().split()))

t = [0] * N
t[0] = sum(A[::2]) - sum(A[1::2])
for i in range(1, N):
    t[i] = 2 * A[i - 1] - t[i - 1]
print(*list(map(str, t)))
