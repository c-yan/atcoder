N, *A = map(int, open(0).read().split())

b = sorted(A)[-2]
print(A.index(b) + 1)
