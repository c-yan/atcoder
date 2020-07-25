N = int(input())
A = list(map(int, input().split()))

t = [-1] * (N + 1)
t[0] = 1000
for i in range(N):
    t[i + 1] = max(t[i + 1], t[i])
    k = t[i] // A[i]
    y = t[i] % A[i]
    for j in range(i + 1, N):
        t[j + 1] = max(t[j + 1], k * A[j] + y)
print(t[N])
