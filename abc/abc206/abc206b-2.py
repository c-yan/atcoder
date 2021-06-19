N = int(input())

ok = 10 ** 5
ng = 0
while ok - ng > 1:
    m = ng + (ok - ng) // 2
    if m * (m + 1) // 2 >= N:
        ok = m
    else:
        ng = m
print(ok)
