x, y, W = input().split()
x = int(x) - 1
y = int(y) - 1
c = [input() for _ in range(9)]

if W == 'R':
    dx = 1
    dy = 0
elif W == 'L':
    dx = -1
    dy = 0
elif W == 'U':
    dx = 0
    dy = -1
elif W == 'D':
    dx = 0
    dy = 1
elif W == 'RU':
    dx = 1
    dy = -1
elif W == 'RD':
    dx = 1
    dy = 1
elif W == 'LU':
    dx = -1
    dy = -1
elif W == 'LD':
    dx = -1
    dy = 1

result = ''
for i in range(4):
    result += c[y][x]
    if y + dy == -1:
        dy = 1
    if y + dy == 9:
        dy = -1
    if x + dx == -1:
        dx = 1
    if x + dx == 9:
        dx = -1
    x += dx
    y += dy
print(result)
