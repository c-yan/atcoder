from itertools import permutations

N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]

result = 0
for p in permutations(range(1, N)):
    i = 0
    t = 0
    for x in p:
        t += T[i][x]
        i = x
    t += T[i][0]
    if t == K:
        result += 1
print(result)
