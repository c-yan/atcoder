from math import gcd

A, B = map(int, input().split())

x = B // gcd(A, B)
if x > 10 ** 18 // A:
    print('Large')
else:
    print(A * x)
