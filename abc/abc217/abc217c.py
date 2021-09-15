N, *p = map(int, open(0).read().split())

Q = [None] * N
for i in range(N):
    Q[p[i] - 1] = i + 1
print(*Q)
