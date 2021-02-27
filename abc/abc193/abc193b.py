INF = 10 ** 18

N = int(input())

result = INF
for _ in range(N):
    A, P, X = map(int, input().split())
    if X - A > 0:
        result = min(result, P)
if result == INF:
    print(-1)
else:
    print(result)
