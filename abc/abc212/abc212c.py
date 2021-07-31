from bisect import bisect_left

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.sort()

result = 10 ** 9
for a in A:
    i = bisect_left(B, a)
    if i != 0:
        result = min(result, abs(a - B[i - 1]))
    if i != M:
        result = min(result, abs(a - B[i]))
print(result)
