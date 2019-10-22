# 二分探索
from bisect import bisect_left

N = int(input())
L = list(map(int, input().split()))

L.sort()
result = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        result += bisect_left(L, L[i] + L[j]) - j - 1
print(result)
