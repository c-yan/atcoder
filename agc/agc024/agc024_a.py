A, B, C, K = map(int, input().split())

if K % 2 == 0:
    t = A - B
else:
    t = B - A
if t > 10 ** 18:
    print('Unfair')
else:
    print(t)
