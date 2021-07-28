from math import gcd

A, B = map(int, input().split())

x = A * B // gcd(A, B)
if x > 10 ** 18:
    print('Large')
else:
    print(x)
