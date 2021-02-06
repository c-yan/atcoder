N, X, *A = map(int, open(0).read().split())

print(*[a for a in A if a != X])
