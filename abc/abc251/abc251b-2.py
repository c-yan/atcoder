N, W, *A = map(int, open(0).read().split())

t = A[:]

for x in range(N - 1):
    for y in range(x + 1, N):
        t.append(A[x] + A[y])

for x in range(N - 2):
    for y in range(x + 1, N - 1):
        for z in range(y + 1, N):
            t.append(A[x] + A[y] + A[z])

print(len(set(x for x in t if x <= W)))
