H, W, A, B = map(int, input().split())

t = [[False] * W for _ in range(H)]


def g(y, x):
    if x + 1 < W:
        return y, x + 1
    return y + 1, 0


def f(y, x, a, b):
    if y == H:
        return a + b == 0

    if t[y][x]:
        ny, nx = g(y, x)
        return f(ny, nx, a, b)

    result = 0
    if a >= 0:
        if x + 1 < W and not t[y][x + 1]:
            t[y][x] = True
            t[y][x + 1] = True
            ny, nx = g(y, x)
            result += f(ny, nx, a - 1, b)
            t[y][x + 1] = False
            t[y][x] = False
        if y + 1 < H and not t[y + 1][x]:
            t[y][x] = True
            t[y + 1][x] = True
            ny, nx = g(y, x)
            result += f(ny, nx, a - 1, b)
            t[y + 1][x] = False
            t[y][x] = False
    if b >= 0:
        t[y][x] = True
        ny, nx = g(y, x)
        result += f(ny, nx, a, b - 1)
        t[y][x] = False
    return result


print(f(0, 0, A, B))
