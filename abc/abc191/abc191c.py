H, W = map(int, input().split())
S = [input() for _ in range(H)]

result = 0
for y in range(H - 1):
    for x in range(W - 1):
        t = 0
        if S[y][x] == '#':
            t += 1
        if S[y][x + 1] == '#':
            t += 1
        if S[y + 1][x] == '#':
            t += 1
        if S[y + 1][x + 1] == '#':
            t += 1
        if t == 1 or t == 3:
            result += 1
print(result)
