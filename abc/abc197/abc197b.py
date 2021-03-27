H, W, X, Y = map(int, input().split())
S = [input() for _ in range(H)]

X, Y = X - 1, Y - 1

result = 0
x, y = Y, X
while y >= 0 and S[y][x] == '.':
    result += 1
    y -= 1
x, y = Y, X
while y < H and S[y][x] == '.':
    result += 1
    y += 1
x, y = Y, X
while x >= 0 and S[y][x] == '.':
    result += 1
    x -= 1
x, y = Y, X
while x < W and S[y][x] == '.':
    result += 1
    x += 1
result -= 3
print(result)
