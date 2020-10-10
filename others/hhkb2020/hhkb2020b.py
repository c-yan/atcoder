H, W = map(int, input().split())
S = [input() for _ in range(H)]

result = 0
for h in range(H):
    for w in range(W - 1):
        if S[h][w] == '.' and S[h][w + 1] == '.':
            result += 1
for h in range(H - 1):
    for w in range(W):
        if S[h][w] == '.' and S[h + 1][w] == '.':
            result += 1
print(result)
