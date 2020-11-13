H, W = map(int, input().split())
S = [input() for _ in range(H)]


def is_black(h, w):
    for y in range(-1, 2):
        for x in range(-1, 2):
            if h + y < 0 or h + y >= H or w + x < 0 or w + x >= W:
                continue
            if S[h + y][w + x] == '#':
                continue
            return False
    return True


t = [[None] * W for _ in range(H)]
for h in range(H):
    for w in range(W):
        if is_black(h, w):
            t[h][w] = '#'
        else:
            t[h][w] = '.'

u = [['.'] * W for _ in range(H)]
for h in range(H):
    for w in range(W):
        if t[h][w] != '#':
            continue
        for y in range(-1, 2):
            for x in range(-1, 2):
                if h + y < 0 or h + y >= H or w + x < 0 or w + x >= W:
                    continue
                u[h + y][w + x] = '#'

for h in range(H):
    if S[h] == ''.join(u[h]):
        continue
    print('impossible')
    exit()

print('possible')
for h in range(H):
    print(*t[h], sep='')
