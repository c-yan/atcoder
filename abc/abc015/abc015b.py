N, *A = map(int, open(0).read().split())

B = [a for a in A if a != 0]
print((sum(B) + len(B) - 1) // len(B))
