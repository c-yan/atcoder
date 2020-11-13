from collections import deque

A = [input() for _ in range(10)]


def fill(h, w, c):
    t[h][w] = c
    q = deque([(h, w)])
    while q:
        y, x = q.popleft()
        if y != 0 and A[y - 1][x] == 'o' and t[y - 1][x] is None:
            q.append((y - 1, x))
            t[y - 1][x] = c
        if y != 9 and A[y + 1][x] == 'o' and t[y + 1][x] is None:
            q.append((y + 1, x))
            t[y + 1][x] = c
        if x != 0 and A[y][x - 1] == 'o' and t[y][x - 1] is None:
            q.append((y, x - 1))
            t[y][x - 1] = c
        if x != 9 and A[y][x + 1] == 'o' and t[y][x + 1] is None:
            q.append((y, x + 1))
            t[y][x + 1] = c


t = [[None] * 10 for _ in range(10)]
c = 0
for h in range(10):
    for w in range(10):
        if A[h][w] == 'o' and t[h][w] is None:
            fill(h, w, c)
            c += 1

for h in range(10):
    for w in range(10):
        if A[h][w] == 'o':
            continue
        s = set()
        if h != 0 and t[h - 1][w] is not None:
            s.add(t[h - 1][w])
        if h != 9 and t[h + 1][w] is not None:
            s.add(t[h + 1][w])
        if w != 0 and t[h][w - 1] is not None:
            s.add(t[h][w - 1])
        if w != 9 and t[h][w + 1] is not None:
            s.add(t[h][w + 1])
        if len(s) == c:
            print('YES')
            exit()
print('NO')
