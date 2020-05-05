# PyPy なら通る
# 二分探索
def is_ok(x):
    trainings = 0
    for i in range(N):
        t = A[i] - x // F[i]
        if t > 0:
            trainings += t
    return trainings <= K


N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))

A.sort()
F.sort(reverse=True)

ng = -1
ok = A[-1] * F[0]
while ok - ng > 1:
    m = ng + (ok - ng) // 2
    if is_ok(m):
        ok = m
    else:
        ng = m
print(ok)
