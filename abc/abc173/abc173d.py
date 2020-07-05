N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
result = 0
for i in range(N - 1):
    result += A[(i + 1) // 2]
print(result)
