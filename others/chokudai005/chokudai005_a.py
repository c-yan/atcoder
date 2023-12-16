id, N, K = map(int, input().split())
S = [input() for _ in range(N)]

result = []
for n in range(1, K + 1):
    x = str(n)
    t = []
    for i in range(N):
        for j in range(N):
            if S[i][j] != x and (i == 0 or S[i][j] != S[i - 1][j]) and (j == 0 or S[i][j] != S[i][j - 1]):
                t.append('%d %d %s' % (i + 1, j + 1, x))
    result.append(t)

best = min(len(result[i]) for i in range(K))
for i in range(K):
    if len(result[i]) == best:
        best_index = i
        break

print(len(result[best_index]))
print(*result[best_index], sep='\n')
