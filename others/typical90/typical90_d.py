H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

h = [sum(a) for a in A]
v = [sum(A[y][x] for y in range(H)) for x in range(W)]

B = [[0] * W for _ in range(H)]
for y in range(H):
    for x in range(W):
        B[y][x] = h[y] + v[x] - A[y][x]

for y in range(H):
    print(*B[y])
