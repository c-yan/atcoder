N, M, X, T, D = map(int, input().split())

print(T - (X - min(X, M)) * D)
