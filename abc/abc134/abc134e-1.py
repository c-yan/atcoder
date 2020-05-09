from collections import deque
from bisect import bisect_left

N = int(input())
A = [int(input()) for _ in range(N)]

t = deque([A[0]])
for a in A[1:]:
    i = bisect_left(t, a) - 1
    if i == -1:
        t.appendleft(a)
    else:
        t[i] = a
print(len(t))
