def main():
    N, Ma, Mb = map(int, input().split())
    abc = [tuple(map(int, input().split())) for _ in range(N)]

    INF = 10 ** 20

    s0 = {(0, 0, 0)}
    for a, b, c in abc[:N // 2]:
        t = set()
        for x, y, z in s0:
            t.add((a + x, b + y, c + z))
        s0 |= t

    s1 = {(0, 0, 0)}
    for a, b, c in abc[N // 2:]:
        t = set()
        for x, y, z in s1:
            t.add((a + x, b + y, c + z))
        s1 |= t

    # a0 + a1 : b0 + b1 = Ma : Mb
    # -> Mb(a0 + a1) = Ma(b0 + b1)
    # -> Mb * a0 - Ma * b0 = Ma * b1 - Mb * a1

    s0.remove((0, 0, 0))
    d0 = {}
    for a, b, c in s0:
        t = Mb * a - Ma * b
        d0.setdefault(t, INF)
        d0[t] = min(d0[t], c)

    s1.remove((0, 0, 0))
    d1 = {}
    for a, b, c in s1:
        t = Ma * b - Mb * a
        d1.setdefault(t, INF)
        d1[t] = min(d1[t], c)

    result = INF
    if 0 in d0:
        result = min(result, d0[0])
    if 0 in d1:
        result = min(result, d1[0])
    for k in d0:
        if k not in d1:
            continue
        t = d0[k] + d1[k]
        if t == 0:
            continue
        result = min(result, t)
    if result == INF:
        print(-1)
    else:
        print(result)


main()
