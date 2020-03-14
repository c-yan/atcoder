N, Q = map(int, input().split())

t = [['N'] * N for _ in range(N)]
for _ in range(Q):
    S = input()
    if S[0] == '1':
        _, a, b = map(int, S.split())
        t[a - 1][b - 1] = 'Y'
    elif S[0] == '2':
        _, a = map(int, S.split())
        for i in range(N):
            if t[i][a - 1] == 'Y':
                t[a - 1][i] = 'Y'
    elif S[0] == '3':
        _, a = map(int, S.split())
        for i in [i for i in range(N) if t[a - 1][i] == 'Y']:
            for j in range(N):
                if t[i][j] == 'Y' and j != a - 1:
                    t[a - 1][j] = 'Y'

for i in range(N):
    print(''.join(t[i]))
