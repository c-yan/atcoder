INF = float('inf')


def f(H, W):
    return min(f1(H, W), f1(W, H))


def f1(H, W):
    result = INF
    for h in range(1, H):
        t = [h * W] + f2(H - h, W)
        t.sort()
        if abs(t[0] - t[2]) < result:
            result = abs(t[0] - t[2])
        t = [h * W] + f2(W, H - h)
        t.sort()
        if abs(t[0] - t[2]) < result:
            result = abs(t[0] - t[2])
    return result


def f2(H, W):
    if H < 2:
        return [-INF, INF]
    h = H // 2
    return [h * W, (H - h) * W]


H, W = map(int, input().split())

print(f(H, W))
