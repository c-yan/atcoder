N = int(input())
A = list(map(int, input().split()))

a = A[:-1]
for i in range(1, N - 1):
    a[i] += a[i - 1]

l = sum(A)
print(min(abs(p + p - l) for p in a))
