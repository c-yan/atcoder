N, M, X = map(int, input().split())

C = []
A = []
for i in range(N):
    t = list(map(int, input().split()))
    C.append(t[0])
    A.append(t[1:])

result = -1
for i in range(1 << N):
    t = [0] * M
    c = 0
    for j in range(N):
        if (i >> j) & 1 == 0:
            continue
        c += C[j]
        for k in range(M):
            t[k] += A[j][k]
    if all(x >= X for x in t):
        if result == -1:
            result = c
        else:
            result = min(result, c)
print(result)
