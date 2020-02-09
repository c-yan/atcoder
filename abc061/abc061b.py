N, M = map(int, input().split())

result = [0] * N
for _ in range(M):
    a, b = map(int, input().split())
    result[a - 1] += 1
    result[b - 1] += 1

for i in result:
    print(i)
