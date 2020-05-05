N = int(input())
K = int(input())

result = 1
for _ in range(N):
    result = min(result * 2, result + K)
print(result)
