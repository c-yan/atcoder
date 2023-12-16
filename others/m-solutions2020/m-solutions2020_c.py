N, K = map(int, input().split())
A = list(map(int, input().split()))

result = []
for i in range(K, N):
    if A[i] > A[i - K]:
        result.append('Yes')
    else:
        result.append('No')
print(*result, sep='\n')
