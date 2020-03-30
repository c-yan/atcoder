N, X, Y = map(int, input().split())

t = [0] * (N - 1)
for i in range(1, N):
    for j in range(i + 1, N + 1):
        t[min(j - i, abs(X - i) + 1 + abs(Y - j)) - 1] += 1
print('\n'.join(map(str, t)))
