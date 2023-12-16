N, *A = map(int, open(0).read().split())

A.sort()
s = sum(A)
result = 0
for i in range(N):
    a = A[i]
    s -= a
    result += s - a * (N - i - 1)
print(result)
