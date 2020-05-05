N = int(input())
A = list(map(int, input().split()))

result = []
for i in range(N):
    x = i
    j = 1
    x = A[x] - 1
    while x != i:
        x = A[x] - 1
        j += 1
    result.append(j)
print(*result)
