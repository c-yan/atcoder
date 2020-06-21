N, *A = map(int, open(0).read().split())

A.sort(reverse=True)
print(sum(A[::2]))
