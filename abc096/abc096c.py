from sys import exit

H, W = map(int, input().split())
s = [input() for _ in range(H)]

for i in range(H):
    for j in range(W):
        if s[i][j] == '.':
            continue
        if i > 0 and s[i - 1][j] == '#':
            continue
        if i < H - 1 and s[i + 1][j] == '#':
            continue
        if j > 0 and s[i][j - 1] == '#':
            continue
        if j < W - 1 and s[i][j + 1] == '#':
            continue
        print('No')
        exit()
print('Yes')
