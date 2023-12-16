N = int(input())
A = list(map(int, input().split()))

limit = 10 ** 18
A.sort()
result = A[0]
for a in A[1:]:
    result *= a
    if result > limit:
        print(-1)
        exit()
print(result)
