N = int(input())
T = input()

d = 0
t = [(1, 0), (0, -1), (-1, 0), (0, 1)]
x, y = 0, 0
for c in T:
    if c == 'S':
        dx, dy = t[d]
        x += dx
        y += dy
    elif c == 'R':
        d += 1
        d %= 4
print(x, y)
