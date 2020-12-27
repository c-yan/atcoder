from bisect import bisect_left

N, T, *A = map(int, open(0).read().split())

s0 = {0}
for a in A[:N // 2]:
    for x in s0.copy():
        if x + a > T:
            continue
        s0.add(x + a)

s1 = {0}
for a in A[N // 2:]:
    for x in s1.copy():
        if x + a > T:
            continue
        s1.add(x + a)

ys = sorted(s1)
result = 0
for x in s0:
    i = bisect_left(ys, T - x + 1) - 1
    result = max(result, x + ys[i])
print(result)
