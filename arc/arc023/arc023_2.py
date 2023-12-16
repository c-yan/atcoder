R, C, D = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]

result = 0
for r in range(R):
    for c in range(C):
        t = D - r - c
        if t < 0 or t % 2 != 0:
            continue
        result = max(result, A[r][c])
print(result)
