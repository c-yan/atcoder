N = int(input())

A = [None] * N
B = [None] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

result = 0
for i in range(N - 1, -1, -1):
    t = (A[i] + result) % B[i]
    if t != 0:
        result += B[i] - t
print(result)
