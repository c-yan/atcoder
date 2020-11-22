from collections import deque

INF = 10 ** 9

H, W = map(int, input().split())
a = [input() for _ in range(H)]

d = {}
for h in range(H):
    for w in range(W):
        c = a[h][w]
        if c in 'SG':
            d[c] = (h, w)
        elif c in '.#':
            continue
        else:
            if c in d:
                d[c].append((h, w))
            else:
                d[c] = [(h, w)]

not_warped = {}
for c in 'abcdefghijklmnopqrstuvwxyz':
    not_warped[c] = True


def move(h, w, p):
    c = a[h][w]
    if c == '#':
        return
    if t[h][w] > p:
        t[h][w] = p
        q.append((h, w))


t = [[INF] * W for _ in range(H)]
h, w = d['S']
t[h][w] = 0
q = deque([(h, w)])
while q:
    h, w = q.popleft()
    c = a[h][w]
    p = t[h][w] + 1
    if 'a' <= c <= 'z' and not_warped[c]:
        for nh, nw in d[c]:
            if t[nh][nw] > p:
                t[nh][nw] = p
                q.append((nh, nw))
        not_warped[c] = False
    if h != 0:
        move(h - 1, w, p)
    if h != H - 1:
        move(h + 1, w, p)
    if w != 0:
        move(h, w - 1, p)
    if w != W - 1:
        move(h, w + 1, p)

h, w = d['G']
if t[h][w] == INF:
    print(-1)
else:
    print(t[h][w])
