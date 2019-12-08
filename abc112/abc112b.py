N, T = map(int, input().split())

result = float('inf')
for _ in range(N):
    c, t = map(int, input().split())
    if t <= T and c < result:
        result = c
if result != float('inf'):
    print(result)
else:
    print('TLE')
