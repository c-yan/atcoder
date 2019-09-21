a, b, c, k = map(int, input().split())
if k % 2 == 0:
    t = a - b
else:
    t = b - a
if t > 10 ** 18:
    print('Unfair')
else:
    print(t)
