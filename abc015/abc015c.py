N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]

t = [0] * N
for i in range(N ** K):
    x = 0
    for i in range(N):
        x ^= T[i][t[i]]
    if x == 0:
        print('Found')
        exit()
    for i in range(N):
        if t[i] != K - 1:
            t[i] += 1
            break
        t[i] = 0
print('Nothing')
