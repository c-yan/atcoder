from collections import deque
from bisect import bisect_left

N = int(input())
A = [int(input()) for _ in range(N)]

t = deque([A[0]])
for a in A[1:]:
    if a <= t[0]:
        t.appendleft(a)
    else:
        t[bisect_left(t, a) - 1] = a
print(len(t))
