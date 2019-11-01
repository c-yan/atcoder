def f(n, a, p, r):
    for i in range(1, n):
        t = p + a[i]
        if p < 0 and t <= 0:
            r += 1 - t
            t = 1
        elif p > 0 and t >= 0:
            r += t + 1
            t = -1
        p = t
    return r


n = int(input())
a = list(map(int, input().split()))

# 最初がプラス
p = a[0]
r = 0
if p <= 0:
    r += 1 - p
    p = 1
result1 = f(n, a, p, r)

# 最初がマイナス
p = a[0]
r = 0
if p >= 0:
    r += p + 1
    p = -1
result2 = f(n, a, p, r)

print(min(result1, result2))
