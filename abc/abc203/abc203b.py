N, K = map(int, open(0).read().split())

result = 0
for i in range(N):
    for j in range(K):
        result += (i + 1) * 100 + (j + 1)
print(result)
