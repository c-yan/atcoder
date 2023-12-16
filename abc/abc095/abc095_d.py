N, C = map(int, input().split())
x = [None] * N
v = [None] * N
for i in range(N):
    x[i], v[i] = map(int, input().split())

a0 = [None] * N
a = v[0] - x[0]
a0[0] = max(0, a)
for i in range(1, N):
    a += v[i] - (x[i] - x[i - 1])
    a0[i] = max(a, a0[i - 1])

a1 = [None] * N
a = v[N - 1] - (C - x[N - 1])
a1[0] = max(0, a)
for i in range(1, N):
    a += v[N - 1 - i] - ((C - x[N - 1 - i]) - (C - x[N - 1 - (i - 1)]))
    a1[i] = max(a, a1[i - 1])

result = max(a0[N - 1], a1[N - 1])
for i in range(N - 1):
    result = max(result, a0[i] - x[i] + a1[N - 1 - (i + 1)])
for i in range(N - 1):
    result = max(result, a1[i] - (C - x[N - 1 - i]) + a0[N - 1 - (i + 1)])
print(result)
