N = int(input())
A = [input() for _ in range(N)]

for y in range(N):
    for x in range(N):
        if x == y:
            continue
        if A[y][x] == 'W' and A[x][y] != 'L':
            print('incorrect')
            exit()
        if A[y][x] == 'L' and A[x][y] != 'W':
            print('incorrect')
            exit()
        if A[y][x] == 'D' and A[x][y] != 'D':
            print('incorrect')
            exit()
print('correct')
