H, W, A, B = map(int, input().split())

placed = [[False] * W for _ in range(H)]


def proceed(p):
    y, x = p
    if x + 1 < W:
        return (y, x + 1)
    return (y + 1, 0)


def f(p, a, b):
    y, x = p

    if y == H:
        return a + b == 0

    if placed[y][x]:
        return f(proceed(p), a, b)

    result = 0
    if a >= 0:
        # right
        if x + 1 < W and not placed[y][x + 1]:
            placed[y][x] = True
            placed[y][x + 1] = True
            result += f(proceed(p), a - 1, b)
            placed[y][x + 1] = False
            placed[y][x] = False
        # down
        if y + 1 < H and not placed[y + 1][x]:
            placed[y][x] = True
            placed[y + 1][x] = True
            result += f(proceed(p), a - 1, b)
            placed[y + 1][x] = False
            placed[y][x] = False
    if b >= 0:
        placed[y][x] = True
        result += f(proceed(p), a, b - 1)
        placed[y][x] = False
    return result


print(f((0, 0), A, B))
