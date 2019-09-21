n, l = [int(e) for e in input().split()]
if l < 0 and n + l - 1 > 0:
    print(sum(range(l, n + l)))
else:
    if abs(l) > abs(n + l - 1):
        print(sum(range(l, n + l)) - (n + l - 1))
    else:
        print(sum(range(l, n + l)) - l)
