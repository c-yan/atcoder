from itertools import accumulate
from bisect import bisect_left

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = [0] + list(accumulate(A))
b = [0] + list(accumulate(B))

result = 0
for i in range(N + 1):
    t = K - a[i]
    if t < 0:
        break
    j = bisect_left(b, t)
    if j == M + 1:
        result = max(result, i + M)
    elif b[j] == t:
        result = max(result, i + j)
    else:
        result = max(result, i + j - 1)
print(result)
