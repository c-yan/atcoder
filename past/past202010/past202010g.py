N, M = map(int, input().split())
S = [input() for _ in range(N)]


def f(y, x):
    s = [list(l) for l in S]
    s[y][x] = '.'
    t = [[False] * M for _ in range(N)]
    q = [(y, x)]
    while q:
        u, v = q.pop()
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = u + dy, v + dx
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if s[ny][nx] == '#':
                continue
            if not t[ny][nx]:
                t[ny][nx] = True
                q.append((ny, nx))
    for y in range(N):
        for x in range(M):
            if s[y][x] == '#' or t[y][x]:
                continue
            return False
    return True


result = 0
for y in range(N):
    for x in range(M):
        if S[y][x] == '.':
            continue
        if f(y, x):
            result += 1
print(result)
