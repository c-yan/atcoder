N = int(input())
A = list(map(int, input().split()))

while True:
    A.sort()
    t = sum(A)
    for i in range(1, N):
        if A[i] % A[0] == 0:
            A[i] = A[0]
        else:
            A[i] = A[i] % A[0]
    if sum(A) == t:
        break
print(A[0])
