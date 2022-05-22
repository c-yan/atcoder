from bisect import bisect_left, bisect_right

N, *A = map(int, open(0).read().split())

A.sort()

result = 0
for j in range(1, N - 1):
    i = bisect_right(A, A[j] - 1)
    k = bisect_left(A, A[j] + 1)
    result += i * (N - k)
print(result)
