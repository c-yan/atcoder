N = int(input())
p = list(map(int, input().split()))

result = 0
for i in range(N - 1):
    if p[i] != i + 1:
        continue
    result += 1
    p[i], p[i + 1] = p[i + 1], p[i]
if p[N - 1] == N:
    result += 1
print(result)
