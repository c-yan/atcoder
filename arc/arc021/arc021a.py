A = [input().split() for _ in range(4)]

for i in range(4):
    for j in range(3):
        if A[i][j] == A[i][j + 1]:
            print('CONTINUE')
            exit()
        if A[j][i] == A[j + 1][i]:
            print('CONTINUE')
            exit()
print('GAMEOVER')
