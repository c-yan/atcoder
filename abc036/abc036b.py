N = int(input())
s = [input() for _ in range(N)]

for y in range(N):
    for x in range(N):
        print(s[N - 1 - x][y], end='')
    print('')
