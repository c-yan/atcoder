from sys import stdin

readline = stdin.readline

N, D, K = map(int, readline().split())
LR = [tuple(map(lambda x: int(x) - 1, readline().split())) for _ in range(D)]

goals = [None] * K
currents = [None] * K
for i in range(K):
    s, t = map(lambda x: int(x) - 1, readline().split())
    goals[i] = t
    currents[i] = s

result = [None] * K
for i in range(1, D + 1):
    l, r = LR[i - 1]
    for j in range(K):
        if currents[j] == goals[j]:
            continue
        if currents[j] < l or currents[j] > r:
            continue
        if l <= goals[j] <= r:
            result[j] = i
            currents[j] = goals[j]
            continue
        if abs(goals[j] - l) < abs(goals[j] - r):
            currents[j] = l
        else:
            currents[j] = r
print(*result, sep='\n')
