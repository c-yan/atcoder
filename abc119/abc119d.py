# 二分探索
from bisect import bisect_left

INF = float('inf')

def f(x, s, t):
    result = INF
    i = bisect_left(s, x)
    if i > 0:
        j = bisect_left(t, s[i - 1])
        if j > 0:
            result = min(result, (x - s[i - 1]) + (s[i - 1] - t[j - 1]))
        if j < len(t):
            result = min(result, (x - s[i - 1]) + (t[j] - s[i - 1]))
    if i < len(s):
        j = bisect_left(t, s[i])
        if j > 0:
            result = min(result, (s[i] - x) + (s[i] - t[j - 1]))
        if j < len(t):
            result = min(result, (s[i] - x) + (t[j] - s[i]))
    return result


A, B, Q = map(int, input().split())
s = [int(input()) for _ in range(A)]
t = [int(input()) for _ in range(B)]

for i in range(Q):
    x = int(input())
    print(min(f(x, s, t), f(x, t, s)))
