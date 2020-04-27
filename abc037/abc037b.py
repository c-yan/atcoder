N, Q = map(int, input().split())

result = [0] * (N + 1)
for _ in range(Q):
    L, R, T = map(int, input().split())
    for i in range(L, R + 1):
        result[i] = T

for i in result[1:]:
    print(i)
