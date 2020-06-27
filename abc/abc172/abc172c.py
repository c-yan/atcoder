from itertools import accumulate
from bisect import bisect_left

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = list(accumulate(A))
b = list(accumulate(B))

result = 0
j = bisect_left(b, K)
if j == M:
  result = M
elif b[j] == K:
    result = j + 1
else:
    result = j
for i in range(N):
    t = K - a[i]
    if t < 0:
        break
    j = bisect_left(b, t)
    if j == M:
        result = max(result, i + 1 + M)
    elif b[j] == t:
        result = max(result, i + 1 + j + 1)
    else:
        result = max(result, i + 1 + j)
print(result)
