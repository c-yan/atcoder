from bisect import bisect_left

N, M = map(int, input().split())
X, Y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = 0
t = 0
while True:
    i = bisect_left(a, t)
    if i == len(a):
        break
    t = a[i] + X
    i = bisect_left(b, t)
    if i == len(b):
        break
    t = b[i] + Y
    result += 1
print(result)
