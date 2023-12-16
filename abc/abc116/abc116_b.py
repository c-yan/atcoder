def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


s = int(input())

a = [0] * 1000000
a[0] = s
for i in range(1, 1000000):
    a[i] = f(a[i - 1])

t = set()
for i in range(1000000):
    if a[i] in t:
        print(i + 1)
        break
    t.add(a[i])
