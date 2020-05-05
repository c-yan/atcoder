N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = 0
for i in range(N):
    if A[i] > B[i]:
        result += B[i]
        A[i] -= B[i]
        B[i] = 0
    else:
        result += A[i]
        B[i] -= A[i]
        A[i] = 0
        if A[i + 1] > B[i]:
            result += B[i]
            A[i + 1] -= B[i]
            B[i] = 0
        else:
            result += A[i + 1]
            B[i] -= A[i + 1]
            A[i + 1] = 0
print(result)
