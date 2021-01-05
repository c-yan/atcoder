N, H = map(int, input().split())
A, B, C, D, E = map(int, input().split())

a = 1 - (H - E * N)
result = 10 ** 20
for i in range(N):
    j = max((a - (B + E) * i + (D + E) - 1) // (D + E), 0)
    result = min(result, A * i + C * j)
print(result)
