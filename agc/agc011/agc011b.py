N = int(input())
A = list(map(int, input().split()))

A.sort()
a = A[0]
result = 1
for i in range(1, N):
    if a * 2 >= A[i]:
        result += 1
    else:
        result = 1
    a += A[i]
print(result)
