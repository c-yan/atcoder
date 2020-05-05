# 二分探索
from bisect import bisect_left, bisect_right

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

for x in [A, B, C]:
    x.sort()

result = 0
for b in B:
    a = bisect_left(A, b)
    c = N - bisect_right(C, b)
    result += a * c
print(result)
