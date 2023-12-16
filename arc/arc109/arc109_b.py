n = int(input())

ok = 1
ng = 10 ** 18 + 2
while ng - ok > 1:
    m = ok + (ng - ok) // 2
    if m * (m + 1) // 2 <= n + 1:
        ok = m
    else:
        ng = m
print(n - ok + 1)
