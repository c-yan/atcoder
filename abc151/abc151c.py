N, M = map(int, input().split())

ac = [False] * N
wa = [0] * N
for _ in range(M):
    p, S = input().split()
    p = int(p) - 1
    if S == 'AC':
        ac[p] = True
    else:
        wa[p] += 1

a = 0
b = 0
for i in range(N):
    if ac[i]:
        a += 1
        b += wa[i]
print(*[a, b])
