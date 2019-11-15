N, M = map(int, input().split())

b = [1] * N
b[0] = -1
for i in range(M):
    x, y = map(int, input().split())
    if b[x - 1] < 0:
        b[x - 1] += 1
        if b[y - 1] >= 0:
            b[y - 1] = -(b[y - 1] + 1)
        else:
            b[y - 1] -= 1
    else:
        b[x - 1] -= 1
        if b[y - 1] >= 0:
            b[y - 1] += 1
        else:
            b[y - 1] -= 1
print(len([x for x in b if x < 0]))
