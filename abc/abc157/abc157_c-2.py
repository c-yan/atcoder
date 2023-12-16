N, M = map(int, input().split())
sc = [tuple(map(int, input().split())) for _ in range(M)]

for i in range(1000):
    t = str(i)
    if len(t) != N:
        continue
    ok = True
    for s, c in sc:
        if int(t[s - 1]) != c:
            ok = False
            break
    if ok:
        print(i)
        exit()
print(-1)
