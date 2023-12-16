H, W = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(H)]

t = [[(0, 0)] * (W + 1) for _ in range(H + 1)]
for y in range(1, H + 1):
    for x in range(1, W + 1):
        b1, w1 = t[y - 1][x]
        b2, w2 = t[y][x - 1]
        b3, w3 = t[y - 1][x - 1]
        b, w = b1 + b2 - b3, w1 + w2 - w3
        if (y + x) % 2 == 0:
            b += C[y - 1][x - 1]
        else:
            w += C[y - 1][x - 1]
        t[y][x] = (b, w)

result = 0
for y1 in range(H + 1):
    for y2 in range(y1 + 1, H + 1):
        for x1 in range(W + 1):
            for x2 in range(x1 + 1, W + 1):
                b1, w1 = t[y2][x2]
                b2, w2 = t[y1][x2]
                b3, w3 = t[y2][x1]
                b4, w4 = t[y1][x1]
                b, w = b1 - b2 - b3 + b4, w1 - w2 - w3 + w4
                if b == w:
                    result = max(result, (y2 - y1) * (x2 - x1))
print(result)
