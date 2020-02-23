N, M = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(N)]
cd = [tuple(map(int, input().split())) for _ in range(M)]

for a, b in ab:
    best = float('inf')
    result = -1
    for i in range(M):
        c, d = cd[i]
        t = abs(a - c) + abs(b - d)
        if t < best:
            result = i + 1
            best = t
    print(result)
