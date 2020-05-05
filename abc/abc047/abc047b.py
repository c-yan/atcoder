W, H, N = map(int, input().split())

t = [[1] * W for _ in range(H)]
for _ in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        for h in range(H):
            for w in range(x):
                t[h][w] = 0
    elif a == 2:
        for h in range(H):
            for w in range(x, W):
                t[h][w] = 0
    elif a == 3:
        for h in range(y):
            for w in range(W):
                t[h][w] = 0
    elif a == 4:
        for h in range(y, H):
            for w in range(W):
                t[h][w] = 0
print(sum(sum(l) for l in t))
