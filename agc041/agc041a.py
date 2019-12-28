N, A, B = map(int, input().split())

t = float('inf')
if abs(A - B) % 2 == 0:
    t = min(abs(A - B) // 2, t)
t = min(B - 1, t)
t = min(N - A, t)
t = min((B - A - 1) // 2, t)
t = min((N - (A + (N - B + 1))) // 2, t)
print(t)
