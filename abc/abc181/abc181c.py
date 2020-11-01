N = int(input())
xy = [tuple(map(int, input().split())) for _ in range(N)]

for i in range(N - 1):
    xi, yi = xy[i]
    for j in range(i + 1, N):
        xj, yj = xy[j]
        for k in range(j + 1, N):
            x, y = xy[k]
            if xj == xi:
                if x == xi:
                    print('Yes')
                    exit()
            elif yj == yi:
                if y == yi:
                    print('Yes')
                    exit()
            elif abs(y - (yj - yi) / (xj - xi) * (x - xi) - yi) < 0.000001:
                print('Yes')
                exit()
print('No')
