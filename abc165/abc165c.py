from itertools import combinations_with_replacement

N, M, Q = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(Q)]

result = 0
for A in combinations_with_replacement(range(1, M + 1), N):
    t = 0
    for a, b, c, d in abcd:
        if A[b - 1] - A[a - 1] == c:
            t += d
    result = max(result, t)
print(result)
