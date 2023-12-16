N = int(input())
A = list(map(int, input().split()))

c = abs(0 - A[0])
for i in range(1, N):
    c += abs(A[i - 1] - A[i])
c += abs(A[N - 1] - 0)
print(c - abs(0 - A[0]) - abs(A[0] - A[1]) + abs(0 - A[1]))
for i in range(1, N - 1):
    print(c - abs(A[i - 1] - A[i]) -
          abs(A[i] - A[i + 1]) + abs(A[i - 1] - A[i + 1]))
print(c - abs(A[N - 2] - A[N - 1]) - abs(A[N - 1] - 0) + abs(A[N - 2] - 0))
