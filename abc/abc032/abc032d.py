N, W = map(int, input().split())
vw = [tuple(map(int, input().split())) for _ in range(N)]


def solve1(N, W, vw):
    q = [(0, 0)]
    for v, w in vw[:N // 2]:
        nq = []
        while q:
            x, y = q.pop()
            nq.append((x, y))
            nq.append((x + w, y + v))
        q = nq
    q.sort()
    a = [q[0]]
    for w, v in q[1:]:
        if a[-1][0] == w:
            a[-1] = (w, v)
        elif v > a[-1][1]:
            a.append((w, v))

    q = [(0, 0)]
    for v, w in vw[N // 2:]:
        nq = []
        while q:
            x, y = q.pop()
            nq.append((x, y))
            nq.append((x + w, y + v))
        q = nq
    q.sort()
    b = [q[0]]
    for w, v in q[1:]:
        if b[-1][0] == w:
            b[-1] = (w, v)
        elif v > b[-1][1]:
            b.append((w, v))

    result = 0
    for w, v in a:
        if w > W:
            break
        ok = 0
        ng = len(b)
        while ng - ok > 1:
            m = ok + (ng - ok) // 2
            if w + b[m][0] <= W:
                ok = m
            else:
                ng = m
        result = max(result, v + b[ok][1])
    print(result)


def solve2(N, W, vw):
    max_w = min(sum(w for _, w in vw), W)
    dp = [-1] * (max_w + 1)
    dp[0] = 0
    for v, w in vw:
        for i in range(max_w - w, -1, -1):
            if dp[i] == -1:
                continue
            dp[i + w] = max(dp[i + w], dp[i] + v)
    print(max(dp))


def solve3(N, W, vw):
    max_v = sum(v for v, _ in vw)
    dp = [W + 1] * (max_v + 1)
    dp[0] = 0
    for v, w in vw:
        for i in range(max_v, -1, -1):
            if dp[i] > W:
                continue
            dp[i + v] = min(dp[i + v], dp[i] + w)
    for i in range(max_v, -1, -1):
        if dp[i] > W:
            continue
        print(i)
        break


if N <= 30:
    solve1(N, W, vw)
elif all(w <= 1000 for _, w in vw):
    solve2(N, W, vw)
elif all(v <= 1000 for v, _ in vw):
    solve3(N, W, vw)
