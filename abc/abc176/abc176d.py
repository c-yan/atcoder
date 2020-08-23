from collections import deque


def main():
    from sys import stdin
    readline = stdin.readline

    from builtins import max, min, range

    INF = 10 ** 6

    H, W = map(int, readline().split())
    Ch, Cw = map(lambda x: int(x) - 1, readline().split())
    Dh, Dw = map(lambda x: int(x) - 1, readline().split())
    S = [readline()[:-1] for _ in range(H)]

    t = [[INF] * W for _ in range(H)]
    for h in range(H):
        th = t[h]
        Sh = S[h]
        for w in range(W):
            if Sh[w] == '#':
                th[w] = -1

    t[Ch][Cw] = 0
    q = deque([(Ch, Cw)])
    a = 0
    while q:
        warpq = []
        while q:
            h, w = q.popleft()
            warpq.append((h, w))
            if h - 1 >= 0 and t[h - 1][w] > a:
                q.append((h - 1, w))
                t[h - 1][w] = a
            if h + 1 < H and t[h + 1][w] > a:
                q.append((h + 1, w))
                t[h + 1][w] = a
            if w - 1 >= 0 and t[h][w - 1] > a:
                q.append((h, w - 1))
                t[h][w - 1] = a
            if w + 1 < W and t[h][w + 1] > a:
                q.append((h, w + 1))
                t[h][w + 1] = a

        if t[Dh][Dw] != INF:
            break

        a += 1
        for h, w in warpq:
            for i in range(max(0, h - 2), min(H, h + 3)):
                ti = t[i]
                for j in range(max(0, w - 2), min(W, w + 3)):
                    if ti[j] > a:
                        ti[j] = a
                        q.append((i, j))

    if t[Dh][Dw] == INF:
        print(-1)
    else:
        print(t[Dh][Dw])


main()
