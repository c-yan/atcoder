N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

result = 0
best = float('inf')
for i in range(N):
    t = T - H[i] * 0.006
    if abs(A - t) < best:
        best = abs(A - t)
        result = i + 1
print(result)
