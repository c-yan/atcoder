N, K = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(N)]

ab.sort()
t = 0
for a, b in ab:
    t += b
    if t >= K:
        print(a)
        break
