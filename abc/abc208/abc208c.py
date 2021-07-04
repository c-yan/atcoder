N, K, *a = map(int, open(0).read().split())

result = [K // N] * N
for i, _ in sorted(enumerate(a), key=lambda x: x[1])[:K % N]:
    result[i] += 1
print(*result, sep='\n')
