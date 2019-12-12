N = int(input())
A = list(map(int, input().split()))

A.sort()
print(abs(A[-1] - A[0]))
