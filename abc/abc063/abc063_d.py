from bisect import bisect_right

N, A, B, *h = map(int, open(0).read().split())

h.sort()
d = A - B

ng = (h[-1] + (A - 1)) // A - 1
ok = (h[-1] + (B - 1)) // B
while ok - ng > 1:
    m = (ok + ng) // 2
    b = B * m
    if m >= sum((h[i] - b + (d - 1)) // d for i in range(bisect_right(h, b), N)):
        ok = m
    else:
        ng = m
print(ok)
