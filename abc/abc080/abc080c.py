N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]

result = -float('inf')
for i in range(1, 1024):
    t = 0
    for j in range(N):
        t += P[j][sum((i >> k & 1) & F[j][k] for k in range(10))]
    if t > result:
        result = t
print(result)
