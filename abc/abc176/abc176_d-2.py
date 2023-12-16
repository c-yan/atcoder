from sys import stdin
from collections import deque

readline = stdin.readline
INF = 10 ** 6

H, W = map(int, readline().split())
Ch, Cw = map(lambda x: int(x) - 1, readline().split())
Dh, Dw = map(lambda x: int(x) - 1, readline().split())
S = [readline()[:-1] for _ in range(H)]

t = [[INF] * W for _ in range(H)]
t[Ch][Cw] = 0

q = deque([(Ch, Cw)])
while q:
    h, w = q.popleft()
    for dh, dw in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nh, nw = h + dh, w + dw
        if nh < 0 or nh >= H or nw < 0 or nw >= W:
            continue
        if S[nh][nw] == '#':
            continue
        if t[nh][nw] > t[h][w]:
            t[nh][nw] = t[h][w]
            q.appendleft((nh, nw))

    for nh in range(max(0, h - 2), min(H, h + 3)):
        for nw in range(max(0, w - 2), min(W, w + 3)):
            if S[nh][nw] == '#':
                continue
            if t[nh][nw] > t[h][w] + 1:
                t[nh][nw] = t[h][w] + 1
                q.append((nh, nw))

if t[Dh][Dw] == INF:
    print(-1)
else:
    print(t[Dh][Dw])
