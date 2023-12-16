N, K, Q = map(int, input().split())
A = list(map(lambda x: int(x) - 1, input().split()))
L = list(map(lambda x: int(x) - 1, input().split()))

cells = [None] * N
for i in range(K):
    cells[A[i]] = i

for l in L:
    t = -1
    for j in range(N):
        if cells[j] is None:
            continue
        t += 1
        if t == l:
            break
    if j != N - 1 and cells[j + 1] is None:
        cells[j + 1] = cells[j]
        cells[j] = None

result = [-1] * K
for i in range(N):
    if cells[i] is None:
        continue
    result[cells[i]] = i + 1
print(*result)
