N, *A = map(int, open(0).read().split())

i = A.index(max(A))
if i < 2 ** (N - 1):
    print(A.index(max(A[:2 ** (N - 1)]) + 1)
else:
    print(A.index(max(A[2 ** (N - 1):]) + 1)
