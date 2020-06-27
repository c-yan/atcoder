# 二分探索
N = int(input())
A = [int(input()) for _ in range(N)]

t = [A[0]]
for a in A[1:]:
    if t[-1] >= a:
        t.append(a)
        continue
    ok = len(t) - 1
    ng = -1
    while ok - ng > 1:
        m = (ok + ng) // 2
        if t[m] < a:
            ok = m
        else:
            ng = m
    t[ok] = a
print(len(t))
