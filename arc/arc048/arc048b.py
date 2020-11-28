from sys import stdin
readline = stdin.readline

N = int(readline())
RH = [tuple(map(int, readline().split())) for _ in range(N)]

a = {}
b = {}
for r, h in RH:
    a.setdefault(r, 0)
    a[r] += 1
    b.setdefault(r, [0, 0, 0, 0])
    b[r][h] += 1

c = {}
t = 0
for k in sorted(a.keys(), reverse=True):
    c[k] = t
    t += a[k]

win = [0] * N
lose = [0] * N
draw = [0] * N
for i in range(N):
    r, h = RH[i]
    lose[i] = c[r]
    win[i] = N - c[r] - a[r]
    draw[i] = b[r][h] - 1
    if h == 1:
        win[i] += b[r][2]
        lose[i] += b[r][3]
    elif h == 2:
        win[i] += b[r][3]
        lose[i] += b[r][1]
    elif h == 3:
        win[i] += b[r][1]
        lose[i] += b[r][2]

print('\n'.join('%d %d %d' % (win[i], lose[i], draw[i]) for i in range(N)))
