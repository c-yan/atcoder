n, m = map(int, input().split())
if n > m:
    n, m = m, n
if n == 1:
    if m == 1:
        print(1)
    elif m == 2:
        print(0)
    else:
        print(m - 2)
elif n == 2:
    print(0)
else:
    print((n - 2) * (m - 2))
