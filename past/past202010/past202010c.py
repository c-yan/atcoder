N, M = map(int, input().split())
s = [input() for _ in range(N)]

result = ''
for y in range(N):
    for x in range(M):
        c = 0
        for dy in [-1, 0, 1]:
            ny = y + dy
            if ny < 0 or ny >= N:
                continue
            for dx in [-1, 0, 1]:
                nx = x + dx
                if nx < 0 or nx >= M:
                    continue
                if s[ny][nx] == '#':
                    c += 1
        result += str(c)
    result += '\n'
print(result)
