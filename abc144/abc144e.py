# PyPy なら通る
# 二分探索
def is_ok(x):
    result = 0
    for i in range(N):
        a = A[i]
        t = x // F[i]
        if t < a:
            result += a - t
    return result <= K


N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))

A.sort()
F.sort(reverse=True)

l = -1
r = A[-1] * F[0]
while r > l+1:
    m = l + (r - l) // 2
    if is_ok(m):
        r = m
    else:
        l = m
print(r)
