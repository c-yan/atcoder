N = int(input())
A = [None] * N
B = [None] * N
for i in range(N):
    a, b = map(int, input().split())
    A[i] = a
    B[i] = b

A.sort()
B.sort()

if N % 2 == 0:
    b = (B[N // 2] + B[(N - 1) // 2]) / 2
    a = (A[N // 2] + A[(N - 1) // 2]) / 2
    print(int((b - a) * 2 + 1))
else:
    print(B[N // 2] - A[N // 2] + 1)
