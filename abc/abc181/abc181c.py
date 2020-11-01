N = int(input())
xy = [tuple(map(int, input().split())) for _ in range(N)]

for i in range(2, N):
    xi, yi = xy[i]
    for j in range(1, i):
        xj, yj = xy[j]
        for k in range(j):
            x, y = xy[k]
            if y * (xj - xi) == (yj - yi) * (x - xi) + yi * (xj - xi):
                print('Yes')
                exit()
print('No')
