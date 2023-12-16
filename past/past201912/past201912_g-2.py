from itertools import product

N = int(input())
a = [list(map(int, input().split())) for _ in range(N - 1)]

result = -float('inf')
for g in product(range(3), repeat=N):
    t = 0
    for i in range(N):
        for j in range(i + 1, N):
            if g[i] == g[j]:
                t += a[i][j - i - 1]
    result = max(result, t)
print(result)
