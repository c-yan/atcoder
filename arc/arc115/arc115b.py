N = int(input())
C = [list(map(int, input().split())) for _ in range(N)]

INF = 10 ** 18

a = INF
i, j = 0, 0
for y in range(N):
    for x in range(N):
        if C[y][x] >= a:
            continue
        i, j = y, x
        a = C[y][x]


def f(z):
    A = [INF] * N
    B = [INF] * N
    A[i] = z
    for x in range(N):
        B[x] = C[i][x] - z
    for y in range(N):
        A[y] = C[y][0] - B[0]
    for y in range(N):
        for x in range(N):
            if C[y][x] != A[y] + B[x]:
                return None
    return A, B


for z in range(max(0, a // 2 - 10), min(a // 2 + 10, a + 1)):
    result = f(z)
    if result is None:
        continue
    print('Yes')
    print(*result[0])
    print(*result[1])
    break
else:
    print('No')
