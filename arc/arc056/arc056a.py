A, B, K, L = map(int, input().split())

t = (K + L - 1) // L
print(min(A * K, B * t, B * (t - 1) + A * (K - L * (t - 1))))
