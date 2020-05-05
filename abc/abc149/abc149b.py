A, B, K = map(int, input().split())

a = max(A - K, 0)
K -= A - a
b = max(B - K, 0)
print(*[a, b])
