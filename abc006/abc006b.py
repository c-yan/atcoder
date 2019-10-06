n = int(input())

if n == 1:
    print(0)
elif n == 2:
    print(0)
elif n == 3:
    print(1)
else:
    a = [0] * (n + 1)
    a[3] = 1
    for i in range(4, n + 1):
        a[i] = (a[i - 1] + a[i - 2] + a[i - 3]) % 10007
    print(a[n])
