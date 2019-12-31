N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

d = {'r': P, 's': R, 'p': S}
result = 0
wins = [False] * K
for i in range(len(T)):
    if not wins[i % K] or T[i] != T[i - K]:
        result += d[T[i]]
        wins[i % K] = True
    else:
        wins[i % K] = False
print(result)
