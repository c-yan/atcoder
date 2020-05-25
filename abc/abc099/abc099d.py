from itertools import permutations

N, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(C)]
c = [list(map(int, input().split())) for _ in range(N)]

a = [[0] * C for _ in range(3)]
for y in range(N):
    for x in range(N):
        t = ((x + 1) + (y + 1)) % 3
        a[t][c[y][x] - 1] += 1

result = float('inf')
for b in permutations(range(C), 3):
    t = 0
    for i in range(3):
        for j in range(C):
            t += a[i][j] * D[j][b[i]]
    result = min(result, t)
print(result)
