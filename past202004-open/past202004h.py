N, M = map(int, input().split())
A = [input() for _ in range(N)]

d = {}
for i in range(N):
    for j in range(M):
        d.setdefault(A[i][j], [])
        d[A[i][j]].append((i, j))


for i in list(range(1, 10)) + ['S', 'G']:
    if str(i) not in d:
        print(-1)
        exit()

dp = [[float('inf')] * M for _ in range(N)]
i, j = d['S'][0]
dp[i][j] = 0

current = 'S'
while current != 'G':
    if current == 'S':
        next = '1'
    elif current == '9':
        next = 'G'
    else:
        next = str(int(current) + 1)
    for i, j in d[current]:
        for ni, nj in d[next]:
            dp[ni][nj] = min(dp[ni][nj], dp[i][j] + abs(ni - i) + abs(nj - j))
    current = next


i, j = d['G'][0]
print(dp[i][j])
