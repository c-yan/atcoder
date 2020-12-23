from sys import stdin

readline = stdin.readline
m = 1000000007

H, W = map(int, readline().split())
S = [readline()[:-1] for _ in range(H)]

K = H * W
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            K -= 1

yoko = [[0] * W for _ in range(H)]
tate = [[0] * W for _ in range(H)]

for i in range(H):
    s = 0
    l = 0
    for j in range(W):
        if S[i][j] == '#':
            for k in range(s, j):
                yoko[i][k] = l
            s = j + 1
            l = 0
        elif S[i][j] == '.':
            l += 1
    for k in range(s, W):
        yoko[i][k] = l

for i in range(W):
    s = 0
    l = 0
    for j in range(H):
        if S[j][i] == '#':
            for k in range(s, j):
                tate[k][i] = l
            s = j + 1
            l = 0
        elif S[j][i] == '.':
            l += 1
    for k in range(s, H):
        tate[k][i] = l


t = [0] * (K + 1)
t[0] = 1
for i in range(1, K + 1):
    t[i] = t[i-1] * 2
    t[i] %= m


c = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue
        c += t[K - tate[i][j] - yoko[i][j] + 1]
        c %= m

result = K * t[K] - c
result %= m
print(result)
