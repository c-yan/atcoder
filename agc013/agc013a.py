N = int(input())
A = list(map(int, input().split()))
result = 1
d = 0
for i in range(1, N):
    if A[i - 1] == A[i]:
        continue
    if d == 0:
        if A[i - 1] > A[i]:
            d = -1
        else:
            d = 1
    elif d == 1 and A[i - 1] > A[i]:
        d = 0
        result += 1
    elif d == -1 and A[i - 1] < A[i]:
        d = 0
        result += 1
print(result)
