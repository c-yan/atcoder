m = 1000000007

H, W = map(int, input().split())
S = [input() for _ in range(H)]

au = [0] * W             # 上方向のアキュムレータ
aul = [0] * (H + W + 1)  # 左上方向のアキュムレータ
for h in range(H):
    al = 0               # 左方向のアキュムレータ
    for w in range(W):
        n = h - w + (W - 1)
        if h == 0 and w == 0:
            al = 1
            au[w] = 1
            aul[n] = 1
        elif S[h][w] == '#':
            al = 0
            au[w] = 0
            aul[n] = 0
        else:
            t = al + au[w] + aul[n]
            al += t
            al %= m
            au[w] += t
            au[w] %= m
            aul[n] += t
            aul[n] %= m
print(t % m)
