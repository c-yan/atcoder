N, *A = map(int, open(0).read().split())

print(sorted(enumerate(A), key=lambda x: x[1])[-2][0] + 1)
