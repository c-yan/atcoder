A, B, N = map(int, input().split())

x = min(B - 1, N)
print(A * x // B - A * (x // B))
