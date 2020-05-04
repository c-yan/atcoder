N = int(input())
S = [input() for _ in range(N)]

T = [list(l) for l in S]
for i in range(N - 2, -1, -1):
    for j in range(2 * N - 1):
        if T[i][j] == '.':
            continue
        if j - 1 >= 0:
            if T[i + 1][j - 1] == 'X':
                T[i][j] = 'X'
        if T[i + 1][j] == 'X':
            T[i][j] = 'X'
        if j + 1 < 2 * N - 1:
            if T[i + 1][j + 1] == 'X':
                T[i][j] = 'X'
for l in T:
    print(''.join(l))
