b = [list(map(int, input().split())) for _ in range(2)]
c = [list(map(int, input().split())) for _ in range(3)]


def calc_score(t):
    chokudai, chokuko = 0, 0
    for i in range(2):
        for j in range(3):
            if t[i * 3 + j] == t[(i + 1) * 3 + j]:
                chokudai += b[i][j]
            else:
                chokuko += b[i][j]
    for i in range(3):
        for j in range(2):
            if t[i * 3 + j] == t[i * 3 + (j + 1)]:
                chokudai += c[i][j]
            else:
                chokuko += c[i][j]
    return chokudai, chokuko


def f(turn, t):
    if t.count(-1) == 0:
        return calc_score()

    if turn == 0:
        chokudai, chokuko = -10 ** 18, 0
    elif turn == 1:
        chokudai, chokuko = 10 ** 18, 0

    for i in range(9):
        if t[i] != -1:
            continue
        t[i] = turn
        x, y = f(turn ^ 1, t)
        if turn == 0:
            if x - y > chokudai - chokuko:
                chokudai, chokuko = x, y
        elif turn == 1:
            if x - y < chokudai - chokuko:
                chokudai, chokuko = x, y
        t[i] = -1

    return chokudai, chokuko


chokudai, chokuko = f(0, [-1] * 9)
print(chokudai)
print(chokuko)
