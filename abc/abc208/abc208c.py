N, K, *a = map(int, open(0).read().split())

result = [K // N] * N
a = sorted(enumerate(a), key=lambda x: x[1])
for i in range(K % N):
    result[a[i][0]] += 1
print(*result, sep='\n')
