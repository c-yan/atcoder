N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

hands = [None] * N
d1 = {'r': 'p', 's': 'r', 'p': 's'}
d2 = {'r': P, 's': R, 'p': S}
result = 0
for i in range(len(T)):
    if i >= K and d1[T[i]] == hands[i - K]:
        if i + K < N:
            hands[i] = list(set('rps') - set(d1[T[i]]) - set(d1[T[i + K]]))[0]
        else:
            hands[i] = T[i]
    else:
        hands[i] = d1[T[i]]
        result += d2[T[i]]
print(result)
