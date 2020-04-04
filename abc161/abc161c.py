N, K = map(int, input().split())

result = N
if N > K:
    result = min(result, N % K)
for i in range(1000):
    result = min(result, abs(result - K))
print(result)
